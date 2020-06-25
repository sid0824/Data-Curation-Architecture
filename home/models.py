from django.db import models
import csv
import pandas as pd
import numpy as np
# Create your models here.


def completeProcess(dataset, fields):
    key1 = fields[0]
    vdata = dataset.loc[dataset[key1] > 0] # whether key1 column is empty!    
    
    return vdata
def accuracyProcess(dataset, fields):
    # data = dataset.loc[dataset[fields[0]] > 0]
    if fields[2] != '':
        data = dataset.loc[dataset[fields[2]].notnull()] # whether key3 column is empty!
    if fields[4] != '':
        data = dataset.loc[dataset[fields[4]].notnull()] # whether key5 column is empty!
    rdata = data[fields[0]].value_counts()  #  whether key3 column is empty!
    pdata = data.iloc[np.lexsort([rdata.index, rdata.values])]
    return pdata
def tractablilityProcess(dataset, fields):
    data = dataset.loc[dataset[fields[0]] > 0]
    if fields[2] != '':
        rdata = data.loc[data[fields[2]].str.contains("a", na=False)] # whether key3 column contains "a"
    
    return rdata
    
    
    