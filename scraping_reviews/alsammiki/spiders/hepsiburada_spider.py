import scrapy

# -*- coding: utf-8 -*-
from alsammiki.items import Review


class DmozSpider(scrapy.Spider):
    name = "hepsiburada"
    allowed_domains = ["hepsiburada.com"]
    start_urls = [
      #"http://www.hepsiburada.com/oral-b-vitality-sarj-edilebilir-dis-fircasi-cross-action-p-SGORAL043577-yorumlari"
        #"http://www.hepsiburada.com/lg-g4-32-gb-ithalatci-garantili-p-TELCEPLGG432GR-DS3-yorumlari"
        "http://www.hepsiburada.com/prima-bebek-bezi-aktif-bebek-aylik-plus-paket-5-beden-p-ZYPYON7376120-yorumlari"
        #"http://www.hepsiburada.com/sinbo-sbs-4427-dijital-baskul-p-SGSINBOSBS4427-yorumlari",
        #"http://www.hepsiburada.com/sandisk-32gb-microsd-48mb-s-class10-hafiza-karti-sdsqunb-032g-gn3mn-p-FTHFZSND32GMCG48-yorumlari",
        #"http://www.hepsiburada.com/delta-vinyl-altigen-koseli-ciftli-renkli-dambil-set-p-SPORDELTA1289-1X2-yorumlari",
        #"http://www.hepsiburada.com/delta-cok-fonksiyonlu-deluxe-kapi-barfiksi-mekik-sinav-cekme-aleti-ds-1325-p-SPORDELTA787-yorumlari",
        #"http://www.hepsiburada.com/gillette-fusion-proglide-flexball-tiras-makinesi-4-lu-tiras-bicagi-p-SGSTOK12112-yorumlari",
        #"http://www.hepsiburada.com/altis-sd5000-trendy-m-2-5-hp-masajli-motorlu-mp3-calar-kosu-bandi-body-roller-hediye-p-SPORALTISSD5000-yorumlari",
        #"http://www.hepsiburada.com/arnica-bora-4000-2400-watt-su-filtreli-turbo-fircali-elektrikli-supurge-yesil-p-EVARNICABORA4000-yorumlari",
        #"http://www.hepsiburada.com/samsung-hm1500-bluetooth-kulaklik-cift-telefon-destegi-p-TELBKULSAMHM1500-yorumlari",
        #"http://www.hepsiburada.com/logitech-m175-kablosuz-nano-mouse-910-002777-p-BD40120-yorumlari"
    ]

    def parse(self, response):
        base_url = "http://www.hepsiburada.com/prima-bebek-bezi-aktif-bebek-aylik-" \
                   "plus-paket-5-beden-p-ZYPYON7376120-yorumlari?sayfa=%s"
        page_lis = response.xpath("//*[@id='pagination']/ul/li/a/text()").extract()
        for page in range(1, int(page_lis[-1]) + 1):
            yield scrapy.Request(base_url % page, callback=self.parse_page)

    def parse_page(self, response):
        unicode(response.body.decode(response.encoding)).encode('utf-8')
        review = Review()
        review['product_name'] = response.xpath("//*[@class='name']/h1/text()").extract()[0]
        for r in response.xpath("//*[@id='reviews']/li"):
            subject = r.xpath("strong[@class='subject']/text()").extract()
            if len(subject):
                subject = subject[0]
                subject = subject.replace('\n', '')
                subject = subject.replace('\r', '')
                review['subject'] = subject.strip().encode('utf8')
            else:
                review['subject'] = ""
            text = r.xpath("p[@class='review-text']/text()").extract()
            if len(text):
                text = text[0]
                text = text.replace("\n", "")
                text = text.replace("\r", "")
                review['text'] = text.strip().encode('utf8')
            else:
                review['text'] = ""
            yield review
