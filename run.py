import os

channel = os.getenv("channel")
range = os.getenv("range")
must_has_text = os.getenv("must_has_text")


os.system(
    f"scrapy crawl tgChannel -a channel={channel} -a range={range} -a must_has_text={must_has_text}"
)
