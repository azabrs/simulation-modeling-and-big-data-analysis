import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import math
from heapq import nlargest
#4 зависимости: кубическая парабола, корень квадратный, логарифм и сигмоид
plt.plot(np.arange(-2,2,0.1), np.arange(-2,2,0.1)**(3),color='green', marker='o', linestyle='solid', linewidth=2, markersize=4, label='x**3')
plt.plot(np.arange(-2,2,0.1), np.sqrt(np.arange(-2,2,0.1)),color='red', marker='x', linestyle='dotted', linewidth=2, markersize=4, label='sqrt(x)')
plt.plot(np.arange(0.1,2,0.1), np.log(np.arange(0.1,2,0.1)),color='yellow', linestyle='solid', linewidth=1, label='log(x)')
x=1/((np.array(list(map(lambda x:np.exp(-x),np.arange(-5,5,0.1)))))+1)
plt.plot(np.arange(-5,5,0.1),x,color='blue', linestyle='dashed', linewidth=2, label='sigm(x)')
plt.title('line')
plt.xlabel('x')
plt.ylabel('y')
#таблица, состоящая из 50 колонок и 1000 строк с нормальным распределением в каждой колонке
df = pd.DataFrame(data=np.array([np.random.normal(loc = (i-1),scale=(1 + i/25),size=1000) for i in range(50)]).T, columns=['Var'+str(i) for i in range(50)])
print(df)
#медианы и стандартные отклонения для всех колонок
dct=pd.DataFrame({'mean': [df['Var' + str(i)].mean() for i in range(50)] ,'std':[df['Var' + str(i)].std() for i in range(50)]})
plt.figure(figsize=(10,10))
#2 отдельных точечных графика в одном окне: один для медиан, второй для стандартных отклонений.
plt.scatter(np.arange(50),dct['std'],s=20, c='red', alpha=0.7)
plt.scatter(np.arange(50),dct['mean'],s=10, c='green', alpha=1)
plt.title("scatter plot")
plt.xlabel("number line")
plt.ylabel("value line")
print(dct)

#boxplot для любых 10 колонок
plt.figure(figsize=(10,10))
df.boxplot(column = list(df.columns[0:10]))

# таблицу, состоящую из 1000 колонок и 1000 строк, c равномерным распределением в интервале от 0 до 1
df = pd.DataFrame(data=np.array([np.random.uniform(low = 0,high=1,size=1000) for i in range(1000)]).T, columns=['Var'+str(i) for i in range(1000)])
print(df.info)
#попарная корреляция Пирсона всех колонок
td=df.corr()

max_col = dict()

#определение 4 пар колонок, имеющих наибольшую попарную корреляцию
for col, ser in td.iteritems(): 
    ser.loc[ser.name]=-1;
    maxi=np.argmax(ser.values)
    maxv=np.max(ser.values)
    max_col[ser.name] = [maxi,maxv]
finish=sorted(max_col.items(),key=lambda x : x[1][1],reverse=True)[:8:2]
print(finish)

plt.figure(figsize=(10,10))
print(df)
#линейные графики этих пар в одном окне
plt.title('corr')
plt.plot(sorted(df[finish[0][0]]),sorted(df['Var' + str(finish[0][1][0])]),color='red')
plt.plot(sorted(df[finish[1][0]]),sorted(df['Var' + str(finish[1][1][0])]),color='blue')
plt.plot(sorted(df[finish[2][0]]),sorted(df['Var' + str(finish[2][1][0])]),color='green')
plt.plot(sorted(df[finish[3][0]]),sorted(df['Var' + str(finish[3][1][0])]),color='black')
plt.show()