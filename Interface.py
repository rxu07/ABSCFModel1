import WholeLoan
import WholeLoan as WL
import time
import pandas as pd

def readExcelLoantape(path):
    use = path
    df = pd.read_excel(path)

def testRun(numberofruns):
    wl = WL.WholeLoan(500000, 500000, 0.05, 675, 360)
    tic = time.perf_counter()
    for i in range(0, numberofruns):
        wl.runCF(1)
        i = i + 1
    toc = time.perf_counter()
    print(f"Ran the program in {toc - tic:0.4f} seconds")

wl = WL.WholeLoan(1000000,1000000,0.075,700,360)
#print(wl.runCF(100))
tic = time.perf_counter()
pd.options.display.max_columns = 99
list = []
for i in range (0,1000):
    df = wl.runCF(0.99)
    #print(df)
    list.append(df)
    i = i + 1
df = wl.runCF(0.99)
for i in range (0,len(list)):
    df = df.add(list[i])
    i = i +1
#print(df)
df.to_excel(r"C:\Users\rxu\OneDrive - TPG\Desktop\Project Alexandria\TEST.xlsx")
toc = time.perf_counter()
print(f"Ran the program in {toc - tic:0.4f} seconds")
#wl1 = WL.WholeLoan(500000, 500000, 0.05, 675, 360)
#print(type(wl1))
#print(wl1.RemTerm)
#print(wl1.runCF())

#testRun(1000)
