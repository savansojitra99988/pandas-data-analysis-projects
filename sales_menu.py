import pandas as pd

data = {
    "order_id": [1001,1002,1003,1004,1005,1006,1007,1008,1009,1010,
                 1011,1012,1013,1014,1015,1016,1017,1018,1019,1020],
    "date": ["2026-01-01","2026-01-02","2026-01-03","2026-01-04","2026-01-05",
             "2026-01-06","2026-01-07","2026-01-08","2026-01-09","2026-01-10",
             "2026-01-11","2026-01-12","2026-01-13","2026-01-14","2026-01-15",
             "2026-01-16","2026-01-17","2026-01-18","2026-01-19","2026-01-20"],
    "customer": ["Amit","Neha","Ravi","Pooja","Karan","Sneha","Vikas","Anjali",
                 "Amit","Priya","Aman","Ritika","Sohan","Nisha","Arjun","Meena",
                 "Rohit","Kavya","Deepak","Simran"],
    "product": ["Laptop","Mouse","Keyboard","Monitor","Printer","Laptop","Mouse",
                "Keyboard","Monitor","Printer","Laptop","Mouse","Keyboard","Monitor",
                "Printer","Laptop","Mouse","Keyboard","Monitor","Printer"],
    "category": ["Electronics","Accessories","Accessories","Electronics","Electronics",
                 "Electronics","Accessories","Accessories","Electronics","Electronics",
                 "Electronics","Accessories","Accessories","Electronics","Electronics",
                 "Electronics","Accessories","Accessories","Electronics","Electronics"],
    "city": ["Delhi","Mumbai","Patna","Kolkata","Delhi","Mumbai","Patna","Kolkata",
             "Delhi","Mumbai","Patna","Kolkata","Delhi","Mumbai","Patna","Kolkata",
             "Delhi","Mumbai","Patna","Kolkata"],
    "quantity": [2,5,3,1,2,1,4,2,3,1,2,6,4,2,1,3,5,2,1,2],
    "price": [55000,500,1500,12000,8000,60000,550,1600,12500,8500,58000,600,1700,
              13000,9000,62000,650,1800,13500,9500],
    "discount": [5000,50,100,1000,500,4000,40,120,1500,600,4500,60,150,1200,700,
                 5500,70,180,1300,800],
    "payment_mode": ["UPI","Cash","Card","UPI","Card","Cash","UPI","Card","Cash",
                     "UPI","Card","Cash","UPI","Card","Cash","UPI","Card","Cash",
                     "UPI","Card"]
}

df = pd.DataFrame(data)
df["date"] = pd.to_datetime(df["date"])
df["sales"] = (df["price"] * df["quantity"]) - df["discount"]
df["GST"] = df["sales"] * 0.18
df["net_amt"] = df["sales"] + df["GST"]

def cat(x):
    if x > 50000:
        return "high"
    elif x > 10000:
        return "medium"
    else:
        return "low"

df["sales_cat"] = df["net_amt"].apply(cat)

def total_quantity():
    print("Total Quantity Sold =", df["quantity"].sum())

def total_sales_amount():
    print("Total Sales Amount =", (df["quantity"]*df["price"]).sum())

def avg_product_price():
    print("Average Product Price =", df["price"].mean())

def max_min_price():
    print("Max Price Product =", df.loc[df["price"].idxmax()]["product"])
    print("Min Price Product =", df.loc[df["price"].idxmin()]["product"])

def city_wise_sales():
    print(df.groupby("city")["sales"].sum().reset_index())

def category_wise_sales():
    print(df.groupby("category")["sales"].sum().reset_index())

def product_wise_quantity():
    print(df.groupby("product")["quantity"].sum().reset_index())

def payment_mode_quantity():
    print(df.groupby("payment_mode")["quantity"].sum().reset_index())

def city_max_discount():
    print(df.groupby("city")["discount"].max().reset_index())

def product_avg_discount():
    print(df.groupby("product")["discount"].mean().reset_index())

