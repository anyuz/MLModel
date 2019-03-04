# import pandas as pd
# #import matplotlib.pyplot as plt
# import sklearn

# from sklearn.model_selection import train_test_split
# from sklearn.neighbors import KNeighborsClassifier
import pytest
import pymongo
def f():
    raise SystemExit(1)
def test_mytest():
    with pytest.raises(SystemExit):
        f()
# # loading data 
# data = pd.read_csv('iris.csv')
# # changing the column names for convenience
# data.columns = list(map(str.lower, data.columns.values.tolist()))
# X_train, X_test, Y_train, Y_test = train_test_split(
#         data.loc[:, ['petal_length','petal_width']], data.loc[:, 'species'])

# knn = KNeighborsClassifier(n_neighbors=2, p=2, metric='minkowski')
# knn.fit(X_train, Y_train)
# # write training accuracy and test accuracy to file
# file = open("trainingresults.txt","w") 
# file.write("Training Accuracy {}".format(knn.score(X_train, Y_train)))
# file.write("Testing Accuracy {}".format(knn.score(X_test, Y_test)))

# read mongodb accuracy
client = pymongo.MongoClient("mongodb://readonlyuser:m5MgB3iD4T0SeltE@cluster0-shard-00-00-xsyvp.mongodb.net:27017,cluster0-shard-00-01-xsyvp.mongodb.net:27017,cluster0-shard-00-02-xsyvp.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true")
db = client["myNewdatabase"]
mycol = db['accuracy']
accuracy = mycol.find({})
accuracydata = []
for x in accuracy:
    accuracydata.append(x['accuracy'])

# test RMSE accuracy < bar value if yes publish docker image
def test_answer():
    assert accuracydata[-1]<= 4
