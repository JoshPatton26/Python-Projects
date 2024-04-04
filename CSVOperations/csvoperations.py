# ||||===========           Read info from CSV file. Perform several tasks            ===========||||
# ||||=====  Data gathered from https://catalog.data.gov/dataset?q=&sort=views_recent+desc  =====||||
from numpy import ravel
import array as ar
import pandas
import collections

def crimeByDivision(df):
    divs = collections.Counter()
    # dvs = list((lambda x: int(x), [df['AREA']]))

    for i in range(len(df)):
        divs[df['AREA'][i]] += 1

    print("\nDiv | # Crimes Rptd")
    # for div in divs.most_common(21):
    #     print("\n", *div, sep=', ')

    for unique, val in divs.items():
        print("\n", unique, ":\t(", val, "results )")

    val = int(input("Enter the number of the data you would like to use (1-21): "))



def mostCommonCrime(df):
    uniques = collections.Counter()
    num = int(input("\nEnter the number you wanna search (ex. Enter 5 for top 5 most common crimes): "))

    for i in range(len(df)):
        uniques[df['Crm Cd Desc'][i]] += 1
        
    j = 1
    for mc in uniques.most_common(num):
        print("\n", j,":", mc)
        j +=1

def crimeByType(df):
    uniques = collections.Counter()
    for i in range(len(df)):
        uniques[df['Crm Cd Desc'][i]] += 1

    for unique, val in uniques.items():
        print("\n", unique, " : ", val)


def getMaxObesity(df):
    mx = df['Obesity'][0]
    for i in range(len(df)):
        if(i == 0):
            mx = df['Obesity'][i]
        elif(i == 51):
            continue
        elif(df['Obesity'][i]) > mx:
            mx = df['Obesity'][i]
            mxst = df['NAME'][i]
    print("\n",mxst, "has the hightest obesity index with a rating of", mx)


def getMinObesity(df):
    mx = df['Obesity'][0]
    for i in range(len(df)):
        if(i == 0):
            mx = df['Obesity'][i]
        elif(i == 51):
            continue
        elif(df['Obesity'][i]) < mx:
            mx = df['Obesity'][i]
            mxst = df['NAME'][i]
    print("\n",mxst, "has the lowest obesity index with a rating of", mx)


def obesityByState(df):
    state = input("\nEnter the name of the State you wanna search: ")
    for i in range(len(df)):
        if state == df['NAME'][i]:
            print("\n", df['FID'][i], df['NAME'][i], df['Obesity'][i], df['SHAPE_Length'][i],df['SHAPE_Area'][i])


def mostCommonMegaBall(df):
    mstcmn = collections.Counter()

    for i in range(len(df)):
        mstcmn[df['Mega Ball'][i]] += 1
    
    shit = ravel(mstcmn.most_common(1))

    print("\nThe number", shit[0], "appeared", shit[1], "times since January 1st, 2002 : 12:00:00AM(EST)")

def mostCommonLotNums(df):
    mstcmn = collections.Counter()

    for i in range(len(df)):
        mstcmn[df['Winning Numbers'][i]] += 1
    
    print("\nThere are none...")


def megaBallRecords(df):
    mstcmn = collections.Counter()

    for i in range(len(df)):
        mstcmn[df['Mega Ball'][i]] += 1
    
    for mc, num in mstcmn.items():
        print("\nThe number", mc, "appeared",num, "times since January 1st, 2002 : 12:00:00AM(EST)")


def menu():
    print("\n||||==========  Welcome to Josh's data farm  ==========||||")
    inp = int(input("1: Lottery Data \n2: Crime Data \n3: Obesity Data \n\nTo exit enter -1 \n\nEnter the number of the dataset you would like to use: "))
    if inp != -1:
        if(inp == 1):
            df = pandas.read_csv('CSVFiles\WinningLotteryNumbersSince2002.csv')
            val = int(input("1: Most Common Mega Ball number \n2: Mega Ball number count since 2002 \n2: Most common winning lottery numbers \n\nTo exit enter -1 \n\nEnter the number of the data you would like to use: "))
            if(val == 1):
                mostCommonMegaBall(df)
            elif(val == 2):
                megaBallRecords(df)
            elif(val == 3):
                mostCommonLotNums(df)
            elif(val == -1):
                exit()
        elif(inp == 2):
            df = pandas.read_csv('CSVFiles\CrimeDataSince2020.csv')
            val = int(input("1: Look up crime by division \n2: Look up crime by crime type \n3: Most common crimes \n\nTo exit enter -1 \n\nEnter the number of the data you would like to use: "))
            if(val == 1):
                crimeByDivision(df)
            elif(val == 2):
                crimeByType(df)
            elif(val == 3):
                mostCommonCrime(df)
            elif(val == -1):
                exit()
        elif(inp == 3):
            df = pandas.read_csv('CSVFiles\ObesityByState.csv')
            val = int(input("1: Look up data by State \n2: State with highest obesity rate \n3: State with the lowest obesity rate \n\nTo exit enter -1 \n\nEnter the number of the data you would like to use: "))
            if(val == 1):
                obesityByState(df)
            elif(val == 2):
                getMaxObesity(df)
            elif(val == 3):
                getMinObesity(df)
            elif(val == -1):
                exit()
    else:
        return -1

if __name__=="__main__":
    val = 0
    while val != -1:
        val = menu()