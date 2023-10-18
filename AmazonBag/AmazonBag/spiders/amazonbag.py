import scrapy


class AmazonbagSpider(scrapy.Spider):
    name = "amazonbag"
    #allowed_domains = ["example"]
    start_urls = ["https://www.amazon.in/s?k=bags&crid=2M096C61O4MLT&qid=1653308124&sprefix=ba%2Caps%2C283&ref=sr_pg_1"]

    count=1
    def parse(self, response):
        #ProUrl=response.css("h2.a-size-mini a-spacing-none a-color-base s-line-clamp-2 a").xpath("@href").extract()
        ProUrl=response.xpath("(//h2/a)/@href").extract()
        ProName=response.css(".a-color-base.a-text-normal::text").extract()
        ProPrice=response.css(".a-price-whole::text").extract()
        ProRating=response.css(".a-icon-alt::text").extract()
        ProNoReview=response.css(".s-link-style .s-underline-text::text").extract()
        yield {"ProUrl":ProUrl,
               "ProName":ProName,
               "ProPrice":ProPrice,
               "ProRating":ProRating,
               "ProNoReview":ProNoReview
               }
        AmazonbagSpider.count+=1
                  
        nxt_page= "https://www.amazon.in/s?k=bag&page="+str(AmazonbagSpider.count)+"&qid=1697648130&sprefix=bag%2Caps%2C269&ref=sr_pg_1"
        
        if AmazonbagSpider.count<30:
            yield response.follow(nxt_page,callback=self.parse)

        


        
