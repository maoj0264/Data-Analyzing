# CMSC641 Final Project 
# Jingning Mao
# Helper function definitions used in the project

#%matplotlib inline
import seaborn as sns
import pyodbc
import pandas as pd
import numpy as np
import scipy
import matplotlib as mpl
import matplotlib.pyplot as plt


def ShowBarPlot(data, x, y, hue, bins, title, rotation, figsize_x, figsize_y):
    fig, ax1 = plt.subplots(figsize=(figsize_x, figsize_y))

    g=sns.barplot(x=x, y=y, hue=hue,data=data, ax=ax1)
    plt.locator_params(nbins=bins)
    plt.title(title)

    #rotate x-axis labels
    g.set_xticklabels(g.get_xticklabels(), rotation=rotation)
    
    #place legend to the right
    plt.legend(bbox_to_anchor=(1,1), loc=2)

    sns.despine(fig)


def ShowBarPlotNoHue(data, x, y, bins, title, rotation, figsize_x, figsize_y):
    fig, ax1 = plt.subplots(figsize=(figsize_x, figsize_y))

    g=sns.barplot(x=x, y=y, data=data, ax=ax1)
    plt.locator_params(nbins=bins)
    plt.title(title)

    #rotate x-axis labels
    g.set_xticklabels(g.get_xticklabels(), rotation=rotation)
    
    #place legend to the right
    plt.legend(bbox_to_anchor=(1,1), loc=2)

    sns.despine(fig)
    
def ShowLmplotByRow(data, x, y, hue, row, bins, title, size):

    g= sns.lmplot(x=x, y=y, hue=hue, row=row, data=data, size=size)
    plt.locator_params(nbins=bins)
    plt.title(title)


def ShowLmplotByRowNoHue(data, x, y, row, bins, title, size):

    g= sns.lmplot(x=x, y=y, row=row, data=data, size=size)
    plt.locator_params(nbins=bins)
    plt.title(title)


def ShowLmplot(data, x, y, bins, title, size):

    g= sns.lmplot(x=x, y=y, data=data, size=size)
    plt.locator_params(nbins=bins)
    plt.title(title)
    
    
def ShowPairplot(data, hue, title, size):
    g = sns.pairplot(data, hue=hue, size = size)
    plt.title(title)


def ExceSQL(sql, connectionString):
    
    #cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=MAO2015;DATABASE=Amazon;UID=rpt_user;PWD=itrpt1!')
    cnxn = pyodbc.connect(connectionString)
    cnxn.autocommit = True
    cnxn.execute(sql)
    cnxn.close()