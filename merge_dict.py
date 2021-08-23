# -*- coding: utf-8 -*-
# @File  : merge_dict.py
# @Author: FanyFull
# @Date  : 2021/8/21

# 将三个分表合并成一个总表

import pymysql.cursors

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='lf123456',
                             database='dictsdb',
                             cursorclass=pymysql.cursors.DictCursor)

n = 0
with connection:
    # with connection.cursor() as cursor:
    #     # insert a record
    #     value = ('1', '00002', '扒', '手', '2', '5', '(一)ㄅㄚ', '(一)bā', None, None, '[動]\n1.剝開。如：「把橘子扒開來吃。」\n2.扯掉。如：「扒衣裳」。\n3.挖開、刨開。如：「扒土」、「扒堤」。\n4.用手攀住東西。如：「扒著欄杆」、「你扒住，不然會掉下去。」', None, '(二)ㄆㄚˊ\u3000pá（00584）', '0')
    #     sql = "INSERT INTO `dict_tb` (`property`, `word_num`, `name`, `part_excluded`, `part_num`, `all_num`, `punc`, `pinyin`, `similar`, `opposite`, `meaning`, `edit_comment`, `duoyin`, `yiti`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    #     cursor.execute(sql, value)
    # connection.commit()

    with connection.cursor() as cursor:
        # read records
        sql = "SELECT * FROM `dict_tb_all`"
        cursor.execute(sql)
        result = cursor.fetchall()
        for item in result:
            n = n + 1
            record = list(item.values())[1:]
            sql = "INSERT INTO `dict_tb_all_backup` (`property`, `word_num`, `name`, `part_excluded`, `part_num`, `all_num`, `punc`, `pinyin`, `similar`, `opposite`, `meaning`, `edit_comment`, `duoyin`, `yiti`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(sql, record)
            print(str(n) + " success")
        connection.commit()
        print('all success')
