import numpy as np
import pandas as pd 
import os
#pd.test()
#csvfile = open( 'E:/homework/clone/my-app/happ/media/2.csv'  ,encoding='utf-8' )
data = pd.read_csv('E:/homework/clone/my-app/happ/media/2.csv' , encoding='utf-8' , )
#dates = dates = pd.date_range('20130101', periods=6)
#print(dates)
#vdata = data.head(10);
#for i , row  in vdata.iterrows():
#   print( row['genres'])
    #for n in row:
    #    print(n);
#print(os.listdir(os.getcwd()))
#print(data.loc[data['original_title'].str.contains(',')]) #2 complete
count = data.nunique(axis = 1)
print(data.count())
vdata = data[4:10]
#vdata = data.loc[data['original_title'].str.contains(',')].to_dict(orient='records')
#rdata = data['original_title'].value_counts()
#vdata = data.iloc[np.lexsort([rdata.index , rdata.values])]
#pdata = rdata.to_dict(orient='records')
#print(data.iloc[np.lexsort([rdata.index , rdata.values])])
#print(data['original_title'].value_counts()) #3 /// complete
#print(data['original_title'].map(type).value_counts()) #3 /// complete
#print(data.iloc[np.lexsort([rdata.index , rdata.values])]) ///3 complete
#index = data['overview'].str.contains('^[AaTtIi]{1,}' , regex=True)

#print(data.loc[data['overview'].str.contains("nt|nv", na=False)]) //  2 complete
#print(data.loc[data['overview'].isnull()]) //.complete!
#print(data.loc[data['overview'].str.contains('^W.+ +.$' , regex=True)]) #


