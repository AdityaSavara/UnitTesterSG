# -*- coding: utf-8 -*-
def sum_of_elements(value_list=[]):
    sum_elements=0
    for i in range(0,len(value_list)):
        sum_elements=sum_elements+int(value_list[i])
    return sum_elements
