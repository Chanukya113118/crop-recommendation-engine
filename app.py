import pandas as pd
import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
data=pd.read_excel('data.xlsx')
#rfc=RandomForestClassifier()
le=LabelEncoder()
data['le']=le.fit_transform(data['label'])
xtr,xtes,ytr,ytes=train_test_split(data.iloc[:,:7],data.iloc[:,-1])
#fit=rfc.fit(xtr,ytr)
print(xtr.head(2))
#print(rfc.score(xtes,ytes))
'''with open('model.pkl','wb') as f:
    pickle.dump(rfc,f)'''

    
