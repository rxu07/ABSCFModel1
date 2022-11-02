import pandas as pd
import numpy_financial as npf
import matplotlib.pyplot as plt
from collections import namedtuple


class RWL:
    OrigBal = 500000
    CurrBal = 500000
    Coupon = 10
    OrigFICO = 700
    CurrFICO = 725
    OrigTerm = 360
    RemTerm = 360
    CDR = 10
    Severity = 50
    CPR = 10

    periods = range(1, OrigTerm + 1)

    CDR_Curve = ''
    CNL_Curve = ''
    CPR_Curve = ''

    def __init__(self):
        ...

    def generateCF(self):
        print('Generating CF')

    def getFICOBucket(self):
        FICO_Bucket = ''
        if (RWL.CurrFICO) < 600:
            FICO_Bucket = '<600'
        elif RWL.CurrFICO < 625:
            FICO_Bucket = '600-625'
        elif RWL.CurrFICO < 625:
            FICO_Bucket = '600-625'
        elif RWL.CurrFICO < 625:
            FICO_Bucket = '600-625'
        elif RWL.CurrFICO < 625:
            FICO_Bucket = '600-625'
        elif RWL.CurrFICO < 625:
            FICO_Bucket = '600-625'
        elif RWL.CurrFICO < 625:
            FICO_Bucket = '600-625'
        elif RWL.CurrFICO < 625:
            FICO_Bucket = '600-625'
        elif RWL.CurrFICO < 625:
            FICO_Bucket = '600-625'
        elif RWL.CurrFICO < 625:
            FICO_Bucket = '600-625'
        else:
            FICO_Bucket = 'Other'
        return FICO_Bucket

    def getLLCF(self):
        LLCF = []


test = RWL()
print(test.getFICOBucket())
print(test.CurrFICO)

#Read CDR
#Read CPR
#Read Severity Curves
#Recovery