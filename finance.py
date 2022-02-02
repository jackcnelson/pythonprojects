# MIS 207 HW05-Q2
#
# This program contains financial functions

import math

# Creation of necessary formulas
def present_value(fv, r, n):
    return (fv / (1 + r)) ** n

def future_value(pv, r, n):
    return (pv * (1 + r)) ** n

def rate_of_return(fv, pv, n):
    return ((fv / pv) ** (1 / n)) - 1

def number_of_terms(fv, pv, r):
    return math.log(fv / pv) / math.log(1 + r)


