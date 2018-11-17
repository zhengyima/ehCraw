# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem

class MyImagesPipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        for image_url in item['image_urls']:
            #print("++++++++++++++++++++++++++++++++--------------------------------------------")
            #print(item)
            yield scrapy.Request(image_url)

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        #image_paths = [item["title_hash"]+"/"+str(item["id"])+".jpg" for ok, x in results if ok]
        print("images_paths:--------------------------------------------")
        print(image_paths)
        for p in image_paths:
            f = open("/root/mulu.txt","wb+")
            f.write(p + "\t" + str(item["id"]) + "\t" + item["title"] + "\n")
            f.close()
        if not image_paths:
            raise DropItem("Item contains no images")
        item['image_paths'] = image_paths
        return item