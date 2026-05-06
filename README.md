# Netflix_DataAnalytics_Project

# 🎬 Netflix Content Analytics Dashboard

## 📌 Overview

This project is an end-to-end **Data Analytics and Business Intelligence** solution focused on analyzing Netflix content data. The project transforms raw streaming platform data into meaningful business insights using Python, MySQL, and Power BI.

The analysis explores trends in movies, TV shows, genres, ratings, countries, release patterns, and audience-focused content strategies.

---

# 🎯 Project Objective

The main objective of this project is to:

* Analyze Netflix content trends
* Perform data cleaning and preprocessing
* Generate business-oriented SQL insights
* Build an interactive Power BI dashboard
* Present actionable recommendations through visualization and reporting

---

# 📂 Dataset Summary

* **Dataset Name:** Netflix Titles Dataset
* **Rows:** 8,807
* **Columns:** 12

## 🔑 Key Features

* Content Type (Movie / TV Show)
* Title
* Director
* Cast
* Country
* Release Year
* Date Added
* Rating
* Duration
* Genre / Category
* Description

---

# 🛠️ Tools & Technologies Used

* **Python** – Data Cleaning & Exploratory Data Analysis
* **Pandas & NumPy** – Data Manipulation
* **Matplotlib / Seaborn** – Visualization
* **MySQL** – Business-Oriented SQL Analysis
* **Power BI** – Interactive Dashboard Development
* **Gamma** – Presentation & Storytelling
* **Jupyter Notebook / VS Code** – Development Environment

---

# 🔄 Project Workflow

```text
Netflix Dataset
       ↓
Python Data Cleaning & EDA
       ↓
Feature Engineering
       ↓
MySQL Business Analysis
       ↓
Power BI Dashboard
       ↓
Business Insights & Recommendations
```

---

# 🧹 Data Cleaning & Preprocessing

The dataset was cleaned and prepared using Python.

## ✅ Steps Performed

* Handled missing values in:

  * director
  * cast
  * country
  * rating
  * date_added
* Removed duplicate records
* Standardized column names using snake_case format
* Converted date columns into datetime format
* Standardized country records
* Created additional analytical columns:

  * year_added
  * duration_number
  * duration_type

---

# 📊 Exploratory Data Analysis (EDA)

The following analyses were performed:

## 🔍 Analysis Areas

* Movies vs TV Shows distribution
* Top content-producing countries
* Ratings distribution
* Genre popularity analysis
* Release year trends
* Duration analysis
* Director analysis
* Audience-focused content trends

---

# 🗄️ MySQL Business Analysis

Business-oriented SQL queries were used to generate actionable insights.

## 📌 Key Business Questions

1. Which content type dominates Netflix?
2. Which countries produce the most content?
3. Which genres are most popular?
4. What is the trend of Netflix content growth?
5. Which audience ratings dominate the platform?
6. Which directors contribute the most titles?
7. What are the duration trends for movies and TV shows?

---

# 📈 Power BI Dashboard

An interactive Power BI dashboard was created to visualize insights.

## 📌 Dashboard Features

* KPI Cards
* Slicers & Filters
* Movies vs TV Shows Analysis
* Country-wise Content Analysis
* Genre Distribution
* Ratings Analysis
* Release Year Trends
* Duration Analysis

## 🎨 Dashboard Theme

* Netflix-inspired dark theme
* Red & black color palette
* Interactive visuals and filters
* Business-oriented dashboard layout

---

# 💡 Key Insights

* Movies dominate Netflix’s content library.
* USA and India contribute major content production.
* Drama and International Movies are highly popular categories.
* Netflix content increased significantly after 2015.
* TV-MA and TV-14 are among the most common ratings.

---

# 📌 Business Recommendations

* Invest more in high-performing genres.
* Expand regional content production.
* Improve audience targeting using ratings analysis.
* Increase focus on long-running TV shows.
* Optimize content strategy using trend analysis.

---

# 🚀 How to Run the Project

## 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/netflix-content-analytics.git
cd netflix-content-analytics
```

## 2️⃣ Install Required Libraries

```bash
pip install pandas numpy matplotlib seaborn sqlalchemy pymysql
```

## 3️⃣ Run Python Analysis

```bash
jupyter notebook
```

## 4️⃣ Configure MySQL Connection

Update database credentials in Python:

```python
mysql+pymysql://username:password@localhost:3306/netflix_analysis
```

## 5️⃣ Open Power BI Dashboard

Open the `.pbix` file in Power BI Desktop.

---

# 📂 Project Structure

```text
Netflix-Analytics-Project/
│
├── dataset/
├── python_analysis/
├── sql_queries/
├── dashboard/
├── screenshots/
├── presentation/
├── report/
└── README.md
```

---

# 📸 Dashboard Preview

Add your Power BI dashboard screenshots here.

---

# 📚 Learning Outcomes

This project helped strengthen skills in:

* Data Cleaning
* Exploratory Data Analysis
* SQL Querying
* Business Intelligence
* Dashboard Design
* Data Storytelling
* Corporate Analytics Workflow

---

# 📌 Conclusion

This project demonstrates an end-to-end corporate analytics workflow using Python, MySQL, and Power BI. It showcases the ability to clean raw data, perform business-oriented analysis, and present actionable insights through professional dashboards and reportin
