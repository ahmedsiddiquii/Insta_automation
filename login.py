import pandas as pd
def login():
    df = pd.read_csv('Probate_Sample.csv')
    names = df['Username']
    print(names)
    passwords = df['Password']
    print(passwords)
def user():
    df = pd.read_csv('Probate_Sample.csv')
    search1 =df['People']
    print(search1)