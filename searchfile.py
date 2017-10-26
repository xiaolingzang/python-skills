# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 18:17:54 2017

@author: zangxiaoling
"""

import os
def search(s,path=os.getcwd()):
    filelst=[x for x in os.listdir(path)]
    for filename in filelst:
        filepath=os.path.join(path,filename)
        if os.path.isfile(filepath):
            if s in filename:
                print(os.path.realpath(filepath))
        elif os.path.isdir(filepath):
            search(s,filepath)

if __name__=='__main__':
    s=input('Enter the string: ')
    search(s)