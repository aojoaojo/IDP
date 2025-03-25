#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 24 10:20:21 2022

@author: aojoaojov
"""

import pandas as pd

def get_data():
    dados = pd.read_csv('static/archive/convertcsv (1).csv')
    return dados

