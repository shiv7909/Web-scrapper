
from flask import Flask, request, render_template, send_file
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time
import os
import re

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
OUTPUT_FILE = "student_results.xlsx"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

RESULTS_URL = "https://egovernance.unom.ac.in/results/ugresult.asp"

def setup_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-dev-shm-usage")
    service = Service()
    driver = webdriver.Chrome(service=service, options=options)
    return driver

def is_valid_name(text):
    """Check if text is a valid name (only alphabets & spaces, no numbers or register number)."""
    return bool(re.match(r"^[A-Za-z\s]+$", text))  

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "No file part"
    file = request.files['file']
    if file.filename == '':
        return "No selected file"
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(filepath)
    
    df = pd.read_excel(filepath)
    results = []
    driver = setup_driver()
    
    for index, row in df.iterrows():
        try:
            register_no = str(row["Register Number"]).strip()
            dob = str(row["Date of Birth"]).strip()
            
            print(f"\n🔍 Fetching data for Register Number: {register_no} | DOB: {dob}")
            
            driver.get(RESULTS_URL)
            WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.NAME, "regno")))

            reg_input = driver.find_element(By.NAME, "regno")
            dob_input = driver.find_element(By.NAME, "pwd")
            submit_btn = driver.find_element(By.XPATH, "//input[@type='button' and @value='Get Result']")
            
            reg_input.send_keys(register_no)
            dob_input.send_keys(dob)
            submit_btn.click()
            
            WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, "//table[contains(@class, 'bordered')]")))
            time.sleep(2)

            student_data = {
                "Register Number": register_no,
                "DOB": dob,
                "Name": "",
                "Subjects": []
            }
            
            print("✅ Successfully loaded result page.")

            tables = driver.find_elements(By.XPATH, "//table[contains(@class, 'bordered')]")
            for table in tables:
                rows = table.find_elements(By.TAG_NAME, "tr")
                
                for row in rows:
                    cols = row.find_elements(By.TAG_NAME, "td")

                    if len(cols) == 2:
                        heading = cols[0].text.strip()
                        data = cols[1].text.strip()

                        if "Name" in heading and student_data["Name"] == "":
                            student_data["Name"] = data  
                            print(f"🆔 Extracted Name: {data}")  
                        elif "register" not in heading.lower() and "dob" not in heading.lower():  
                            student_data[heading] = data

                    elif len(cols) >= 5:  
                        # **Skip the first row with "UE IA TOTAL RESULT"**
                        if "UE" in cols[0].text and "IA" in cols[1].text:
                            continue  # Skip this row
                        
                        subject_data = {
                            "UE": cols[1].text.strip(),
                            "IA": cols[2].text.strip(),
                            "Total": cols[3].text.strip(),
                            "Result": cols[4].text.strip()
                        }
                        student_data["Subjects"].append(subject_data)
                        print(f"📚 Extracted Subject: {subject_data}")  
                        
            results.append(student_data)
            time.sleep(2)
            
        except Exception as e:
            print(f"❌ Error fetching results for {register_no}: {e}")
    
    driver.quit()
    
    structured_data = []
    for student in results:
        base_data = {
            "Register Number": student["Register Number"],
            "DOB": student["DOB"],
            "Name": student["Name"]  
        }
        
        first_subject = True
        for subject in student["Subjects"]:
            row_data = base_data.copy()
            if first_subject:
                first_subject = False  
            else:
                row_data["Register Number"] = ""  
                row_data["DOB"] = ""
                row_data["Name"] = ""

            row_data.update(subject)
            structured_data.append(row_data)

    final_df = pd.DataFrame(structured_data)
    final_df.to_excel(OUTPUT_FILE, index=False, engine='openpyxl')
    
    print("\n📄 Results saved to:", OUTPUT_FILE)
    
    return send_file(OUTPUT_FILE, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
