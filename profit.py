import json
import time
import numpy as np


with open ('list_chains.txt', 'r') as list_ch:
        list_chains = json.load (list_ch)

_list = np.array (list_chains)

def profit (_dict):
    fee_taker = 0.001   
    for i in range (len(_list)):
        if  _dict[_list[i,0,0]] != [-1,-1] and  _dict[_list[i,1,0]] != [-1,-1] and _dict[_list[i,2,0]] != [-1,-1]:   
            if _list [i,1,1] == "ask":                       
                profit = (float(_dict[_list[i,2,0]][1]) * (1-fee_taker)**3)/(float(_dict[_list[i,0,0]][0])*float(_dict[_list[i,1,0]][0]))
                coef_profit = profit - 1
                if coef_profit > 0:
                    pass
                    #print (coef_profit, '  ', f'{_list[i,0,0]}/{_list[i,1,0]}/{_list[i,2,0]}')
                #return (coef_profit)
            else:
                profit = (float(_dict[_list[i,1,0]][1])*float(_dict[_list[i,2,0]][1])*(1-fee_taker)**3)/(float(_dict[_list[i,0,0]][0]))
                coef_profit = profit - 1
                if coef_profit > 0:
                    pass
                    #print (coef_profit, '  ', f'{_list[i,0,0]}/{_list[i,1,0]}/{_list[i,2,0]}')
                #return (coef_profit)


def run (queue_flag,queue_dict):
    time.sleep (30)
    queue_flag.put (True)
    while True:
        _dict = queue_dict.get ()
        profit (_dict)
        queue_flag.put (True)