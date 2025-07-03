from fastapi import FastAPI, Query, HTTPException
from typing import List
import pandas as pd
import os

app = FastAPI()

# Load Excel file
excel_path = os.path.join("data", "capbudg.xls")
xls = pd.ExcelFile(excel_path)

@app.get("/list_tables")
def list_tables():
    return {"tables": xls.sheet_names}

@app.get("/get_table_details")
def get_table_details(table_name: str):
    if table_name not in xls.sheet_names:
        raise HTTPException(status_code=404, detail="Table not found.")
    
    df = xls.parse(table_name)
    row_names = df.iloc[:, 0].dropna().tolist()
    return {"table_name": table_name, "row_names": row_names}

@app.get("/row_sum")
def row_sum(table_name: str, row_name: str):
    if table_name not in xls.sheet_names:
        raise HTTPException(status_code=404, detail="Table not found.")
    
    df = xls.parse(table_name)
    
    # Find the row that matches the given row_name
    match_row = df[df.iloc[:, 0] == row_name]
    
    if match_row.empty:
        raise HTTPException(status_code=404, detail="Row not found.")

    numeric_values = pd.to_numeric(match_row.iloc[0, 1:], errors='coerce')
    total = numeric_values.sum(skipna=True)

    return {
        "table_name": table_name,
        "row_name": row_name,
        "sum": total
    }
