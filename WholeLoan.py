import numpy as np
import numpy_financial as npf
import pandas as pd
import datetime as dt

class WholeLoan:
    OrigBal:int = 1000000
    CurrBal:int = 1000000
    Coupon = 0.075
    OrigLTV = 0.5
    CurrLTV = 0.5
    OrigFICO = 700
    CurrFICO = 725
    OrigTerm = 360
    RemTerm:int = 360
    CDR = 0.10 #Lay out framework in excel #Warehouse and cost of financing
    Severity = 0.4
    CPR = 0.08
    ServicingFee = 0.05
    SettleDate = dt.date(2022,11,1)
    def __init__(self, OrigBal=0, CurrBal=0, Coupon=0, OrigFICO=0, RemTerm=0 ):
        self.OrigBal = OrigBal
        self.CurrBal = CurrBal
        self.Coupon = Coupon
        self.OrigFICO = OrigFICO
        self.RemTerm = RemTerm + 1
        ...

    #def getCDR(self):

    #def getCPR(self):

    #def getSeverity(self):

    def runCF(self, Price=0):
        #Create CF table to keep track of CFs
        principal_remaining = np.zeros(self.RemTerm)
        interest_pay_arr = np.zeros(self.RemTerm)
        principal_pay_arr = np.zeros(self.RemTerm)
        recovery_amt = np.zeros(self.RemTerm)
        default_amt = np.zeros(self.RemTerm)
        prepay_amt = np.zeros(self.RemTerm)
        total_cf = np.zeros(self.RemTerm)

        for i in range(0, self.RemTerm):
            if i == 0:
                principal_outstanding = self.CurrBal
                scheduled_principal = 0
                default_amount = 0
                prepay_amount = 0
                interest_payment = 0
                principal_payment = 0
                recovery_amount = 0
                servicing_fee = 0
                period_cf = -self.CurrBal
            else:
                principal_outstanding = principal_remaining[i - 1]
                scheduled_principal = -npf.ppmt(self.Coupon/12,1,self.RemTerm - i, principal_outstanding)
                default_amount = (1-(1-self.CDR)**(1/12)) * principal_outstanding #
                recovery_amount = default_amount * (1-self.Severity)
                prepay_amount = (1-(1-self.CPR)**(1/12)) * (principal_outstanding - default_amount)
                interest_payment = principal_outstanding * self.Coupon/12
                principal_payment = scheduled_principal
                servicing_fee = principal_outstanding * self.ServicingFee/12
            if principal_outstanding - principal_payment < 0:
                principal_payment = principal_outstanding

            interest_pay_arr[i] = interest_payment
            principal_pay_arr[i] = principal_payment
            default_amt[i] = default_amount
            recovery_amt[i] = recovery_amount
            prepay_amt[i] = prepay_amount
            principal_remaining[i] = principal_outstanding - principal_payment - default_amount - prepay_amount
            if i == 0:
                total_cf[i] = -self.CurrBal * Price
            else:
                total_cf[i] = interest_payment + principal_payment + prepay_amount + recovery_amount - servicing_fee
            #scheduled_pay_arr[i] = scheduled_payment
            #print(principal_outstanding)
        df = pd.DataFrame(interest_pay_arr,columns=['Interest Payment'])
        df['Principal Payment'] = principal_pay_arr
        df['Principal Remaining'] = principal_remaining
        df['Prepay Amount'] = prepay_amt
        df['Default Amount'] = default_amt
        df['Recovery Amount'] = recovery_amt
        df['Total CF'] = total_cf
        #df['Scheduled Payment'] = scheduled_pay_arr
        #print(df)
        #7.5% Discount
        #print(df)
        return df


pd.options.display.max_columns = 99
wl1 = WholeLoan(1000000, 1000000, 0.075, 675, 360)
#print(wl1.runCF(1))
df = wl1.runCF(1)
#print(df)
df.to_excel(r"C:\Users\rxu\OneDrive - TPG\Desktop\Project Alexandria\TEST.xlsx")