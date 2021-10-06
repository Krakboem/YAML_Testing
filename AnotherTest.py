import os
import pandas as pd

print("This is another test")

cwd = os.getcwd()

print("Current working directory: {0}".format(cwd))
print("os.getcwd() returns an object of type: {0}".format(type(cwd)))

df = pd.read_csv ("C:\Users\MA642GN\OneDrive - EY\Documents\Microsoft Azure\DevOps\Data Kaggle\home-credit-default-risk\application_test.csv")
print(df)
