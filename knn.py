from sklearn.neighbors import KNeighborsClassifier
x1=[7,7,3,1]
y1=[7,4,4,4]
target=['BAD',"BAD",'GOOD','GOOD']
feature1=list(zip(x1,y1)) # input
k=KNeighborsClassifier(n_neighbors=3)  #k=3 , # create an object for KNeighborsClassifier function
k.fit(feature1,target) #target data
print(k.predict([[3,7]]))