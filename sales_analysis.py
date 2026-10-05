+import pandas as pd
import matplotlib.pyplot as plt

# Sales data
data = {
    "Order_ID": [1001,1002,1003,1004,1005,1006,1007,1008,1009,1010,1011,1012],
    "Date": ["2026-01-05","2026-01-12","2026-01-20","2026-02-03","2026-02-15","2026-02-22",
             "2026-03-04","2026-03-11","2026-03-19","2026-04-02","2026-04-15","2026-04-27"],
    "Product": ["Laptop","Phone","Tablet","Laptop","Phone","Laptop",
                "Tablet","Phone","Laptop","Tablet","Phone","Laptop"],
    "Region": ["North","South","North","West","South","North",
               "West","North","South","West","North","West"],
    "Units": [2,5,3,1,4,3,6,5,2,4,6,3],
    "Sales": [2400,4000,1500,1200,3800,3600,3000,4250,2500,2200,5100,3900]
}

sales_df = pd.DataFrame(data)

# Convert Date to datetime
sales_df["Date"] = pd.to_datetime(sales_df["Date"])

# Create Month column
sales_df["Month"] = sales_df["Date"].dt.month

# Create Sales Per Unit
sales_df["Sales_Per_Unit"] = sales_df["Sales"] / sales_df["Units"]

# KPIs
total_sales = sales_df["Sales"].sum()
total_units = sales_df["Units"].sum()
average_sale = sales_df["Sales"].mean()
average_units = sales_df["Units"].mean()

print("Total Sales:", total_sales)
print("Total Units:", total_units)
print("Average Sale Per Order:", round(average_sale, 2))
print("Average Units Per Order:", round(average_units, 2))

# Sales by Product
product_sales = sales_df.groupby("Product")["Sales"].sum()
print("\nSales by Product:")
print(product_sales)

# Units by Product
product_units = sales_df.groupby("Product")["Units"].sum()
print("\nUnits by Product:")
print(product_units)

# Sales by Region
region_sales = sales_df.groupby("Region")["Sales"].sum()
print("\nSales by Region:")
print(region_sales)

# Sales by Month
monthly_sales = sales_df.groupby("Month")["Sales"].sum()
print("\nSales by Month:")
print(monthly_sales)

# Average Sales Per Unit by Product
product_avg = sales_df.groupby("Product")["Sales_Per_Unit"].mean()
print("\nAverage Sales Per Unit:")
print(product_avg)

# Chart 1: Total Sales by Product
product_sales.plot(kind="bar")
plt.title("Total Sales by Product")
plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.show()

# Chart 2: Total Sales by Region
region_sales.plot(kind="bar")
plt.title("Total Sales by Region")
plt.xlabel("Region")
plt.ylabel("Total Sales")
plt.show()

# Chart 3: Total Sales by Month
monthly_sales.plot(kind="bar")
plt.title("Total Sales by Month")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.show()

# Chart 4: Average Sales Per Unit by Product
product_avg.plot(kind="bar")
plt.title("Average Sales Per Unit by Product")
plt.xlabel("Product")
plt.ylabel("Average Sales Per Unit")
plt.show()ss
