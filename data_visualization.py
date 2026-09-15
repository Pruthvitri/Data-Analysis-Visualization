import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px


# -----------------------------------
# 1. Create Dataset
# -----------------------------------

data = {
    "Name": [
        "Amit", "Rahul", "Priya", "Neha", "Riya",
        "Karan", "Jay", "Pooja", "Vivek", "Anjali"
    ],

    "Study_Hours": [2, 3, 4, 5, 6, 7, 8, 6, 9, 10],

    "Attendance": [65, 70, 75, 80, 85, 90, 92, 88, 95, 98],

    "Marks": [45, 50, 55, 62, 68, 75, 82, 78, 88, 94]
}

df = pd.DataFrame(data)


# -----------------------------------
# 2. Display Dataset
# -----------------------------------

print("Dataset:")
print(df)


# -----------------------------------
# 3. Basic Data Analysis
# -----------------------------------

print("\nFirst 5 rows:")
print(df.head())

print("\nDataset Information:")
df.info()

print("\nStatistical Summary:")
print(df.describe())

print("\nMissing Values:")
print(df.isnull().sum())


# -----------------------------------
# 4. Calculate Statistics
# -----------------------------------

print("\nAverage Marks:", df["Marks"].mean())
print("Highest Marks:", df["Marks"].max())
print("Lowest Marks:", df["Marks"].min())

student = df.loc[df["Marks"].idxmax()]

print("\nStudent with Highest Marks:")
print(student)


# -----------------------------------
# 5. Matplotlib Line Chart
# -----------------------------------

plt.figure(figsize=(8, 5))

plt.plot(
    df["Name"],
    df["Marks"],
    marker="o"
)

plt.xlabel("Student")
plt.ylabel("Marks")
plt.title("Student Marks")

plt.xticks(rotation=45)

plt.show()


# -----------------------------------
# 6. Matplotlib Bar Chart
# -----------------------------------

plt.figure(figsize=(8, 5))

plt.bar(
    df["Name"],
    df["Marks"]
)

plt.xlabel("Student")
plt.ylabel("Marks")
plt.title("Student Marks Comparison")

plt.xticks(rotation=45)

plt.show()


# -----------------------------------
# 7. Matplotlib Scatter Plot
# -----------------------------------

plt.figure(figsize=(8, 5))

plt.scatter(
    df["Study_Hours"],
    df["Marks"]
)

plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.title("Study Hours vs Marks")
    
plt.show()


# -----------------------------------
# 8. Seaborn Bar Plot
# -----------------------------------

plt.figure(figsize=(8, 5))

sns.barplot(
    data=df,
    x="Name",
    y="Marks"
)

plt.title("Student Marks using Seaborn")
plt.xticks(rotation=45)

plt.show()


# -----------------------------------
# 9. Seaborn Scatter Plot
# -----------------------------------

plt.figure(figsize=(8, 5))

sns.scatterplot(
    data=df,
    x="Study_Hours",
    y="Marks",
    s=100
)

plt.title("Study Hours vs Marks")

plt.show()


# -----------------------------------
# 10. Seaborn Regression Plot
# -----------------------------------

plt.figure(figsize=(8, 5))

sns.regplot(
    data=df,
    x="Study_Hours",
    y="Marks"
)

plt.title("Study Hours vs Marks with Regression Line")

plt.show()


# -----------------------------------
# 11. Correlation Heatmap
# -----------------------------------

correlation = df[
    ["Study_Hours", "Attendance", "Marks"]
].corr()

print("\nCorrelation:")
print(correlation)

plt.figure(figsize=(7, 5))

sns.heatmap(
    correlation,
    annot=True
)

plt.title("Correlation Heatmap")

plt.show()


# -----------------------------------
# 12. Plotly Bar Chart
# -----------------------------------

fig = px.bar(
    df,
    x="Name",
    y="Marks",
    title="Student Marks - Interactive Chart"
)

fig.show()


# -----------------------------------
# 13. Plotly Scatter Plot
# -----------------------------------

fig = px.scatter(
    df,
    x="Study_Hours",
    y="Marks",
    text="Name",
    title="Study Hours vs Marks"
)

fig.show()


# -----------------------------------
# 14. Plotly 3D Chart
# -----------------------------------

fig = px.scatter_3d(
    df,
    x="Study_Hours",
    y="Attendance",
    z="Marks",
    text="Name",
    title="Study Hours, Attendance and Marks"
)

fig.show()
