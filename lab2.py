import numpy as np
import pandas as pd
tabl=pd.DataFrame([["fruit","red",45,60,120],
["fruit","yellow",45,32,100],
["fruit","orange",60,45,50],
["fruit","orange",75,21,70],
["fruit","green",45,40,170],
["fruit","peach colour",45,35,130],
["vegetable","brown",45,30,90],
["vegetable","orange",20,16,110],
["vegetable","yellow",30,24,150],
["vegetable","green",120,80,220]],
columns=["type","collor","weight","size","price"],
index=["apple", "banana", "orange", "tangerine", "pear", "peach", "potato", "carrot", "onion", "cabbage"])

print(tabl.tail(4))
print(tabl.info())

print(tabl[(tabl["size"]  > tabl['size']['potato']) & (tabl["type"]=="fruit") ])
print(tabl[(tabl["weight"] > tabl["weight"]["banana"]) & (tabl["type"]=="fruit")]["price"].mean())

mean=0;
fruct=tabl[tabl["type"] == "fruit"]
for v,k in fruct.iterrows():
    mean+=k["price"]

mean=mean/fruct.shape[0]
print(mean)

tabl2=pd.DataFrame({"Min":tabl.min()[2:], "Max":tabl.max()[2:], "Mean":tabl.mean(), "Median":tabl.median()})
print(tabl2)
tabl3=tabl.agg([np.min, np.max,np.mean,np.median]).iloc[:,2:5]
print(tabl3)
print(tabl.groupby("collor").mean().iloc[:,[0,2]])
print(tabl.groupby("collor").max().iloc[:,[1,3]])

