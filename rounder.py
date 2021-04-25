"""
***********************************************

Author: MontyGUI
Last Edit: 23/4/2021

Description
This script includes arithmetics functions of rounding a number

***********************************************
"""
import math


def round_half_up(n, decimals=0):
    mtp = 10 ** decimals
    return math.floor(n * mtp + 0.5) / mtp


def round_basic(n, decimals=0):
    rounded_abs = round_half_up(abs(n), decimals)
    return math.copysign(rounded_abs, n)
