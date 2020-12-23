import pandas as pd
from matplotlib import pyplot as mb 
df = pd.read_csv('Iris_1.csv')
x= df['Species']
y= df['SepalLengthCm']
#Line graph of Species and Sepal Length
mb.subplot(2,2,1)
mb.plot(x,y)
#Bar graph of Species and Sepal Length
mb.subplot(2,2,2)
mb.bar(x,y)
#Scatter graph of Species and Sepal Length
mb.subplot(2,2,3)
mb.scatter(x,y)


#x1 = df['Species']
#y1 = df['SepalWidthCm']
#Line graph of Species and Sepal Width
#mb.subplot(2,2,1)
#mb.plot(x1,y1)
#Bar graph of Species and Sepal Width
#mb.subplot(2,2,2)
#mb.bar(x1,y1)
#Scatter graph of Species and Sepal Width
#mb.subplot(2,2,3)
#mb.scatter(x1,y1)


#x2 = df['Species']
#y2 = df['PetalLengthCm']
#Line graph of Species and Petal Length
#mb.subplot(2,2,1)
#mb.plot(x2,y2)
#Bar graph of Species and Petal Length
#mb.subplot(2,2,2)
#mb.bar(x2,y2)
#Scatter graph of Species and Petal Length
#mb.subplot(2,2,3)
#mb.scatter(x2,y2)



#x3 = df['Species']
#y3 = df['PetalWidthCm']
#Line graph of Species and Petal Width
#mb.subplot(2,2,1)
#mb.plot(x3,y3)
#Bar graph of Species and Petal Width
#mb.subplot(2,2,2)
#mb.plot(x3,y3)
#Scatter graph of Species and Petal Width
#mb.subplot(2,2,3)
#mb.plot(x3,y3)
