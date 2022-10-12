
import numpy as np
import pandas as pd
import streamlit as st
from sklearn.linear_model import LinearRegression
st.title("LINEAR REGRESSION MODEL")
X = np.array([[1, 1], [1, 2], [2, 2], [2, 3],[3,4]])
# y = 1 * x_0 + 2 * x_1 + 3
y = np.dot(X, np.array([1, 2])) + 3
reg = LinearRegression().fit(X, y)
reg.score(X, y)
reg.coef_
reg.intercept_

inx=st.slider("X",min_value=0,max_value=10,value=2,step=1)
iny=st.slider("y",min_value=0,max_value=10,value=2,step=1)
if(st.button('compute')):
  op=reg.predict(np.array([[inx, iny]]))[0]

  st.write("your predictedue o/p val is:",op)






