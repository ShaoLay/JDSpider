# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exporters import JsonItemExporter


class BookPipeline(object):
    def open_spider(self, spider):
        self.file = open('book.json', 'wb')
        self.write = JsonItemExporter(self.file)
        self.write.start_exporting()

    def process_item(self, item, spider):
        self.write.export_item(item)
        return item

    def close_spider(self, spider):
        self.write.finish_exporting()
        self.file.close()
