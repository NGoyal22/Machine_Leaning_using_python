from sklearn import tree

#x is a list of (height,weight,shoe_size)
x=[[181,80,44],[180,77,43],[183,81,42],[184,83,40],[177,79,39],[185,90,45],[176,87,44]]
y=['male','female','male','female','male','female','male']

clf=tree.DecisionTreeClassifier()
clf=clf.fit(x,y)

prediction=clf.predict([[190,89,43]])
print(prediction)
