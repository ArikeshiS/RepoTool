import argparse
# importing the module
import pandas as pd
import requests as rq
import json
# read specific columns of csv file using Pandas

def checkVersion(vargs,csvFile,depend):
    # cmd = input("Enter CMD: ")
    # df = pd.read_csv("CSVFile.csv")
    df = pd.read_csv(csvFile)
    # print(df.dropna()
    dfname = df['name'].dropna().tolist()
    dfrepo = df['repo'].dropna().tolist()
    res = dict(zip(dfname, dfrepo))
    # print(df)
    # print(res)
    print("name \t \t \t \t"+" repo \t \t \t \t \t\t\t"+"version \t \t \t"+" version_satisfied")

    for key, value in res.items():
        x = value.replace("https://github.com/","https://raw.githubusercontent.com/")
        # print(type(i))
        #print(x)
        link = x+"main/package.json"
        # print(link)
        r = rq.get(link)
        j = r.json()
        data = json.loads(r.text)
        print(data)
        # print(data.get(depend))
        # version = data['dependency'].get(depend)
        version = data['dependencies'][depend]
        idx = version.index('^')
        version = version[idx+1: ]
        # print(version)

        # if(cmd >= version):
        #     print("true")
        # else:
        #     print("false")
        if(version >= vargs):
            print(key + "\t " + value + "     \t\t" + version+" \t \t \t\t true")
        else:
            print(key + "\t " + value + "     \t\t" + version+" \t \t \t\t false")

def main():
    parser = argparse.ArgumentParser()
    # version = '1.4.2'
    parser.add_argument("-update","--update", help="display a square of a given number", action='store_true')
    parser.add_argument("-i", help="display a square of a given number", action='store_true')
    parser.add_argument("csvFile", help="csvFile")

    parser.add_argument("ver", help="version")


    args3 = parser.parse_args()
    if(args3.update):
        print("update args")
    # print(args3.csvFile, "")
    # print(args3.ver, "")
    idx = args3.ver.index('@')
    idx1 = args3.ver.rfind(' ')
    depend = args3.ver[idx1+1:idx]
    print(depend)
    vargs = args3.ver[idx+1:]
    checkVersion(vargs, args3.csvFile,depend)
    #     print("true")
    # else:
    #     print("false")
    # print(args3.ver, "")

if __name__ == "__main__":
    main()