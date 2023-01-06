# importing the module
import pandas as pd
import requests as rq
import json
# read specific columns of csv file using Pandas
def checkVersion():
    cmd = input("Enter CMD: ")
    df = pd.read_csv("CSVFile.csv", usecols=['repo'])
    df = df['repo'].tolist()
    print(df)
    for i in df:
        x = i.replace("https://github.com/","https://raw.githubusercontent.com/")
        print(type(i))
        print(type(x))
        link = x+"main/package.json"
        print(link)
        r = rq.get(link)
        data = json.loads(r.text)
        print(data)
        print(data.get('version'))
        version = data.get('version')
        if(cmd >= version):
            print("true")
        else:
            print("false")


if __name__ == "__main__":
    checkVersion()