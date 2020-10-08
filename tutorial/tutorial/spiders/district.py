# -*- coding: utf-8 -*-
import scrapy
from transliterate import translit, get_available_language_codes


class Spyder(scrapy.Spider):
    name = "spyder_district"
    allowed_domains = ['indicators.miccedu.ru']
    _start_url = 'http://indicators.miccedu.ru/monitoring/2019/'
    start_urls = ['http://indicators.miccedu.ru/monitoring/2019/index.php?m=vpo']
    # allowed_domains = ['https://www.uni-dubna.ru/abitur']
        

    def parse(self, response):
        all_federal_district = response.xpath('//p[@class="MsoListParagraph"]')
        # print(all_federal_district)
        for fd in all_federal_district:

            fd_text = fd.xpath('.//a/text()').extract_first()
            fd_href = self._start_url + fd.xpath('.//a/@href').extract_first()

            yield {
                'Name': translit(fd_text, 'ru', reversed=True),
                'Href': fd_href,
            }



        
        

        
        



       