def city_order_count():
    print(df.groupby("city")["order_id"].count().reset_index())

def january_sales():
    print("January Sales =", df[df["date"].dt.month==1]["sales"].sum())

def daily_trends():
    print(df.groupby("date")["sales"].agg(["max","mean","min","sum"]).reset_index())

def weekend_orders():
    print(df[df["date"].dt.dayofweek>=5])

def first10_sales():
    print(df[df["date"].dt.day<=10].groupby(df["date"].dt.month)["sales"].sum().reset_index())

def top_customers():
    print(df.nlargest(3,"net_amt")[["customer","net_amt"]])

def most_selling_product():
    print(df.loc[df["quantity"].idxmax()])

def city_highest_sales():
    print(df.loc[df["sales"].idxmax()]["city"])

def highest_discount_product():
    print(df.loc[df["discount"].idxmax()]["product"])

def correlation_qty_price():
    print("Correlation =", df["quantity"].corr(df["price"]))

def pivot_city_category():
    print(pd.pivot_table(df, values="sales", index="city", columns="category", aggfunc="sum", fill_value=0))

def pivot_payment_product():
    print(pd.pivot_table(df, values="quantity", index="payment_mode", columns="product", aggfunc="sum", fill_value=0))

def pivot_product_sales():
    print(pd.pivot_table(df, values="sales", index="product", aggfunc="sum"))

def pivot_monthly_sales():
    print(pd.pivot_table(df, values="sales", index=df["date"].dt.month, aggfunc="sum"))

while True:
    print("\n========= Sales Analysis Menu =========")
    print("1. Total Quantity Sold")
    print("2. Total Sales Amount")
    print("3. Average Product Price")
    print("4. Max & Min Price Product")
    print("5. City-wise Sales")
    print("6. Category-wise Sales")
    print("7. Product-wise Quantity Sold")
    print("8. Payment Mode-wise Quantity")
    print("9. City-wise Max Discount")
    print("10. Product-wise Avg Discount")
    print("11. City-wise Order Count")
    print("12. January Sales")
    print("13. Daily Trends")
    print("14. Weekend Orders")
    print("15. First 10 Days Sales")
    print("16. Top 3 Customers")
    print("17. Most Selling Product")
    print("18. City with Highest Sales")
    print("19. Product with Highest Discount")
    print("20. Correlation (Quantity vs Price)")
    print("21. Pivot: City vs Category Sales")
    print("22. Pivot: Payment Mode vs Product Quantity")
    print("23. Pivot: Product-wise Sales")
    print("24. Pivot: Monthly Sales")
    print("25. Exit")

    choice = input("Enter your choice (1-25): ")

    if choice == "1":
        total_quantity()
    elif choice == "2":
        total_sales_amount()
    elif choice == "3":
        avg_product_price()
    elif choice == "4":
        max_min_price()
    elif choice == "5":
        city_wise_sales()
    elif choice == "6":
        category_wise_sales()
    elif choice == "7":
        product_wise_quantity()
    elif choice == "8":
        payment_mode_quantity()
    elif choice == "9":
        city_max_discount()
    elif choice == "10":
        product_avg_discount()
    elif choice == "11":
        city_order_count()
    elif choice == "12":
        january_sales()
    elif choice == "13":
        daily_trends()
    elif choice == "14":
        weekend_orders()
    elif choice == "15":
        first10_sales()
    elif choice == "16":
        top_customers()
    elif choice == "17":
        most_selling_product()
    elif choice == "18":
        city_highest_sales()
    elif choice == "19":
        highest_discount_product()
    elif choice == "20":
        correlation_qty_price()
    elif choice == "21":
        pivot_city_category()
    elif choice == "22":
        pivot_payment_product()
    elif choice == "23":
        pivot_product_sales()
    elif choice == "24":
        pivot_monthly_sales()
    elif choice == "25":
        print("Exiting... Thank you!")
        break
    else:
        print("Invalid choice, please try again.")
