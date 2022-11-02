import pandas as pd
class WholeLoan:
    OrigBal:int = 500000
    CurrBal: int = 500000
    Coupon = 10
    OrigFICO = 700
    CurrFICO = 725
    OrigTerm = 360
    RemTerm = 360
    CDR = 10
    Severity = 50
    CPR = 10



    def __init__(self):
        ...

    def runCF(self):
        labels = ['Beginning Balance', 'Ending Balance']
        CF = pd.DataFrame(index=labels)
        for i in range(WholeLoan.RemTerm-1):
            if i == 0:
                #print('Got here')
                beginning_balance = ''
                ending_balance:int = WholeLoan.CurrBal
            else:
                #print('Got here 2')
                beginning_balance:int = CF['Ending Balance'][i-1]

                ending_balance:int = CF['Beginning Balance'][i]
                print(type(ending_balance))
            new_row = pd.DataFrame({'Beginning Balance': beginning_balance,'Ending Balance': ending_balance}, index=[0])
            CF = pd.concat([new_row, CF.loc[:]]).reset_index(drop=True)
        return CF


print(WholeLoan().runCF())
