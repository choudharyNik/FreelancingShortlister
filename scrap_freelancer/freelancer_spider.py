import scrapy
from scrapy.crawler import CrawlerProcess

class FreelanceSpider(scrapy.Spider):
    name = "freelancespider"
    jobs = []

    def __init__(self, skillset='Python', min_price=100, *args, **kwargs):
        super(FreelanceSpider, self).__init__(*args, **kwargs)
        self.start_urls = [
            f'https://www.freelancer.com/jobs/{skillset.lower().replace(" ", "-")}/'
        ]
        self.min_price = min_price

    def parse(self, response):
        # Extracting each job card on the page
        job_cards = response.css("div.JobSearchCard-item-inner")
        for job_card in job_cards:
            # Extracting title, description, and price of each job
            title = job_card.css("a.JobSearchCard-primary-heading-link::text").get()
            description = job_card.css("p.JobSearchCard-primary-description::text").get()
            price = str(job_card.css("div.JobSearchCard-secondary-price::text").get())

            if 'None' in price:
                continue
            else:
                price = price.split()[0].replace('$', '')

            if title and description and price:

                if self.min_price is None or int(price) >= int(self.min_price):
                    self.jobs.append([title.strip(), description.strip(), '$'+str(price)])
    
    # def all_jobs(self):
    #     return self.jobs
process = CrawlerProcess()
process.crawl(FreelanceSpider)
process.start()