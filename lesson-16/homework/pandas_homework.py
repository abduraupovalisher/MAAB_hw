# pandas_homework.py

import pandas as pd
import sqlite3

# --- Part 1: Reading Files ---

# 1. chinook.db - Read customers table
conn = sqlite3.connect('chinook.db')
customers_df = pd.read_sql_query("SELECT * FROM customers", conn)
print("First 10 rows from 'customers' table:")
print(customers_df.head(10))

# 2. iris.json - Load and display shape and columns
iris_df = pd.read_json('iris.json')
print("\nIris DataFrame Shape:", iris_df.shape)
print("Iris Column Names:", iris_df.columns.tolist())

# 3. titanic.xlsx - Load and show head
titanic_df = pd.read_excel('titanic.xlsx')
print("\nFirst 5 rows of Titanic DataFrame:")
print(titanic_df.head())

# 4. flights.parquet - Load and use info
flights_df = pd.read_parquet('flights.parquet')
print("\nFlights DataFrame Info:")
flights_df.info()

# 5. movie.csv - Load and show random 10 rows
movies_df = pd.read_csv('movie.csv')
print("\nRandom 10 rows from Movie DataFrame:")
print(movies_df.sample(10))

# --- Part 2: Exploring DataFrames ---

# 1. iris.json - lowercase columns and select specific
iris_df.columns = iris_df.columns.str.lower()
iris_selected = iris_df[['sepal_length', 'sepal_width']]
print("\nSelected Columns from Iris:")
print(iris_selected.head())

# 2. titanic.xlsx - filter and value_counts
age_filtered = titanic_df[titanic_df['Age'] > 30]
print("\nTitanic Passengers older than 30:")
print(age_filtered)

print("\nGender Counts:")
print(titanic_df['Sex'].value_counts())

# 3. flights.parquet - select columns and count unique
print("\nOrigin, Destination, Carrier columns from Flights:")
print(flights_df[['origin', 'dest', 'carrier']].head())

print("\nNumber of unique destinations:", flights_df['dest'].nunique())

# 4. movie.csv - filter duration > 120, sort by director likes
long_movies = movies_df[movies_df['duration'] > 120]
sorted_movies = long_movies.sort_values(by='director_facebook_likes', ascending=False)
print("\nFiltered & Sorted Movies (duration > 120):")
print(sorted_movies[['movie_title', 'duration', 'director_name', 'director_facebook_likes']].head())

# --- Part 3: Challenges and Explorations ---

# iris.json - mean, median, std
print("\nIris Statistics:")
print("Mean:\n", iris_df.mean(numeric_only=True))
print("Median:\n", iris_df.median(numeric_only=True))
print("Standard Deviation:\n", iris_df.std(numeric_only=True))

# titanic.xlsx - min, max, sum of ages
print("\nTitanic Age Stats:")
print("Min Age:", titanic_df['Age'].min())
print("Max Age:", titanic_df['Age'].max())
print("Sum of Ages:", titanic_df['Age'].sum())

# movie.csv - top director by likes, 5 longest movies
top_director = movies_df.groupby('director_name')['director_facebook_likes'].sum().idxmax()
print("\nDirector with highest total Facebook likes:", top_director)

top5_longest = movies_df.nlargest(5, 'duration')[['movie_title', 'duration', 'director_name']]
print("\nTop 5 Longest Movies:")
print(top5_longest)

# flights.parquet - check & fill missing values
print("\nMissing Values in Flights Data:")
print(flights_df.isnull().sum())

# Fill missing numerical values with mean
numeric_cols = flights_df.select_dtypes(include='number').columns
for col in numeric_cols:
    flights_df[col].fillna(flights_df[col].mean(), inplace=True)

print("\nFilled missing numeric values in Flights DataFrame.")


