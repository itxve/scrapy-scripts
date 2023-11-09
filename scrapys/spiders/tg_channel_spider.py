from typing import Iterable
import scrapy
from scrapy.http import Request, HtmlResponse


from ..items import TgChannelItem


class TgChannelSpider(scrapy.Spider):
    name = "tgChannel"
    allowed_domains = ["t.me"]
    channel = ""
    range = ""  # start-end
    must_has_text = ""
    out_file = ""  # save file to
    # https://t.me/{channelNo}/{messageId}
    start_urls = []

    def start_requests(self) -> Iterable[Request]:
        if self.channel is None or self.range is None:
            raise RuntimeError("[channel] or [range] is empty")

        [start, end] = self.range.split("-")
    
        for url in [
            f"https://t.me/{self.channel}/" + str(i)
            for i in range(int(start), int(end))
        ]:
            yield Request(url)

    def parse(self, response: HtmlResponse):
        description = response.css(
            "meta[property='og:description']::attr(content)"
        ).get()

        shareItem = TgChannelItem()
        shareItem["url"] = response.url
        shareItem["description"] = description

        yield shareItem
