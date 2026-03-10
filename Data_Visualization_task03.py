import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data=pd.read_csv('Super Store sales/super store sales data.csv')
print(data)
print(data.columns)
print(data.shape)
print(data.dtypes)
#checking null
print(data.isnull().sum())
data['Sales']=data['Sales'].apply(lambda x:x if x>0 else 0)
num_duplicates = data.duplicated(subset=['Order ID','Product Name','Sales','Order Date'],keep=False)
print("Number of exact duplicate rows:", num_duplicates)
data.drop(columns=['Row ID','Order ID','Customer ID','Customer Name','Postal Code','Country',],inplace=True)
total_sale=data['Sales'].sum()
print('Total Revenue= ',total_sale)
product=data.groupby('Product Name')['Sales'].sum()
product = product.reset_index()
product=product.sort_values(by='Sales',ascending=False)
print(product)
category=data.groupby('Category')['Sales'].sum()
category = category.reset_index()
category=category.sort_values(by='Sales',ascending=False)
print(category)
sub_category=data.groupby('Sub-Category')['Sales'].sum()
sub_category=sub_category.reset_index()
sub_category=sub_category.sort_values(by='Sales',ascending=False)
print(sub_category)

print('Description about product=',product.shape)
print('Description about category=',category.shape)
print('Description about sub-category=',sub_category.shape)

plt.figure(figsize=(10,12))
plt.bar(category['Category'],category['Sales'],color='purple')
plt.title('Sales Vs Product')
plt.xlabel('Category of Product')
plt.ylabel('Sales')
plt.show()
plt.close()

plt.figure(figsize=(12,12))
plt.bar(sub_category['Sub-Category'],sub_category['Sales'],color='yellow')
plt.title('Sales Vs Product')
plt.xlabel('sub_Category of Product')
plt.ylabel('Sales')
plt.xticks(rotation=45, ha='right')  # Rotate labels 45° and align to right
plt.tight_layout()  # Adjust layout so labels don’t get cut off
plt.show()
plt.close()

print(data['Segment'].value_counts())

segment=data.groupby('Segment')['Sales'].sum()
segment=segment.reset_index()
segment=segment.sort_values(by='Sales', ascending=False)
print(segment)

plt.figure(figsize=(12,12))
plt.bar(segment['Segment'],segment['Sales'],color='green')
plt.xlabel('Segments')
plt.ylabel('Sales')
plt.title('Sales VS Segments')
plt.xticks(rotation=45 , ha='right')
plt.show()
plt.close()