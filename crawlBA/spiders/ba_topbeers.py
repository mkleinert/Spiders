# -*- coding: utf-8 -*-
from scrapy.selector import HtmlXPathSelector
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.http import Request
from crawlBA.items import TopItem
from scrapy.spiders import Spider
from scrapy.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
import scrapy

class BaStylesSpider(CrawlSpider):
    name = "ba_topbeers"
    allowed_domains = ["beeradvocate.com"]
    start_urls = [
        "https://www.beeradvocate.com/lists/top/"
    ]
    # global page = 0
    # rules = (
    #     Rule(LinkExtractor(allow=('/(\d+)/$', )), callback='parse_beers', process_links=lambda l: l[:1]),
    # )

    rules = (Rule(SgmlLinkExtractor(allow=(), deny=('lists')),'parse_beers', follow=False),)
    # rules = (Rule(SgmlLinkExtractor(allow=()), 'parse_start_url', follow=True),)

    def parse_beers(self, response):
        # print 'parse_beers'
        hxs = HtmlXPathSelector(response)
        sites = hxs.select('//*[@id="ba-content"]/table/tr')
        
        self.log("Scraping: " + response.url)

        items = []
        i = 0
        
        for site in sites[2:]:
             # print 'in loop'
            item = TopItem()
            # print 'beerName 1st '
            item['rank'] = site.xpath('td[1]/span/text()').extract()
            item['beerUrl'] = site.xpath('td[2]/a/@href').extract()
            item['beerName'] = site.xpath('td[2]/a/b/text()').extract()
            item['breweryUrl'] = site.xpath('//*[@id="extendedInfo"]/a[1]/@href').extract()[i]
            item['breweryName'] = site.xpath('//*[@id="extendedInfo"]/a[1]/text()').extract()[i]
            # print '^^^^^' 
            item['style'] = site.xpath('//*[@id="extendedInfo"]/a[2]/text()').extract()[i]
            # item['abv'] = site.xpath('//*[@id="extendedInfo"]/text()').extract()[i-3]
            item['avg'] = site.xpath('td[3]/text()').extract()
             # yield item
            # print item['rank']
            # print item['beerUrl'] 
            # print item['beerName'] 
            # print item['breweryUrl']
            # print item['breweryName']
            # print item['style']
            # print item['abv']
            # print item['avg']
            i += 1
            tmp_link = site.xpath('td[2]/a/@href').extract()
            new_links = ''.join(tmp_link)
            # print '===this is new links' + new_links
            

            request = Request('http://www.beeradvocate.com' + new_links, callback=self.parse_link)
            yield item
            yield request
            request.meta['item'] = item
            items.append(item)

    def parse_link(self, response):
        # print 'parse_link loop'
        item = response.meta['item']
        hxs = HtmlXPathSelector(response)
        blocks = hxs.select('//*[@id="rating_fullview_content_2"]')

        lnkbeerUrl = item['beerUrl']
        tmp_link = hxs.select('//*[@id="ba-content"]')
        # tst_tmp_link = tmp_link.xpath('//*[@id="ba-content"]/div[13]/span/a[contains(text(), "next")]/@href').extract()[0]
        # tst_tmp_link = tmp_link.xpath('//a[contains(text(), "next")]/@href').extract()
        tst_tmp_link = tmp_link.xpath("substring-after(//a, 'next ')").extract()
        print '*****'
        print tst_tmp_link
        j = 0
        
        # yield item
        for block in blocks:
            item = TopItem()
            # print "in the block loop"
            item['beerUrlRelate'] = lnkbeerUrl
            item['userRating'] = block.xpath('//span[@class="BAscore_norm"]/text()').extract()[j]
            try:
                item['individRating'] = block.xpath('//*[@id="rating_fullview_content_2"]/span[4]').extract()[j]
            except:
                item['individRating'] = 'NO RATING'
            try:
                item['descrip'] = block.xpath('//*[@id="rating_fullview_content_2"]/text()[2]').extract()[j]
            except:
                item['descrip'] = 'NO DESCRIPTION'
            item['beerUrl'] = lnkbeerUrl
            j += 1
            # print item['userRating']
            # print 'block loop end'
            yield item
        # return item
        beerUrllnk = str(tmp_link.xpath('//a[contains(text(), "next")]/@href').extract_first())
        print beerUrllnk
        # print 'http://www.beeradvocate.com' + beerUrllnk
        try: 
            print 'IN TRY'
            request = Request('http://www.beeradvocate.com' + beerUrllnk, callback=self.parse_link)
            print 'IN TRY2'
            yield request
            request.meta['item'] = item

        except:
            print 'Error in Exception'

    parse_start_url =parse_beers
