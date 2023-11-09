# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json, os
from scrapy.exceptions import DropItem
from .spiders.tg_channel_spider import TgChannelSpider


class GithubTrendingPipeline:
    def process_item(self, item, spider):
        return item


class TgChannelPipeline:
    must_has_text = ""

    def open_spider(self, spider: TgChannelSpider):
        self.resolve_rule(spider)
        os.makedirs("./out", exist_ok=True)
        self.file = open(
            f"./out/{spider.channel + spider.range}.jsonl", "w", encoding="utf-8"
        )

    def resolve_rule(self, spider: TgChannelSpider):
        self.must_has_text = spider.must_has_text or ""
        pass

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        if (
            self.must_has_text is not None
            and not self.must_has_text in item["description"]
        ):
            raise DropItem(f"missing [{self.must_has_text}] content")

        self.file.write(
            json.dumps(
                {"url": item["url"], "description": item["description"]},
                ensure_ascii=False,
            )
            + "\n"
        )
