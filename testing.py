# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 20:36:44 2015

@author: Rafeh
"""
from collections import namedtuple


user_actual = input().split()
user_expected = input().split()

Date = namedtuple('Date', ['day', 'month', 'year'])
exp_date = Date(*map(int, user_expected))
act_date = Date(*map(int, user_actual))
print(exp_date.day)
