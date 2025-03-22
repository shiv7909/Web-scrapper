# Web-scrapper

Student Result Scraper & Processor

Overview

This project automates the extraction of student results from the University of Madras results portal using Flask, Selenium, and Pandas. The extracted data is processed and saved into an Excel sheet.

Features

Automated Data Extraction: Uses Selenium to fetch student results based on Register Number and DOB.

Web-based Upload Interface: A Flask-based web interface to upload Excel files containing student details.

Excel File Processing: Extracted results are structured and exported to a clean Excel format.

Dark Themed UI: Modern interface with animations and a loading indicator for a smooth user experience.

Project Structure

student_results_scraper/
│-- templates/
│   │-- index.html                # Frontend UI for uploading files
│-- app.py                         # Main Flask application
Installation

1️⃣ Prerequisites

Ensure you have Python 3.x installed.

2️⃣ Install Dependencies

pip install -r requirements.txt

3️⃣ Run the Flask App

python app.py

Requirements

Create a requirements.txt file and include the following dependencies:

Flask
selenium
pandas
openpyxl
requests
webdriver-manager

Install them using:

pip install -r requirements.txt

Usage

Run the Flask app.

Open the browser and go to http://127.0.0.1:5000.

Upload an Excel file with Register Numbers & DOBs.

The script will scrape the data and automatically download the processed file.

Expected Excel Output Format

Register Number

DOB

Name

UE Marks

IA Marks

Total Marks

Result

222410482

28/08/2006

RAJALAKSHMI P

063

023

086

PASS







048

020

068

PASS







058

023

081

PASS

Debugging & Logs

To track extraction progress, check the terminal logs:

🆔 Extracted Name: ...

📚 Extracted Subject: ...

📄 Results saved to: student_results.xlsx
