import pandas as pd

def preprocess(df,region_df):

    #filtering summer olympics
    df = df[df['Season']=='Summer']
    #merge with df
    df = df.merge(region_df,how='left',on='NOC')
    #dropping duplicates
    df.drop_duplicates(inplace=True)
    #concatenate
    df = pd.concat([df,pd.get_dummies(df['Medal'])],axis=1)

    return df





