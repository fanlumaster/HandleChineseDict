# -*- coding: utf-8 -*-
# @File  : test_mysql.py
# @Author: FanyFull
# @Date  : 2021/8/20

import pymysql.cursors

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='lf123456',
                             database='dictsdb',
                             cursorclass=pymysql.cursors.DictCursor)

with connection:
    # with connection.cursor() as cursor:
    #     # insert a record
    #     value = ('1', '00002', '扒', '手', '2', '5', '(一)ㄅㄚ', '(一)bā', None, None, '[動]\n1.剝開。如：「把橘子扒開來吃。」\n2.扯掉。如：「扒衣裳」。\n3.挖開、刨開。如：「扒土」、「扒堤」。\n4.用手攀住東西。如：「扒著欄杆」、「你扒住，不然會掉下去。」', None, '(二)ㄆㄚˊ\u3000pá（00584）', '0')
    #     sql = "INSERT INTO `dict_tb` (`property`, `word_num`, `name`, `part_excluded`, `part_num`, `all_num`, `punc`, `pinyin`, `similar`, `opposite`, `meaning`, `edit_comment`, `duoyin`, `yiti`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    #     cursor.execute(sql, value)
    # connection.commit()

    with connection.cursor() as cursor:
        # read records
        sql = "SELECT * FROM `dict_tb` WHERE `word_num` = %s"
        word_num = '00272'
        cursor.execute(sql, (word_num,))
        result = cursor.fetchone()
        print(result)
        for key in result:
            print(key)
            print(result[key])
            print('======')

