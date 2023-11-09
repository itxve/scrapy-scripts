import scrapy
from scrapy.http import HtmlResponse
from ..items import GithubTrendingItem


class TrendingSpider(scrapy.Spider):
    name = "trending"

    def start_requests(self):
        urls = [
            "https://github.com/trending",
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response: HtmlResponse):
        article = response.css("div[data-hpc] > article")
        for article in article:
            item = GithubTrendingItem()
            item["href"] = response.urljoin(article.css("h2 > a::attr(href)").get())
            # item["org"] = article.css("h2 > a > span::text").get().strip()
            # item["repo"] = "".join(
            #     el.strip() for el in article.css("h2 > a::text").getall()
            # )
            item["description"] = article.css("p::text").get("").strip()
            item["language"] = article.css(
                "span[itemprop='programmingLanguage']::text"
            ).get()
            item["total_start"] = (
                article.css(".f6 > a[href*=stargazers]::text").getall()[1].strip()
            )
            item["fork_start"] = (
                article.css(".f6 > a[href*=forks]::text").getall()[1].strip()
            )

            item["today_start"] = (
                article.css(".float-sm-right::text").getall()[1].strip().split(" ")[0]
            )

            yield item
