import pandas as pd
import sys
def stay_or_go_lower(salary,tablenr=32,colnr=1):
    col = "column"+str(colnr)
    df = pd.read_csv("skattetabell.csv",sep=";")
    today_query = "salary_from <={} and salary_to >={} and tablenr=={}".format(salary,salary,tablenr)
    target_index = df.query(today_query).index[0]
    
    curr, prev = df.loc[target_index], df.loc[target_index-1]
    diff = (salary - curr[col]) - (prev["salary_to"]-prev[col])
    print("current",curr)
    print("below",prev)
    if diff >= 0:
        print("Stay on pay")
        max_sal = salary
    else:
        print("Go low!")
        max_sal = prev["salary_to"]
    print("Difference is {}, max salary is {}".format(abs(diff), max_sal))


args = list(map(int,sys.argv[1:]))
if len(args)==1 :
    stay_or_go_lower(args[0])
if len(args)==2 :
    stay_or_go_lower(args[0],args[1])   
if len(args)==3:
    stay_or_go_lower(args[0],args[1],args[2])      


