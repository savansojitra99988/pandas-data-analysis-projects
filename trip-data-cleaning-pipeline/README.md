# Trip Data Cleaning & Analysis Pipeline

## 📌 Overview
This project demonstrates a complete data pipeline:
- Connect to a MySQL database
- Load data into Pandas
- Perform cleaning and transformations
- Analyze with grouping and pivot tables
- Export results to Excel
- Post cleaned data back into SQL

It’s designed as a practical mini‑project for learning **SQL + Pandas + Data Cleaning**.

---

## ⚙️ Steps Implemented
1. **Database Connection**  
   Connect to MySQL using SQLAlchemy and PyMySQL.

2. **Data Loading**  
   Load the `trip` table into a Pandas DataFrame.

3. **Cleaning**  
   - Normalize emails (lowercase + strip spaces)  
   - Clean names (remove special characters)  
   - Remove duplicates  

4. **Transformations**  
   - Convert age to numeric  
   - Categorize into age groups (Teen, Young, Adult, Senior)  
   - Add derived columns: rank, cumulative age  

5. **Analysis**  
   - Average age by gender  
   - Record counts by name  
   - Pivot table (gender vs age_group average ages)  

6. **Export**  
   Save cleaned data to `cleaned_trip.xlsx`.

7. **SQL Posting**  
   Write cleaned data back into a new SQL table `trip_cleaned`.

---

## 📂 Project Structure
