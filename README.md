
---

# **📌 Student Result Scraper & Processor**  
**Automates student result extraction from the University of Madras portal using Flask, Selenium, and Pandas.**  

---

## **📖 Overview**  
This project simplifies the process of fetching student results from the University of Madras results portal. It takes an **Excel file** containing Register Numbers and DOBs, scrapes the result data, and processes it into a structured Excel format.  

---

## **🚀 Features**  
✅ **Automated Data Extraction** – Uses Selenium to fetch student results dynamically.  
✅ **Web-based Upload Interface** – Flask-based UI for seamless file uploads.  
✅ **Excel File Processing** – Structures extracted results into a clean Excel format.  
✅ **Dark Themed UI** – Modern, animated UI with loading indicators for better UX.  

---

## **🛠 Tech Stack & Uses**  

| **Technology**        | **Purpose** |
|----------------------|-------------|
| **Flask**           | Web framework for handling the UI and backend logic. |
| **Selenium**        | Automates browser interaction to fetch student results. |
| **Pandas**          | Processes, structures, and exports extracted data to Excel. |
| **OpenPyXL**        | Handles Excel file operations (read/write). |
| **Requests**        | Manages HTTP requests for data retrieval. |
| **Webdriver-Manager** | Manages and auto-downloads the correct WebDriver for Selenium. |
| **HTML, CSS, JS**   | Frontend for the web-based file upload interface. |

---

## **📂 Project Structure**  
```
student_results_scraper/
│-- templates/
│   │-- index.html       # Frontend UI for file upload
│-- app.py               # Main Flask application

```

---

## **🛠 Installation**  

### **1️⃣ Prerequisites**  
Ensure you have **Python 3.x** installed on your system.  

### **2️⃣ Install Dependencies**  
Run the following command to install required packages:  
```bash
pip install -r requirements.txt
```

### **3️⃣ Run the Flask App**  
To start the web application, execute:  
```bash
python app.py
```

---

## **📋 Requirements**  
Create a `requirements.txt` file and include:  
```
Flask
selenium
pandas
openpyxl
requests
webdriver-manager
```
Install dependencies using:  
```bash
pip install -r requirements.txt
```

---

## **💡 Usage**  
1️⃣ Run the Flask application.  
2️⃣ Open a web browser and navigate to `http://127.0.0.1:5000`.  
3️⃣ Upload an Excel file containing **Register Numbers** and **DOBs**.  
4️⃣ The script scrapes the data and downloads the processed results file.  

---

## **📊 Expected Excel Output Format**  
| Register Number | DOB        | Name          | UE Marks | IA Marks | Total Marks | Result |
|----------------|-----------|--------------|----------|----------|-------------|--------|
| 222410482      | 28/08/2006 | RAJALAKSHMI P | 063      | 023      | 086         | PASS   |
|               |            |              | 048      | 020      | 068         | PASS   |
|               |            |              | 058      | 023      | 081         | PASS   |

---

## **🛠 Debugging & Logs**  
To track the extraction progress, check the terminal logs:  
```bash
🆔 Extracted Name: ...
📚 Extracted Subject: ...
📄 Results saved to: student_results.xlsx
```

