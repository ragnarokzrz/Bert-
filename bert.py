# -*- coding: utf-8 -*-
# @Time    : 2019/7/30 10:06
# @Author  : zhangruizhong
# @FileName: bert.py
# @Software: PyCharm

import re
from bert_base.client import BertClient
from config import Config
import logging

logging.basicConfig(level=logging.INFO)

# bc1 =  BertClient(ip=Config.bert.host, port=Config.bert.port1,port_out=Config.bert.out_port1, show_server_config=False, check_version=False,
#                  check_length=False)
#
# bc2 =  BertClient(ip=Config.bert.host, port=Config.bert.port2,port_out=Config.bert.out_port2, show_server_config=False, check_version=False,
#                  check_length=False)

def is_num(input_str):
    input_str = str(input_str)
    return re.search(r'\d', input_str) != None

def get_word(rs_st, str1):
    list_rs = []
    content = ""
    for i in range(len(rs_st)):
        rs = []
        if rs_st[i] == 'B-LOC':
            if content != "":
                list_rs.append(content)

            content = str1[i]
        elif rs_st[i] == "I-LOC":
            content += str1[i]
        else:
            if content != "":
                list_rs.append(content)
                content = ""
    if content != "":
        list_rs.append(content)
    return list_rs

    #     if rs_st[i] != 'O':
    #         if rs_st[i][0] == 'B':
    #             if '*#*' in content:
    #                 list_rs[content.split('*#*')[0]].append(content.split('*#*')[1])
    #             content = category + '*#*' + str1[i]
    #         elif rs_st[i][0] == 'I':
    #             content += str1[i]
    # # print(rs_st)
    # if '*#*' in content:
    #     list_rs[content.split('*#*')[0]].append(content.split('*#*')[1])
    # return list_rs




def get_bert(str1, bertNum):
    str1 = str1.strip().upper()
    str1 = str1.replace(" ", "")
    str1 = str1.replace("\t", "").replace("\n", "")
    list_i = [ii for ii in u"%s" % (str1)]
    list_ii = []
    for iii in list_i:
        if iii.strip() == "":
            continue
        else:
            list_ii.append(iii)
    rst = None
    if bertNum == 0:
        with BertClient(ip=Config.bert.host, port=Config.bert.port1, port_out=Config.bert.out_port1,
                   show_server_config=False, check_version=False,
                   check_length=False) as bc1:
            rst = bc1.encode([list_ii], is_tokenized=True)
    else:
        with BertClient(ip=Config.bert.host, port=Config.bert.port2, port_out=Config.bert.out_port2,
                        show_server_config=False, check_version=False,
                        check_length=False) as bc2:
            rst = bc2.encode([list_ii], is_tokenized=True)

    entitys = [i for i in get_word(rst[0], list_ii) if len(i) > 1]
    #打印结果
    logging.info(("实体:" + "\t".join(entitys)+"\n"+str(rst[0])))

    return entitys

