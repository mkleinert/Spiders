# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import sys,traceback
import MySQLdb
import hashlib
from scrapy.exceptions import DropItem
from scrapy.http import Request
from crawlBA.items import TopItem


class SQLStore(object):
    def __init__(self):
        # print 'in pipeline'
        self.conn = MySQLdb.connect(user='root', passwd='', db='ETL', host='localhost', charset="utf8", use_unicode=True)
        self.cursor = self.conn.cursor()



    def process_item(self, item, spider):
        # print "pipeline process item"
        # print item['breweryName']
        # print item['userRating']
        try:
            # print 'IN TRY'
            if 'breweryName' in item:
                # print 'INSERT'
                query = ("""INSERT INTO top_beer(breweryName) VALUES (%s)""",('breweryName'))
                data = ('TEST')
                # print query
                self.cursor.execute('INSERT INTO ETL.top_beer(breweryURL,breweryName,beerName,beerUrl,style,rank) VALUES (%s,%s,%s,%s,%s,%s)',(item['breweryUrl'],item['breweryName'],item['beerName'],item['beerUrl'],item['style'],item['rank'])) 
                # self.cursor.execute("""INSERT INTO top_beer(breweryUrl,breweryName,beerName,beerUrl,style,avg,rank) VALUES (%s,%s,%s,%s,%s,%s,%s)""", (item['breweryUrl'],item['breweryName'],item['beerName'],item['beerUrl'],item['style'],item['avg'],item['rank']))
                self.conn.commit()
                # print 'INSERT DONE'
            if 'userRating' in item:
                # print 'INSERT RATING'
                # query = "INSERT INTO beer_rating(beerUrl,userRating,individRating,description) VALUES (%s,%s,%s,%s)", (item['beerUrl'],item['userRating'],item['individRating'],item['descrip'])
                
                # print query
                self.cursor.execute('INSERT INTO ETL.beer_rating(beerUrl,userRating,individRating,description) VALUES (%s,%s,%s,%s)',(item['beerUrl'],item['userRating'],item['individRating'],item['descrip']))
                
                self.conn.commit()

        #     self.cursor.execute("""INSERT INTO BA_Beer(beerName,abv,avg,hads) VALUES (%s,%s,%s,%s)""", (item['beerName'],item['abv'],item['avg'],item['hads']))
        #     self.conn.commit()
            # print 'breweryName db'


            # self.conn.close()

            # if 'referUrl' in item:
            #
            #     # for i,items in item.iteritems():
            #     # for k in item.fields.iterkeys():
            #     print "in beer_rating if statement"
            #     self.cursor.execute("""INSERT INTO beer_rating(userRating,individRating,descrip) VALUES (%s,%s,%s)""", (item['userRating'][1],item['individRating'][1],item['descrip'][1]))
            #     self.conn.commit()
            #     print 'userRating db'
            #     # self.conn.close()


        except MySQLdb.Error, e:
            print "Error %d: %s" % (e.args[0], e.args[1])
            

            # return item
