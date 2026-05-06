import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("C:\\Users\\Meet Modi\\OneDrive\\Desktop\\Netflix Data Analytics Project\\netflix_titles.xlsx")

print(df.describe())
print(df.info())

print(df.isnull().sum())

df["director"] = df["director"].fillna("Unknown")
df["cast"] = df["cast"].fillna("Not Available")
df["country"] = df["country"].fillna("Unknown")
df["date_added"] = df["date_added"].fillna("NA")
df["rating"] = df["rating"].fillna("NA")
df["duration"] = df["duration"].fillna("NA")
print(df.isnull().sum())

""""
drop = df.drop_duplicates()
print(drop)

df.columns = df.columns.str.lower()
df.columns = df.columns.str.replace(" ","_")
print(df.columns)

da = df["date_added"] = pd.to_datetime(df["date_added"],errors="coerce")
print(da)

y = df["year_added"] = df["date_added"].dt.year
print(y)
month = df["month_added"] = df["date_added"].dt.month_name()
print(month)

#Separate Movie Duration and Tv Seasons

dur_no = df["duration_number"] = df["duration"].str.extract("(\d+)").astype("double")
print(dur_no)

dt = df["duration_type"] = df["duration"].str.replace("\d+","",regex=True).str.strip()
print(dt)

count = df["type"].value_counts()
print(count)

high_content = df["country"].value_counts().head(10)
print(high_content)

std_clean = df["country"] = df["country"].str.split(",").str[0]
print(std_clean)

print(df["country"].head(10))

rating_count = df["rating"].value_counts()
print(rating_count)

Yearly_released = df["release_year"].value_counts().sort_index()
print(Yearly_released)

genres = df["listed_in"].str.split(",",expand=True).stack()
print(genres.value_counts().head(5))


dn = df["duration_number"].isnull().sum()
print(dn)
dn1 = df["duration_number"] = df["duration_number"].fillna(0)
print(dn1)


df["type"].value_counts().plot(kind="bar")
plt.title("Data of Movies/Season")
plt.ylabel("Number of Years")
plt.show()

Yearly_released.plot()
plt.title("Netflix Content Growth")
plt.show()

df["country"].value_counts().plot(kind="bar")
plt.title("Top Countries")
plt.show()"""

df.to_csv("C:\\Users\\Meet Modi\\OneDrive\\Desktop\\Netflix Data Analytics Project\\Netflix_Update.csv")
print("File Saved Successfully.....")
