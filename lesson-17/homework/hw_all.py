import pandas as pd
import sqlite3

# 1. Merging and Joining

# 1.1 Inner Join on Chinook Database
def inner_join_chinook():
    conn = sqlite3.connect("chinook.db")
    customers = pd.read_sql_query("SELECT * FROM customers", conn)
    invoices = pd.read_sql_query("SELECT * FROM invoices", conn)
    joined = pd.merge(customers, invoices, on="CustomerId", how="inner")
    total_invoices = joined.groupby("CustomerId").size().reset_index(name="InvoiceCount")
    print("1.1 Total invoices per customer:\n", total_invoices.head())

# 1.2 Outer Join on Movie Data
def outer_join_movies():
    movies = pd.read_csv("movie.csv")
    df1 = movies[['director_name', 'color']].drop_duplicates()
    df2 = movies[['director_name', 'num_critic_for_reviews']].drop_duplicates()

    left_join = pd.merge(df1, df2, on='director_name', how='left')
    outer_join = pd.merge(df1, df2, on='director_name', how='outer')

    print("1.2 Left join row count:", len(left_join))
    print("1.2 Outer join row count:", len(outer_join))


# 2. Grouping and Aggregating

# 2.1 Grouped Aggregations on Titanic
def titanic_grouping():
    df = pd.read_csv("titanic.csv")
    result = df.groupby("Pclass").agg({
        "Age": "mean",
        "Fare": "sum",
        "PassengerId": "count"
    }).rename(columns={"PassengerId": "PassengerCount"}).reset_index()
    print("2.1 Titanic grouping:\n", result)

# 2.2 Multi-level Grouping on Movies
def movie_multilevel_group():
    df = pd.read_csv("movie.csv")
    result = df.groupby(["color", "director_name"]).agg({
        "num_critic_for_reviews": "sum",
        "duration": "mean"
    }).reset_index()
    print("2.2 Movie multi-grouping:\n", result.head())

# 2.3 Nested Grouping on Flights
def flight_grouping():
    df = pd.read_csv("flights.csv")
    result = df.groupby(["Year", "Month"]).agg({
        "FlightNum": "count",
        "ArrDelay": "mean",
        "DepDelay": "max"
    }).rename(columns={"FlightNum": "TotalFlights"}).reset_index()
    print("2.3 Flights nested grouping:\n", result.head())


# 3. Applying Functions

# 3.1 Age Group on Titanic
def titanic_age_group():
    df = pd.read_csv("titanic.csv")

    def classify_age(age):
        if pd.isnull(age):
            return None
        elif age < 18:
            return "Child"
        else:
            return "Adult"

    df["Age_Group"] = df["Age"].apply(classify_age)
    print("3.1 Age groups:\n", df[["Age", "Age_Group"]].head())

# 3.2 Normalize Salaries
def normalize_salary():
    df = pd.read_csv("employee.csv")
    df["NormalizedSalary"] = df.groupby("Department")["Salary"].transform(lambda x: (x - x.mean()) / x.std())
    print("3.2 Normalized salaries:\n", df.head())

# 3.3 Movie Duration Category
def movie_duration_cat():
    df = pd.read_csv("movie.csv")

    def duration_label(x):
        if pd.isnull(x):
            return None
        elif x < 60:
            return "Short"
        elif x <= 120:
            return "Medium"
        else:
            return "Long"

    df["Duration_Category"] = df["duration"].apply(duration_label)
    print("3.3 Movie duration categories:\n", df[["duration", "Duration_Category"]].head())


# 4. Using pipe

# 4.1 Titanic Pipeline
def titanic_pipeline():
    df = pd.read_csv("titanic.csv")

    def filter_survivors(df): return df[df["Survived"] == 1]
    def fill_missing_age(df): return df.assign(Age=df["Age"].fillna(df["Age"].mean()))
    def add_fare_per_age(df): return df.assign(Fare_Per_Age=df["Fare"] / df["Age"])

    result = df.pipe(filter_survivors).pipe(fill_missing_age).pipe(add_fare_per_age)
    print("4.1 Titanic pipeline:\n", result[["Survived", "Age", "Fare", "Fare_Per_Age"]].head())

# 4.2 Flights Pipeline
def flights_pipeline():
    df = pd.read_csv("flights.csv")

    def filter_long_delays(df): return df[df["DepDelay"] > 30]
    def compute_delay_ratio(df): return df.assign(Delay_Per_Hour=df["DepDelay"] / df["AirTime"])

    result = df.pipe(filter_long_delays).pipe(compute_delay_ratio)
    print("4.2 Flights pipeline:\n", result[["DepDelay", "AirTime", "Delay_Per_Hour"]].head())


# RUN ALL FUNCTIONS
if __name__ == "__main__":
    inner_join_chinook()
    outer_join_movies()
    titanic_grouping()
    movie_multilevel_group()
    flight_grouping()
    titanic_age_group()
    normalize_salary()
    movie_duration_cat()
    titanic_pipeline()
    flights_pipeline()
