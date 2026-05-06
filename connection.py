from sqlalchemy import create_engine
import pandas as pd

df = pd.read_csv("C:\\Users\\Meet Modi\\OneDrive\\Desktop\\Netflix Data Analytics Project\\Netflix_Update.csv")
print(df.head())


username = "root"       # MySQL username
password = "9337"       # your MySQL password
host = "localhost"
port = "3306"           # MySQL default port
database = "db_netflix" # your MySQL database

engine = create_engine(
    f"mysql+pymysql://{username}:{password}@{host}:{port}/{database}"
)

# Step 2: Load DataFrame into MySQL
table_name = "netflix_data"

df.to_sql(table_name, con=engine, if_exists="replace", index=False)

print(f"✅ Data successfully loaded into table '{table_name}' in database '{database}'")