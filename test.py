class data:

    NoOfChecks=100

def SavedData(Arr,i): return [Arr[i],Arr[i+1]]

def Start(EnteredArr):
    for CheckLOOP in range(0,data.NoOfChecks):
        for itr in range(0,len(EnteredArr)-1):
            ValueSeved=SavedData(EnteredArr,itr)[0]
            NextValueSeved=SavedData(EnteredArr,itr)[1]
            if ValueSeved>NextValueSeved:
                EnteredArr[itr]=NextValueSeved
                EnteredArr[itr+1] =ValueSeved

    print(EnteredArr)

if __name__=="__main__":
    Start([8,7,5,6,2,1,5])

