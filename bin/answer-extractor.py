#loads the answers in JSON

import json
import sys
import glob


def counter(count_list,status):

    if status == 'a':
        count_list['a'] = count_list['a'] + 1
    elif status == 'b':
        count_list['b'] = count_list['b'] + 1
    elif status == 'c':
        count_list['c'] = count_list['c'] + 1
    elif status == 'd':
        count_list['d'] = count_list['d'] + 1
    elif status == 'e':
        count_list['e'] = count_list['e'] + 1
    else: 
        count_list['u'] = count_list['u'] + 1

    return count_list

answer_file = sys.argv[1]

keys = ['a','b','c','d','e','u']
count_list = dict.fromkeys(keys,0)

with open(answer_file) as json_data:
    for line in json_data:
        data = json.loads(line)
        counter(count_list,data['status'].replace('@cmunell ','').lower())

print str(count_list.values()).strip('[]').replace(', ',';')
