#!/usr/bin/python3
# coding: utf-8

import numpy as np
import hashlib
import pandas
from scipy.misc import imsave as ims
from keras.models import model_from_json

import sys
import os

def hash_to_im(hash):
    h=hashlib.md5(bytes(hash, encoding = 'utf-8'))
    h=h.hexdigest()
    h=int(h,16)
    s=[]
    for j in range(len(str(h))//2):
        s.append(int(str(h)[j*2:j*2+2]))

        np.random.seed(s)
        noise = np.random.normal(0, 1, (1, 100))
        sh=loaded_model.predict(noise)
        sh = 0.5 * sh + 0.5
        sh=sh[0]
        pic_shape=sh.shape

        sh1=np.zeros([pic_shape[0]+28,pic_shape[1]+28,3])

        sh1[15:-13,15:-13,:]=sh
    return sh1

if __name__ == "__main__":
    
    
    json_file = open('generator.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)
    weight='gen.h5'
    loaded_model.load_weights(weight)
    
    
    Hash=sys.argv[1]
    stat2=sys.argv[2]
    if stat2[-1]=='/':
        pass
    else:
        stat2=stat2+'/'
        
    # Файлы .tsv
    if Hash[-4:]=='.tsv':
        A=pandas.read_csv(Hash,header=None)
        for i in range(len(A)):
            ims(stat2+str(A[0][i])+'.png',hash_to_im(A[0][i][4:-8]))
            
    # Файлы .txt        
    if Hash[-4:]=='.txt':
        f = open(Hash)
        b=f.read().split('\n')
        f.close()
        for i in range(len(b)):
            if len(b[i])==52:
                
                ims(stat2+b[i]+'.png',hash_to_im(str(b[i])[4:-8]))
    # Hash
    else:
        ims(stat2+Hash+'.png',hash_to_im(Hash[4:-8]))