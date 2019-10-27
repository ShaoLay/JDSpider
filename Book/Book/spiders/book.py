# -*- coding: utf-8 -*-
from copy import deepcopy

import scrapy

from Book.items import BookItem


class BookSpider(scrapy.Spider):
    name = 'book'
    allowed_domains = ['jd.com']
    start_urls = ['https://book.jd.com/booksort.html']

    def parse(self, response):
        print('我是请求的url地址:',response.url)
        dt_list = response.xpath('//*[@id="booksort"]/div[2]/dl/dt')
        for dt in dt_list:
            item = BookItem()
            item['big_name'] = dt.xpath('./a/text()').extract_first()
            em_list = dt.xpath('./following-sibling::[1]/em')
            for em in em_list:
                item['small_name'] = em.xpath('./a/text()').extract_first()
                item['small_url'] = 'https:' + em.xpath('./a/@href')

                yield scrapy.Request(
                    item['small_url'],
                    callback=self.parse_small_list,
                    meta={'bigkey':deepcopy(item)}
                )

    def parse_small_list(self, response):
        li_list = response.xpath('//*[@id="plist"]/ul/li')

        for li in li_list[:1]:
            item = response.meta['bigkey']
            item['book_image'] = "https:" + li.xpath('.//div[@class="p-img"]/a/img/@src').extract_first()
            # 图书的名字
            item['book_name'] = li.xpath('.//div[@class="p-name"]/a/em/text()').extract_first().strip()

            # 图书的作者
            item['book_author'] = li.xpath('.//span[@class="p-bi-name"]/span/a/text()').extract_first()

            # 出版社
            item['book_store'] = li.xpath('.//span[@class="p-bi-store"]/a/text()').extract_first()

            # 出版时间
            item['book_time'] = li.xpath('.//span[@class="p-bi-date"]/text()').extract_first().strip()

            # 商品id
            item['book_sku'] = li.xpath('./div/@data-sku').extract_first()

            yield item