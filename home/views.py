from django.shortcuts import render
from django.http import HttpResponse
import csv
import json
from .forms import UploadFileForm
from django.conf import settings
import pandas as pd
import numpy as np
import os
from .models import accuracyProcess, completeProcess, tractablilityProcess
from django.core.files.storage import FileSystemStorage

def index(request):
    return render(request, 'blog/data_set.html', {'flag': 'Success'})
def upload(request):
    #main dataset process function
    if request.method == 'POST':        
        if request.POST['upload_flag'] == '0':
            # when first dataset was uploaded, the dataset file must be .csv file;
            myfile = request.FILES['data_file']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.url(filename)
            col1s = []  # int.
            col2s = []  # float.
            col3s = []  # object.
            colms = []
            if uploaded_file_url != '':
                #when dataset file isn't empty;
                csvfile = open(settings.BASE_DIR +
                               uploaded_file_url, encoding='utf-8')
                spmreader = csv.DictReader(csvfile)
                datas = pd.read_csv(settings.BASE_DIR +
                                    uploaded_file_url, encoding='utf-8')
                cns = datas.dtypes
                typs = []
                # the data's columns is classified by data type(int64,float64,object)
                for col, type in cns.items():
                    colms.append(col)
                    typs.append(type)
                    if type == 'int64':
                        col1s.append(col)
                    elif type == 'float64':
                        col2s.append(col)
                    else:
                        col3s.append(col)
                return render(request, 'blog/data_set.html',
                              {'flag': 'File Uploaded Success!!!', 'uploaded_file_url': uploaded_file_url, 'columns':colms, 'data': spmreader, 'columnInt': col1s, 'columnFloat': col2s, 'columnObject': col3s, 'types': typs})
        else:
            if request.POST['path'] != '' and request.POST['path'] != 'Error':
                # this part is the analysis processing part of the data gathering already set.                
                data = pd.read_csv(settings.BASE_DIR +
                                   request.POST['path'], encoding='utf-8')
                # dataset column getting.
                cns = data.dtypes
                col1s = []  # int.
                col2s = []  # float.
                col3s = []  # object.
                typs = []
                colms = []
                # the data's columns is classified by data type(int64,float64,object)
                
                for col, type in cns.items():
                    typs.append(type)
                    colms.append(col)
                    if type == 'int64':
                        col1s.append(col)
                    elif type == 'float64':
                        col2s.append(col)
                    else:
                        col3s.append(col)
                cnt = data.nunique(axis=1)
                a_cnt = cnt.count()
                
                key1 = request.POST['column1']
                key2 = request.POST['column2']
                key3 = request.POST['column3']
                key4 = request.POST['column4']
                key5 = request.POST['column5']
                fields = [];
                fields.append(key1)
                fields.append(key2)
                fields.append(key3)
                fields.append(key4)
                fields.append(key5)

                # vdata = [];
                if request.POST['funct'] == 'complete':
                    pdata = completeProcess(data, fields)
                    # vdata = data.head(4).to_dict(orient='records') # 2
                    # vdata = data.iloc[4].to_dict(orient='records') # 3
                    nnp = len(pdata.to_dict(orient='records')) * 100 / a_cnt
                    return render(request, 'blog/data_set.html', {'flag': 'File Uploaded Success!!!', 'uploaded_file_url': request.POST['path'], 'c_percent': nnp, 'col1': key1, 'col2': key2, 'col3': key3, 'col4': key4, 'col5': key5, 'columns':colms, 'columnInt': col1s, 'columnFloat': col2s, 'columnObject': col3s, 'data': pdata.to_dict(orient='records')})
                elif request.POST['funct'] == 'accuracy':
                    # rdata = data.loc[data['original_title'].str.contains(',')] #11
                    # rdata = data.loc[data['overview'].str.contains("nt|nv", na=False)] #12
                    pdata = accuracyProcess(data, fields)                    
                    nnp = len(pdata.to_dict(orient='records')) * 100 / a_cnt #Calculate the percentage.
                   # nnt = nnp.count() * 100 / a_cnt

                    return render(request, 'blog/data_set.html', {'flag': 'File Uploaded Success!!!', 'uploaded_file_url': request.POST['path'], 'a_percent': nnp, 'col1': key1, 'col2': key2, 'col3': key3, 'col4': key4, 'col5': key5, 'columns':colms, 'columnInt': col1s, 'columnFloat': col2s, 'columnObject': col3s, 'data': pdata.to_dict(orient='records')})
                elif request.POST['funct'] == 'trac':
                    # vdata = data['original_title'].value_counts() #18
                    # vdata = data['original_title'].map(type).value_counts() #17
                    # rdata = data['original_title'].value_counts()
                    rdata = tractablilityProcess(data, fields)                    
                    nn = len(rdata.to_dict(orient='records')) * 100 / a_cnt #Calculate the percentage.
                    # vdate = pdata.to_dict(orient='records')
                    return render(request, 'blog/data_set.html', {'flag': 'File Uploaded Success!!!', 'uploaded_file_url': request.POST['path'], 'col1': key1, 'col2': key2, 'col3': key3, 'col4': key4, 'col5': key5, 't_percent': nn, 'columnInt': col1s,  'columns':colms, 'columnFloat': col2s, 'columnObject': col3s, 'data': rdata.to_dict(orient='records')})
                elif request.POST['funct'] == 'summary':
                    # vdata = data['original_title'].value_counts() #18
                    # vdata = data['original_title'].map(type).value_counts() #17
                    # rdata = data['original_title'].value_counts()                   
                    vdata = completeProcess(data, fields)
                    cpt = len(vdata.to_dict(orient='records')) * 100 / a_cnt #Calculate the percentage.

                    rdata = tractablilityProcess(data, fields)          
                    tpt = len(rdata.to_dict(orient='records')) * 100 / a_cnt # whether key1 column is empty!

                    pdata = accuracyProcess(data, fields)  
                    apt = len(pdata.to_dict(orient='records')) * 100 / a_cnt

                    return render(request, 'blog/data_set.html',
                                  {'flag': 'File Uploaded Success!!!', 'uploaded_file_url': request.POST['path'], 'col1': key1, 'col2': key2, 'col3': key3, 'col4': key4, 'col5': key5, 'columnInt': col1s, 'columnFloat': col2s, 'columnObject': col3s, 'columns':colms, 't_percent': tpt, 'a_percent': apt, 'c_percent': cpt,  'data': data.to_dict(orient='records')})
                else:
                    render(request, 'blog/data_set.html',
                           {'flag': 'File Uploaded Fail!', 'uploaded_file_url': ''})

            else:
                render(request, 'blog/data_set.html',
                       {'flag': 'File Uploaded Fail!', 'uploaded_file_url': ''})

    return render(request, 'blog/data_set.html', {'flag': 'File Uploaded Fail!', 'uploaded_file_url': 'Error'})
