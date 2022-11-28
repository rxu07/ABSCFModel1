import CMO_Model as CMO
import pandas as pd
PoolCF = CMO.poolCashFlows(100000,200,360,3,2.75,4.5,12,0.55)
df = pd.DataFrame.from_dict(PoolCF)
df.to_csv('CF.csv',index = False, header=True)