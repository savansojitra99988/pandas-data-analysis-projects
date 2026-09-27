# 🚗 Trip Data Cleaning Pipeline with Pandas & SQL

![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Cleaning-green?logo=pandas)
![SQL](https://img.shields.io/badge/SQL-Integration-orange?logo=mysql)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## 📌 Project Overview
This project is a **Trip Data Cleaning & Analysis pipeline** built with **Python, Pandas, and MySQL**.  
It demonstrates how to connect to a database, clean messy data, perform transformations, analyze with pivot tables, and export results back to Excel and SQL.

---

## ✨ Features
- Connect to **MySQL database** and load raw trip data.  
- Clean and normalize:
  - Emails (lowercase, strip spaces)
  - Names (remove special characters)
  - Remove duplicates  
- Convert **age to numeric** and categorize into groups (Teen, Young, Adult, Senior).  
- Add derived columns:
  - Rank by age
  - Cumulative age sum  
- Perform **grouping & aggregation**:
  - Average age by gender
  - Record counts by name  
- Generate **pivot tables**:
  - Gender vs Age Group average ages  
- Export cleaned data to **Excel**.  
- Post cleaned data back into **SQL table (`trip_cleaned`)**.  

---

## 📊 Sample Insights
- 👩 Females had higher average age in the dataset.  
- 🧑 Most entries fell into the **Teen** and **Adult** categories.  
- 📈 Cumulative age analysis shows growth trends across records.  

---

## 🚀 How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/pandas-projects.git
   cd pandas-projects/trip-data-cleaning-pipeline
