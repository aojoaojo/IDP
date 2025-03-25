#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 24 10:20:21 2022

@author: aojoaojov
"""

import pandas as pd

def get_data2():
    dados = pd.read_csv('static/archive/netflix_titles.csv')
    return dados

