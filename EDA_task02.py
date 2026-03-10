import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import  train_test_split
from sklearn.preprocessing import StandardScaler

data=pd.read_csv('thyroid_cancer_risk_data.csv')
print(data)
print(data.head(10))
shape=data.shape,data.columns,data.dtypes
print(shape)
print(data.isnull().sum())

#deleting the row of diagnosis as it is target column we cannot fill the numm value

print(data[data['Diagnosis'].isnull()].index)
print(data.loc[11])
data.drop(index=11,inplace=True)
print(data.isnull().sum())
meanofTSH=data['TSH_Level'].mean()
data['TSH_Level']=data['TSH_Level'].fillna(meanofTSH)
print(data['T3_Level'])
data['T3_Level']=data['T3_Level'].astype(str).str.strip()
data['T3_Level']=pd.to_numeric(data['T3_Level'],errors='coerce')
print(data['T3_Level'].dtype)
mean_T3=data['T3_Level'].mean() 
data['T3_Level']=data['T3_Level'].fillna(mean_T3)
print(data.isnull().sum())
mean_T4=data['T4_Level'].mean()
data['T4_Level']=data['T4_Level'].fillna(mean_T4) 
data.dropna(subset=['Thyroid_Cancer_Risk'],inplace=True)
print(data.isnull().sum())
nod_mean=data['Nodule_Size'].mean()
nod_median=data['Nodule_Size'].median()
print('mean=',nod_mean,'median=',nod_median)
data['Nodule_Size']=data['Nodule_Size'].fillna(nod_mean)
print(data.isnull().sum())


#now my data is cleaned and i m finding correlations
#as diagnosis column is not categorical
#converting categorical column to numeric

print(data['Diagnosis'].value_counts())
data['Diagnosis']=data['Diagnosis'].map({
    'Benign':1,
    'Malignant':0
})
print(data['Diagnosis'])
print(data.isnull().sum())

correlations_num=['Age','TSH_Level','T3_Level','T4_Level','Nodule_Size']
for i in correlations_num:
    Correlation=data[i].corr(data['Diagnosis'])
    print(i,':',Correlation)

print(data['Iodine_Deficiency'].value_counts())
print(data['Radiation_Exposure'].value_counts())
convt_cat_num=['Iodine_Deficiency','Family_History','Smoking','Obesity','Diabetes','Radiation_Exposure']
for i in convt_cat_num:
    data[i]=data[i].str.strip()


for i in convt_cat_num:
    data[i]=data[i].map({
        'Yes':1,
        'No':0
    })

data['Gender']=data['Gender'].str.strip()
data['Gender']=data['Gender'].map({
    'Male':1,
    'Female':0
})
print(data.dtypes)
print(data[['Country','Ethnicity']].value_counts())

convt_country_Eth=['Country','Ethnicity']
for i in convt_country_Eth:
    data[i]=data[i].str.strip()

convt_country_Eth=['Country','Ethnicity']

for i in  convt_country_Eth:
    dummies=pd.get_dummies(data[i],prefix=i)
    dummies=dummies.astype(int)
    data=pd.concat([data,dummies],axis=1)
    data.drop(columns=i,inplace=True)
print(data.dtypes)
print(data['Thyroid_Cancer_Risk'])
data['Thyroid_Cancer_Risk']=data['Thyroid_Cancer_Risk'].str.strip()
data['Thyroid_Cancer_Risk']=data['Thyroid_Cancer_Risk'].map({
    'Low':0,
    'Medium':1,
    'High':2
})
print(data.dtypes)

Corre=['Gender','Family_History','Radiation_Exposure','Iodine_Deficiency','Smoking','Obesity','Diabetes','Thyroid_Cancer_Risk']
for i in Corre:
 correlations=data[i].corr(data['Diagnosis']) 
 print(i,':',correlations)

cor=['Country_Brazil','Country_China','Country_Germany','Country_India','Country_Japan','Country_Nigeria','Country_Russia','Country_South Korea','Country_UK','Country_USA']
for i in cor:
 correlatio=data[i].corr(data['Diagnosis']) 
 print(i,':',correlatio)

# i m checking the skewness if thyroid cancer risk at it negatively correlate and effect is moderate  not negligible
plt.hist(data['Thyroid_Cancer_Risk'],bins=20)
plt.xlabel('Thyroid_Cancer_Risk')
plt.ylabel('Frequency')
plt.title('Histogram of Thyroid_Cancer_Risk')
plt.show()
plt.close()

print('mean of Thyroid_Cancer_Risk=',data['Thyroid_Cancer_Risk'].mean())
print('median of Thyroid_Cancer_Risk=',data['Thyroid_Cancer_Risk'].median())
print(data.head())
data.drop('Patient_ID',axis=1,inplace=True)
print(data.dtypes)
X=data.drop(columns=['Diagnosis','Thyroid_Cancer_Risk'])
y=data['Diagnosis']
X_train,X_test,y_train,y_test=train_test_split(
   X,y,
   test_size=0.2,
   random_state=42,
   stratify=y
)
num_features=['TSH_Level','T3_Level','T4_Level','Nodule_Size','Age']
scaler=StandardScaler()
X_train[num_features]=scaler.fit_transform(X_train[num_features])
X_test[num_features]=scaler.transform(X_test[num_features])
