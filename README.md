# AIML-IRIS-ASSIGNMENT
This project is a submission for the AI/ML Engineer position at **IRIS Business Services Ltd.**  
It demonstrates the use of **FastAPI** to process an Excel file and expose useful API endpoints for interacting with its contents.

---

## 📁 Project Overview

The application:
- Reads a provided Excel file (`capbudg.xls`)
- Extracts tables and rows
- Calculates row-wise numeric totals
- Exposes three endpoints via a RESTful API

---

## 🔧 Tech Stack

- **FastAPI** for backend API
- **Pandas** for Excel file processing
- **Uvicorn** for running the server
- **Postman** for API testing

---

## 📌 API Endpoints

### 1. `GET /list_tables`
Returns all sheet names (tables) in the Excel file.

**Response Example:**
```json
{
  "tables": ["CapBudgWS"]
}

### 2. 'GET /get_table_details?table_name=CapBudgWS'
Returns all row names (first column) from the selected table.

**Response Example:**
```json
{
  "table_name": "CapBudgWS",
  "row_names": [
    "Initial Investment=",
    "Opportunity cost (if any)=",
    "Lifetime of the investment"
  ]
}

### 3. 'GET /row_sum?table_name=CapBudgWS&row_name=Initial Investment='
Calculates and returns the sum of all numeric values in a specific row.

**Response Example:**
```json
{
  "table_name": "CapBudgWS",
  "row_name": "Initial Investment=",
  "sum": 250000
}



▶️ How to Run the Project
🛠️ 1. Install Dependencies
pip install fastapi uvicorn pandas openpyxl xlrd


🚀 2. Run the App
uvicorn main:app --reload --port 9090

🌐 3. Open Swagger UI
Visit http://localhost:9090/docs to interact with the API.

📦 Postman Collection
A Postman collection is included for easy testing.

File: IRIS_Postman_Collection.json

Import into Postman and test:
/list_tables

/get_table_details

/row_sum


💡 Potential Improvements
Accept Excel file uploads via POST API

Add frontend interface to explore tables and values

Handle multiple Excel formats and irregular sheets

⚠️ Known Edge Cases
Table or row names must match exactly (case-sensitive)

Rows with text or missing values are safely ignored in summation

Only .xls is currently tested (not .xlsx)


👤 Author
Aarohi Parag Pisolkar
B.E. Artificial Intelligence and Data Science
LinkedIn • GitHub • Email

