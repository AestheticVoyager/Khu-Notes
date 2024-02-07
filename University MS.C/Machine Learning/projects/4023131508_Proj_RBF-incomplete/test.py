from RBF import *
from dataset import y_outs,inputs
from sklearn.model_selection import train_test_split
import numpy as np

X_train, X_test, y_train, y_test = train_test_split(
        inputs, y_outs, test_size=0.4, random_state=123
    )
r=RBF(X_train,20,y_train,0.1)

r.train(50)

print(r.test(X_test,y_test))
