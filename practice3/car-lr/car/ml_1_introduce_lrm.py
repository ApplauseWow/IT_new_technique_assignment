
# coding: utf-8

# In[43]:


#多元线性回归
import pandas as pd
import matplotlib.pyplot as plt
columns = ["mpg", "cylinders", "displacement", "horsepower", "weight", "acceleration", "model year", "origin", "car name"]
cars = pd.read_table("auto-mpg.data", delim_whitespace=True, names=columns)
print(cars.head(5))
print(type(cars['mpg']))


# In[44]:


#feature_cols=["cylinders", "displacement", "horsepower", "weight", "acceleration", "model year", "origin"]
feature_cols=["cylinders", "displacement", "weight", "acceleration"]
xdata=cars[feature_cols]
xdata['cylinders']=xdata['cylinders'].astype('float64')
xdata['displacement']=xdata['displacement'].astype('float64')
xdata['weight']=xdata['weight'].astype('float64')
xdata['acceleration']=xdata['acceleration'].astype('float64')

ydata=cars["mpg"]
print(xdata.head())
print(ydata.head())


# In[45]:


##构造训练集和测试集  
from sklearn.cross_validation import train_test_split  #这里是引用了交叉验证  
X_train,X_test, y_train, y_test = train_test_split(xdata, ydata, random_state=1)
print(X_train.shape)  
print(y_train.shape)  
print(X_test.shape)  
print(y_test.shape) 


# In[46]:


from sklearn.linear_model import LinearRegression  
linreg = LinearRegression()  
model=linreg.fit(X_train, y_train)  
print(model)  
print(linreg.intercept_)  
print(linreg.coef_) 


# In[47]:


zip(feature_cols, linreg.coef_)  


# In[48]:


y_pred = linreg.predict(X_test)  
print(y_pred)


# In[49]:


from sklearn import metrics  
import numpy as np  
sum_mean=0  
for i in range(len(y_pred)):  
    sum_mean+=(y_pred[i]-y_test.values[i])**2  
sum_erro=np.sqrt(sum_mean/50)  
# calculate RMSE by hand  
print("RMSE by hand:",sum_erro )


# In[50]:


import matplotlib.pyplot as plt  
plt.figure()  
plt.plot(range(len(y_pred)),y_pred,'b',label="predict")  
plt.plot(range(len(y_pred)),y_test,'r',label="test")  
plt.legend(loc="upper right") #显示图中的标签  
plt.xlabel("the factors")  
plt.ylabel('mpg')  
plt.show()  

