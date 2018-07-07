import numpy as np
from sklearn.svm import SVR
import csv
import matplotlib.pyplot as plt

dates=[]
prices=[]
def get_data(filename):
    with open(filename,'r') as csvfile:
      csvfr=csv.reader(csvfile)
      next(csvfr)
      for row in csvfr:
          dates.append(int(row[0].split('-')[0]))
          prices.append(float(row[1]))
    return
get_data(filename)

def predict_prices(dates,prices,x):
    dates = np.reshape(dates,(len(dates),1))
    
    svr_len = SVR(kernel='linear',C=1e3)
    svr_poly = SVR(kernel='poly',C=1e3,degree=2)
    svr_rbf = SVR(kernel='rbf',C=1e3,gamma=0.1)
    
    svr_len.fit(dates,prices)
    svr_rbf.fit(dates,prices)
    svr_poly.fit(dates,prices)
    
    plt.scatter(dates,prices,color='black',label='Data')
    plt.plot(dates,svr_len.predict(dates),color='green',label='linear model')
    plt.plot(dates,svr_poly.predict(dates),color='blue',label='poly model')
    plt.plot(dates,svr_rbf.predict(dates),color='red',label='rbf model')
    plt.xlabel('Dates')
    plt.ylabel('Prices')
    plt.title('Support Vector Machine')
    plt.legend()
    plt.show()
    
    return svr_rbf.predict(x)[0],svr_poly.predict(x)[0],svr_len.predict(x)[0]
predict_price = predict_prices(dates,prices,x)
print(predict_price)
