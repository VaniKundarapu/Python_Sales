import pandas as pd
import os    #to get data from dir
df = pd.read_csv("C:\\Users\kundarapu vani\\Downloads\\Pandas-Data-Science-Tasks-master\\Pandas-Data-Science-Tasks-master\\SalesAnalysis\\Sales_Data\\Sales_April_2019.csv" )
df.head()
files = [file for file in os.listdir("C:\\Users\kundarapu vani\\Downloads\\Pandas-Data-Science-Tasks-master\\Pandas-Data-Science-Tasks-master\\SalesAnalysis\\Sales_Data\\")]
months_data = pd.DataFrame()
for file in files:
    df = pd.read_csv("C:\\Users\kundarapu vani\\Downloads\\Pandas-Data-Science-Tasks-master\\Pandas-Data-Science-Tasks-master\\SalesAnalysis\\Sales_Data\\" + file)
    months_data = pd.concat([months_data,df])

months_data.to_csv("total_sales_data.csv",index = False)
all_data = pd.read_csv("total_sales_data.csv")
print(all_data.head())
#q1 = what was the best month for sales? How much was earned that month
# adding month column
all_data['Month'] = all_data['Order Date'].str[0,2]       # adds month column with value
all_data['Month'] = all_data['Month'].astype('int32')           
print(all_data.head())
