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
print(df)

print("Total Quantity Sold =" ,df["quantity"].sum())
df["sales"]=(df["price"]*df["quantity"])-df["discount"]
print(df)


print("Total Sales Amount =" ,(df['quantity']*df['price']).sum())


print("Avg Product Price =",df['price'].mean())


x=df.loc[df["price"].idxmax()]
print("Product with MAX price =",x['product'],'(',x['price'],')')

min_pro=df.loc[df["price"].idxmin()]
print("Product with MIN price =",min_pro['product'],'(',min_pro['price'],')')

print("Total Discount given=",df["discount"].sum())

print("Total number of Unique customer =",df['customer'].nunique()) 

print("Total Order Placed =",df["order_id"].count())

cwo=df.groupby("category")["order_id"].count()
print("Total Order Placed in Electronics catrgory =",cwo["Electronics"])
print()
print("-----------------------Data for DELHI city only ------------------------")

print(df[df["city"]=="Delhi"])

print()
print("-----------------------Data With Quantity > 3 ------------------------")
print(df[df["quantity"]>3])




print()
print("-----------------------Product  With price > 10,000 ------------------------")
p10=df[df["price"]>10000]
print(p10[["product","price"]].reset_index())

print()
print("-----------------------Product  With Payment mode = UPI ------------------------")
upi=df[df["payment_mode"]=="UPI"]
print(upi[["product","payment_mode"]])

print()
print("----------------------- ALL Order of laptop------------------------")
print(df[df["product"]=="Laptop"])

print()
print("-----------------Display Record For the Mumbai city with payment mode=Cash--------------------")
mcity=df[df["city"]=="Mumbai"]
print(mcity[mcity["payment_mode"]=="Cash"])


print()
print("----------------------- Records for Accessories Category ------------------------")
print(df[df["category"] == "Accessories"])

print()
print("----------------------- Records where Quantity is between 2 and 5 ------------------------")
print(df[(df["quantity"] >= 2) & (df["quantity"] <= 5)])

print()
print("----------------------- Total Orders for Printer ------------------------")
pcount=df[df["product"] == "Printer"]
print("Total Printer Orders =",pcount["product"].count())



print()
print("----------------------- Sort price in ascending order ------------------------")
print(df.sort_values('price'))

print()
print("----------------------- Sort quantity in descending order ------------------------")
print(df.sort_values('quantity',ascending=False))

print()
print("----------------------- TOP 5 recoerd as per Discount ------------------------")
# print(df.sort_values('discount',ascending=False).head(5))
print(df.nlargest(5,'discount'))


print()
print("----------------------- TOP 3 recoerd as per sales ------------------------")
print(df.nlargest(3,'sales'))


print()
print("----------------------- sort customer name Alphabatically ------------------------")
print(df.sort_values('customer'))


print()
print("----------------------- City-wise Total Sales ------------------------")
print(df.groupby("city")["sales"].sum().reset_index())

print()
print("----------------------- category wise Total Sales ------------------------")
print(df.groupby("category")["price"].mean().reset_index())

print()
print("----------------------- Product wise Total quantity sold ------------------------")
print(df.groupby("product")["quantity"].sum().reset_index())

print()
print("----------------------- Product wise Total quantity sold ------------------------")
print(df.groupby("payment_mode")["quantity"].sum().reset_index())

print()
print("----------------------- City  wise max Discount ------------------------")
print(df.groupby("city")["discount"].max().reset_index())


print()
print("----------------------- Product  wise Avg Discount ------------------------")
print(df.groupby("product")["discount"].mean().reset_index())


print()
print("----------------------- City  wise Order count ------------------------")
print(df.groupby("city")["order_id"].count().reset_index())

print()
print("-----------------------Add GST(18%)  column------------------------")
df["GST"]=(df["sales"]*0.18)

print(df)


print()
print("-----------------------Add Netamont column------------------------")
df["net_amt"]=(df["sales"]*0.18)+df["sales"]
print(df)

print()
print("-----------------------Add sales category column ------------------------")
def cat(x):
    if x>50000:
        return "high"
    elif x>10000:
        return "medium"
    else:
        return "low"

df["sales_cat"]=df["net_amt"].apply(cat)                    
print(df)


print()
print("-----------------------Find total sales for january ------------------------")
df["date"]=pd.to_datetime(df['date'])
jan_sale=df[df['date'].dt.month==1]
print(jan_sale)
print("Find total sales for january=",jan_sale["sales"].sum())


print()
print("-----------------------Find Daily Trends-----------------------")

df1=df.groupby('date')["sales"].agg(["max","mean","min","sum"]).reset_index()


print("Daily Trends=\n",df1)



print()
print("--------------------Find day with max sales-----------------------")



print("Day with MAX sale is=\n",df.nlargest(1,'sales')[["date",'sales']].reset_index())


print()
print("--------------------Find all weekend Order-----------------------")

weekend=df[df['date'].dt.dayofweek>=5]

print("all weekend Order =\n",weekend)






print()
print("--------------------Calculate sales  of first 10 days-----------------------")


first10 = df[df["date"].dt.day <= 10]
monthly_first10_sales = first10.groupby(df["date"].dt.month)["sales"].sum().reset_index()
print(monthly_first10_sales)


print()
print("--------------------Top 3 customer by purchase amt-----------------------")

print(df.nlargest(3,"net_amt"))


print()
print("--------------------Find most selling Product-----------------------")

bestpro=df.loc[df["quantity"].idxmax()]
print(bestpro.reset_index())


print()
print("--------------------City with the highest Sales recorded-----------------------")

bestcity=df.loc[df["sales"].idxmax()]
print(bestcity['city'])



print()
print("--------------------Product received the highest discount-----------------------")

bestdis=(df["discount"].idxmax())
print(bestcity['product'])


print()
print("-------------------- Correlation between Quantity & Price -----------------------")

correlation = df["quantity"].corr(df["price"])
print("Correlation =", correlation)


print()
print("-------------------- Create City vs Category sales pivot table   -----------------------")


p1=pd.pivot_table(df,values="sales",index="city",columns="category",aggfunc=["sum"]).reset_index
print(p1)

print()
print("-------------------- Create payment mode vs product quantity pivot table   -----------------------")
np=pd.pivot_table(df,values="quantity",index="payment_mode",columns="product",aggfunc="sum")
print(np)
 

print()
print("-------------------- Create product wise total sales pivot table    -----------------------")
p2=pd.pivot_table(df,values="sales",index="product",aggfunc=["sum"])
print(p2)


print()
print("-------------------- Create monthly sales pivot table    -----------------------")
p3=pd.pivot_table(df,values="sales",index=df["date"].dt.month,aggfunc=["sum"]).reset_index()
print(p3)



