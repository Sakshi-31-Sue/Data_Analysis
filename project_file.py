import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Dataset
df = pd.read_csv(
    "data/Diwali Sales Data.csv",
    encoding="unicode_escape"
)

# Data Cleaning
df.drop(columns=["Status", "unnamed1"], inplace=True)
df.dropna(inplace=True)
df["Amount"] = df["Amount"].astype(int)
print("Dataset Shape:", df.shape)

# Create Plot Folder
import os
if not os.path.exists("plots"):
    os.makedirs("plots")

# Gender Analysis
gender_sales = (
    df.groupby("Gender", as_index=False)["Amount"].sum().sort_values(by="Amount", ascending=False))

plt.figure(figsize=(6, 4))
sns.barplot(data=gender_sales, x="Gender", y="Amount")
plt.title("Total Sales by Gender")
plt.xlabel("Gender")
plt.ylabel("Sales Amount")
plt.savefig("plots/gender_sales.png")
plt.show()

# Age Group Analysis
age_sales = (df.groupby("Age Group", as_index=False)["Amount"].sum().sort_values(by="Amount", ascending=False))

plt.figure(figsize=(8, 5))
sns.barplot(data=age_sales, x="Age Group", y="Amount")
plt.title("Sales by Age Group")
plt.xlabel("Age Group")
plt.ylabel("Sales Amount")
plt.savefig("plots/age_group_sales.png")
plt.show()

# State Analysis
state_sales = (df.groupby("State", as_index=False)["Amount"].sum().sort_values(by="Amount", ascending=False).head(10)
)

plt.figure(figsize=(12, 5))
sns.barplot(data=state_sales, x="State", y="Amount")
plt.title("Top 10 States by Sales")
plt.xlabel("State")
plt.ylabel("Sales Amount")
plt.xticks(rotation=45)
plt.savefig("plots/top_states_sales.png")
plt.show()

# Occupation Analysis
occupation_sales = (df.groupby("Occupation", as_index=False)["Amount"].sum().sort_values(by="Amount", ascending=False))

plt.figure(figsize=(12, 5))
sns.barplot(data=occupation_sales, x="Occupation", y="Amount")
plt.title("Sales by Occupation")
plt.xlabel("Occupation")
plt.ylabel("Sales Amount")
plt.xticks(rotation=45)
plt.savefig("plots/occupation_sales.png")
plt.show()

# Product Category Analysis

category_sales = (df.groupby("Product_Category", as_index=False)["Amount"].sum().sort_values(by="Amount", ascending=False)
    .head(10)
)

plt.figure(figsize=(12, 5))
sns.barplot(data=category_sales,
            x="Product_Category",
            y="Amount")
plt.title("Top Product Categories by Sales")
plt.xlabel("Product Category")
plt.ylabel("Sales Amount")
plt.xticks(rotation=45)
plt.savefig("plots/product_category_sales.png")
plt.show()

# Top Selling Products

top_products = (df.groupby("Product_ID", as_index=False)["Orders"].sum().sort_values(by="Orders", ascending=False)
    .head(10)
)

plt.figure(figsize=(12, 5))
sns.barplot(data=top_products,
            x="Product_ID",
            y="Orders")
plt.title("Top 10 Products by Orders")
plt.xlabel("Product ID")
plt.ylabel("Orders")
plt.xticks(rotation=45)
plt.savefig("plots/top_products.png")
plt.show()

# Business Insights

print("\nKEY INSIGHTS")
print("- Female customers generated higher sales.")
print("- Age group 26-35 contributed significantly.")
print("- Certain states generated maximum revenue.")
print("- Some occupations showed higher purchasing power.")
print("- Food, Clothing and Electronics categories were among top performers.")