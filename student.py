import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("students.csv")

# Show data
print("Dataset:\n", df)

# Info & stats
print("\nInfo:")
print(df.info())

print("\nStatistics:")
print(df.describe())

# Create Total & Average
df["Total"] = df["Math"] + df["Science"] + df["English"]
df["Average"] = df["Total"] / 3

print("\nUpdated Data:\n", df)

# Find Topper
topper = df.loc[df["Total"].idxmax()]
print("\nTopper:\n", topper)

# Find Failed Students (marks < 40)
fail_students = df[
    (df["Math"] < 40) |
    (df["Science"] < 40) |
    (df["English"] < 40)
]

print("\nFailed Students:\n", fail_students)

# ---- Visualization ---- #

# Bar chart for Total Marks
plt.figure()
plt.bar(df["Name"], df["Total"])
plt.title("Total Marks of Students")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()

# Seaborn barplot for Average
plt.figure()
sns.barplot(x="Name", y="Average", data=df)
plt.title("Average Marks of Students")
plt.show()