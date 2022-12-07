import requests
from bs4 import BeautifulSoup

class Product():
    def __init__(self):
        self.base_url = "https://freebiesglobal.com/"

    def __find_product_link_from_main(self):
        url = self.base_url+"category/turkish"
        req = requests.get(url=url)
        res = req.content
        soup = BeautifulSoup(res, "html.parser")
        product_links_list = []
        product_url_list_from_main = soup.find_all("a", class_="img-centered-flex rh-flex-center-align rh-flex-justify-center")
        for products in product_url_list_from_main:
            product_links_list.append((str(products).split('"')[3]))
        return (product_links_list)
           

    def find_product(self):
        url = self.__find_product_link_from_main()
        rep = 0
        for urls in url:
            rep +=1
            req = requests.get(url=urls)
            res = req.content
            soup = BeautifulSoup(res, "html.parser")
            product_name = soup.find("span", class_="current").get_text()
            product_date_time_post = soup.find("div", class_="date_time_post").get_text()
            try:
                soup.find("span", class_="rh-expired-notice").get_text() == "Expired"
                product_is_expired = True
            except:
                product_is_expired = False
            product_link = str(soup.find("a", class_="re_track_btn btn_offer_block")).split('"')[3]
            print (f"{rep})Name:{product_name}\nRelease date:{product_date_time_post}\nIs expired:{product_is_expired}\nLink:{product_link}\n")

    def run(self):
        if __name__ == "__main__":
            self.find_product()

Product().run()
