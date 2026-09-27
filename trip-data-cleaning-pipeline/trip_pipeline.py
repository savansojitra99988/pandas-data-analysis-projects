import pandas as pd
import sqlalchemy as sqal

conn=sqal.create_engine(
    "mysql+pymysql://root:@localhost/trip"
)

df=pd.read_sql("select * from trip",conn)
print(df.head())


print("=======================Normalize Email================================")
df['email']=df['email'].str.lower()
df['email']=df['email'].str.strip()
print(df.head())


print("=======================Clean names================================")
df['name']=df['name'].str.replace('[^a-zA-Z]','',regex=True)
print(df)


print("=======================Drop Duplicates================================")
print(df.drop_duplicates(subset=['name']).reset_index())


print("=======================Converting Age to Numeric and its operations================================")
def con(age):
    if(age>51):
        return "Senior"
    elif age>31:
       return "adult"
    else:
     return "teen"
    
df['age']=pd.to_numeric(df['age'],errors='coerce')
df['age_group']=df["age"].apply(con)
df['rank']=df['age'].rank(method='dense',ascending=False)
df['cumsum']=df['age'].cumsum()
print(df.head(10))


print("=======================Grouping & Aggregation================================")
print(df.groupby('gender')['age'].mean().reset_index())
print(df.groupby('name')['sno'].count().reset_index())


print("=======================Pivot Table================================")
print(pd.pivot_table(df,values='age',index='gender',columns='age_group',aggfunc="mean"))


print("=======================Export to Excel================================")
df.to_excel("cleaned_trip.xlsx", index=False)
print("Data exported successfully to cleaned_trip.xlsx")


print("=======================Post Data Back to SQL================================")

df.to_sql(
    name='trip_cleaned',  
    con=conn,              
    if_exists='replace',   
    index=False            
)

print("Data posted successfully into SQL table 'trip_cleaned'")
