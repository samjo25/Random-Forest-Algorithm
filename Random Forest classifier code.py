# -*- coding: utf-8 -*-
"""Untitled6.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1mDf5RgBS7VVrQcB65t5Lu90w2Ob_NOtJ
"""

import numpy as np
import pandas as pd
from sklearn.datasets import load_digits
digits = load_digits()

dir(digits)

# Commented out IPython magic to ensure Python compatibility.
# %matplotlib inline
import matplotlib.pyplot as plt
plt.gray()
for i in range(5):
  plt.matshow(digits.images[i])

digits.data[:4]

df = pd.DataFrame(digits.data)
df.head()

digits.target

df['target'] = digits.target
df.head()

df = df.drop(['target'],axis='columns')
df.head()

# train n test the data

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(df,digits.target,test_size=0.2)

x_train.shape, x_test.shape, y_train.shape, y_test.shape

# import Random forest classifier and fit the model...

from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier(n_estimators=30)
model.fit(x_train,y_train)

# find the accuracy score of y_test and compared with x_test...

model.score(x_test,y_test)

# find the y_predict value and the accuracy score of y_pred...

from sklearn.metrics import accuracy_score
y_pred = model.predict(x_test)
accuracy_score(y_test,y_pred)

# confusion matrix..

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test,y_pred)
cm

# classification report..

from sklearn.metrics import classification_report
print(classification_report(y_pred,y_test))

# Commented out IPython magic to ensure Python compatibility.
# plot the heatmap..

# %matplotlib inline
import matplotlib.pyplot as plt
import seaborn as sns
plt.figure(figsize=(10,9))
sns.heatmap(cm, annot=True)
plt.title('confusion_matrix', size=18)
plt.xlabel('predicted', size=16)
plt.ylabel('True', size=16)