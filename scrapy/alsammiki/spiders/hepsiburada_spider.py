import scrapy

class DmozSpider(scrapy.Spider):
    name = "hepsiburada"
    allowed_domains = ["hepsiburada.com"]
    start_urls = [
        "http://www.hepsiburada.com/eski-tarihli-ceyrek-altin-kulplu-p-GLDEZYNT1-yorumlari"
    ]

    def parse(self, response):
        for href in response.xpath("//*[@id='pagination']/ul/li/a/@href"):
            url = response.urljoin(href.extract())
            yield scrapy.Request(url, callback=self.parse_page)

    def parse_page(self, response):
        for review in response.xpath("//*[@id='reviews']/li"):
            subject = review.xpath("p[@class='review-text']/text()").extract()[0]
            self.write_subjects(subject.encode('utf-8'))
            review = review.xpath("strong[@class='subject']/text()").extract()[0]
            self.write_reviews(review.encode('utf-8'))

    def write_subjects(self, s):
        fo = open("subjects.txt", "ab")
        fo.write(s + "\n")
        fo.close()

    def write_reviews(self, r):
        fo = open("reviews.txt", "ab")
        fo.write(r + "\n")
        fo.close()
