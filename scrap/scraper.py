import requests
from parsel import Selector


class NewsScraper:
    # PLUS_URL = 'https://24.kg'
    URL = 'https://24.kg/'
    HEADERS = {
        "Accept-Language":
            "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0"
    }

    LINK_XPATH = '//div[@class="title"]/a/@href'

    def scrape_data(self):
        response = requests.request(method="GET", url=self.URL, headers=self.HEADERS)
        tree = Selector(text=response.text)
        fresh_links = tree.xpath(self.LINK_XPATH).getall()
        links = [i for i in fresh_links if i.startswith('https://24.kg/')]
        return_data = []
        for i in range(0, len(links)):
            data = {}
            data['link'] = links[i]
            return_data.append(data)
        return return_data

if __name__ == "__main__":
    scraper = NewsScraper()
    print(scraper.scrape_data())

