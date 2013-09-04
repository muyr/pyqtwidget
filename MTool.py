# -*- coding: cp936 -*-
###################################################################
# Author: Mu yanru
# Date	: 2013.09
# Email : muyanru345@163.com
###################################################################


import os, time

def openDir(dirName):
    resultName = dirName
    # dirName is a file
    if os.path.isfile(dirName):
        resultName = os.path.dirname(dirName)
    os.startfile(resultName)

def openFile(fileName):
    try:
        os.startfile(fileName)
    except:
        pass

def getCurrentDateFormat():
    return time.strftime('%Y-%m-%d',time.localtime(time.time()))

def getCurrentDate():
    return time.strftime('%Y%m%d',time.localtime(time.time()))

def getCurrentDateTime():
    return time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))

def getCurrentDateTimeString():
    return time.strftime('%Y-%m-%d %H:%M',time.localtime(time.time()))