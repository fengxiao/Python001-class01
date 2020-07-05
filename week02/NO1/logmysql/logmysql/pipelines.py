# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql

class LogmysqlPipeline:
    def process_item(self, item, spider):
        try:
            filmid = item['filmid']
            filmname = item['filmname']
            filmtype = item['filmtype']
            plandate = item['plandate']
            output = f'pipeline:|{filmname}|\t|{filmtype}|\t|{plandate}|'
            # with open('./maoyanmovie.txt', 'a+', encoding='utf-8') as article:
            #     article.write(output)
            # return item
            print(output)
            conn = pymysql.connect(host='localhost',
                                   port=3306,
                                   user='root',
                                   password='000000',
                                   database='test',
                                   charset='utf8mb4'
                                   )
            # 获得cursor游标对象
            con1 = conn.cursor()
            # 获得清理t1表数据
            # count = con1.execute('TRUNCATE TABLE tb1;')
            # 执行插入一行数据
            TABLE_NAME = 'tb1'
            values = [(filmid, output)]
            con1.executemany('INSERT INTO ' + TABLE_NAME + ' values(%s,%s)', values)
            conn.commit()
            con1.close()
            conn.close()
        except Exception as e:
            print(e)  # 输出异常信息







