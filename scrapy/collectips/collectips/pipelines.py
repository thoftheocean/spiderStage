# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import sys
reload(sys)
sys.setdefaultencoding('utf8')
import MySQLdb


class CollectipsPipeline(object):

    def process_item(self, item, spider):
        #写入txt文本
        # print 'aaa'
        # ips ='ip地址：%s\n端口：%s\n类型：%s\n速度：%s\n位置：%s\n'%(item['ip'],item['port'],item['type'],item['speed'],item['position'])
        # with open('ip1.txt','a') as f:
        #     f.write(ips)
        # return item

        #写入数据库

        DBKWARGS = spider.settings.get('DBKWARGS')
        con = MySQLdb.connect(**DBKWARGS)
        cur = con.cursor()
        sql = ("insert into xiciips(ip,port,type,position,speed) "
               "values(%s,%s,%s,%s,%s)")
        lis = (item['ip'], item['port'], item['type'], item['position'], item['speed'])
        try:
            cur.execute(sql, lis)
        except Exception, e:
            print "Insert error:", e
            con.rollback()
        else:
            con.commit()
        cur.close()
        con.close()
        return item