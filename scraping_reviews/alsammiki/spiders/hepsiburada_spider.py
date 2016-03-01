import scrapy

from alsammiki.items import Review


class DmozSpider(scrapy.Spider):
    name = "hepsiburada"
    allowed_domains = ["hepsiburada.com"]
    start_urls = [
        "http://www.hepsiburada.com/prima-bebek-bezi-aktif-bebek-aylik-plus-paket-5-beden-p-ZYPYON7376120-yorumlari"
    ]

    def parse(self, response):
        base_url = "http://www.hepsiburada.com/prima-bebek-bezi-aktif-bebek-aylik-plus-paket-5-beden-p-ZYPYON7376120-yorumlari?sayfa=%s"
        page_lis = response.xpath("//*[@id='pagination']/ul/li/a/text()").extract()
        for page in range(1, int(page_lis[-1]) + 1):
            yield scrapy.Request(base_url % page, callback=self.parse_page)

    def parse_page(self, response):
        print response
        review = Review()
        for r in response.xpath("//*[@id='reviews']/li"):
            review['subject'] = r.xpath("strong[@class='subject']/text()").extract()[0].encode("utf-8")
            review['text'] = r.xpath("p[@class='review-text']/text()").extract()[0].encode("utf-8")
            review['date'] = r.xpath("div[@class='reviewDate']/strong[@class='date']/text()").extract()[0]
            yield review
