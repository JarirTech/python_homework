import pandas as pd

# Sample data with dates in various formats and some invalid values
data = {
    "Event": ["Project Start", "Client Meeting", "Beta Release", "Final Launch"],
    "Date": ["2021/01/15", "2021-02-30", "03-15-2021", "April 31, 2021"]  # Some invalid or unusual dates
}
df = pd.DataFrame(data)

print("Before conversion:")
print(df)

# Convert 'Date' to datetime
# errors="coerce" will turn invalid dates into NaT (Not a Time)
df["Date_converted"] = pd.to_datetime(df["Date"], errors="coerce")

print("\nAfter converting to datetime:")
print(df)

# You can check how many values became NaT (invalid dates)
num_invalid_dates = df["Date_converted"].isna().sum()
print(f"\nNumber of invalid dates converted to NaT: {num_invalid_dates}")


