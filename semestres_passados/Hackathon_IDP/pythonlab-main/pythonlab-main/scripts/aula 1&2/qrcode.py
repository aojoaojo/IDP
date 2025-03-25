#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 15:54:15 2023

@author: mac-prof
"""

import qrcode 
qrcode.make("https://github.com/idp-pclp/pythonlab").save("pythonlab.png")