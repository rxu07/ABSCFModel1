# initial set-up
import pandas as pd
import numpy_financial as npf
import matplotlib.pyplot as plt
from collections import namedtuple

# loan characteristics
original_balance = 500000
coupon = 0.05
term = 360
cdr = 0.1
cpr = 0.1
severity = 0.4
recovery_lag = 12

# payments
periods = range(1, term+1)
interest_payment = npf.ipmt(
    rate=coupon / 12, per=periods, nper=term, pv=-original_balance)
principal_payment = npf.ppmt(
    rate=coupon / 12, per=periods, nper=term, pv=-original_balance)

plt.stackplot(periods, interest_payment, principal_payment,
              labels=['Interest', 'Principal'])
plt.legend(loc='upper left')
plt.xlabel("Period")
plt.ylabel("Payment")
plt.margins(0, 0)

# pandas float formatting_
pd.options.display.float_format = '{:,.2f}'.format
pd.set_option('display.max_columns', None)
# cash flow table_
cf_data = {'Interest': interest_payment, 'Principal': principal_payment}
cf_table = pd.DataFrame(data=cf_data, index=periods)
cf_table['Scheduled Payment'] = cf_table['Interest'] + cf_table['Principal']
cf_table['Ending Balance'][0] = original_balance
cf_table['Beginning Balance'] = [original_balance] + list(cf_table['Ending Balance'])[:-1]
cf_table['Default Amount'] = cf_table['Beginning Balance'] * cdr/12
cf_table['Ending Balance'] = original_balance - cf_table['Principal'].cumsum() - cf_table['Default Amount']
cf_table['Loss Amount'] = cf_table['Default Amount']* severity
cf_table['Recovery Amount'] = cf_table['Default Amount'] - cf_table ['Loss Amount']
cf_table['CNL'] = cf_table['Loss Amount'].cumsum()
cf_table['Total CF'] = cf_table['Scheduled Payment'] + cf_table['Recovery Amount']
cf_table = cf_table[['Beginning Balance', 'Scheduled Payment', 'Interest',
                     'Principal','Default Amount','Loss Amount','Recovery Amount','CNL', 'Ending Balance']]
cf_table.head(8)
cf_table.to_excel(r"C:\Users\rxu\OneDrive - TPG\Desktop\Project Alexandria\TEST.xlsx")
print(cf_table)