from flask import Flask,request
import pandas as pd
import csv
import numpy as np
from flask_cors import CORS
import json 

app = Flask(__name__)
CORS(app)
@app.route('/post', methods=['POST'])
def post():
    result={}  
    file = request.files['file']

    df=pd.read_csv(file , delimiter=',', names=['DATE','PARTICULARS','WITHDRAWALS','DEPOSITS','BALANCE'])
    result["name"] = df.loc[df.index[0], 'DATE'] 
    result["accountNumber"] = df.loc[df.index[1], 'DATE']
    result["phoneNumber"] = df.loc[df.index[2], 'DATE']


    transactionList=[]
    temp={}
    i=0
    j=0
    for index,x in df.iloc[18:len(df.index)].iterrows():
        if(i!=0):
            temp={'date':x['DATE'],'particulars':x['PARTICULARS'],'deposits':x['DEPOSITS'],'withdrawals':x['WITHDRAWALS'],'balance':x['BALANCE']}
            transactionList.insert(j,temp)
            j=j+1
        i=i+1
    temp={}
    result["TransactionList"] = transactionList
    
    return json.dumps(result).replace("NaN", u'""')

if __name__=="__main__":
    app.run(debug=True)