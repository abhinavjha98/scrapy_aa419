# -*- coding: utf-8 -*-
import scrapy
import urllib
import requests

# item class included here 
class DmozItem(scrapy.Item):

    # define the fields for your item here like:
    URL = scrapy.Field()


class DmozSpider(scrapy.Spider):
    name = "dmoz"
    page_number = 20
    start_num = 0
    start_urls = [
    'https://db.aa419.org/fakebankslist.php'
    ]
    BASE_URL = 'https://db.aa419.org/fakebankslist.php?start=189' 
    

    def parse(self, response): 
        response_records = response.css('span.phpmaker::text').extract()
        records = ""
        for i in response_records:
            if "Records" in i:
                records = i
        page_number = records.split(" ")
        print(len(page_number))
        if len(page_number) == 6:
            DmozSpider.page_number = int(float(page_number[5]))
        else:
            DmozSpider.page_number = int(float(page_number[6]))
        yield scrapy.Request(DmozSpider.BASE_URL, callback=self.parse_attr)

        DmozSpider.BASE_URL = "https://db.aa419.org/fakebankslist.php?start="+str(DmozSpider.start_num)

        if DmozSpider.start_num<=DmozSpider.page_number:
            DmozSpider.start_num +=21
            yield response.follow(DmozSpider.BASE_URL,callback=self.parse)

    def parse_attr(self, response):
        print("Jel")
        item = DmozItem()
        links = response.css('tr.ewTableRow td a::text').extract()
        for i in links:
            if "http" in i:
                print(i)
                item["URL"] = i
                yield item