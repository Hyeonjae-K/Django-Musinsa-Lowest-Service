import django
django.setup()

import requests
from bs4 import BeautifulSoup
from functools import partial
from multiprocessing import Pool, cpu_count
from django.utils import timezone
from .models import Brands, History, Products

headers = {'User-Agent': 'Mozila/5.0'}


def _brandsCrawler(page_num, brand):
    soup = BeautifulSoup(requests.get(
        brand.url + f'?page={page_num}').text, 'html.parser')
    prices = [int(elem.text.split()[-1].replace(',', '').replace('원', ''))
              for elem in soup.select('#searchList > li > div.li_inner > div.article_info > p.price')]
    images = ['https:' + elem['data-original']
              for elem in soup.select('#searchList > li > div.li_inner > div.list_img > a > img')]
    elems = soup.select(
        '#searchList > li > div.li_inner > div.article_info > p.list_info > a')
    product_ids = [int(elem['href'].split('/')[-1]) for elem in elems]
    names = [elem['title'] for elem in elems]
    urls = ['https:' + elem['href'] for elem in elems]

    histories, update_products, new_products = [], [], []
    datetime = timezone.now()
    for price, image, product_id, name, url in zip(prices, images, product_ids, names, urls):
        history = History(product=product_id, price=price,
                          created_date=datetime)
        histories.append(history)
        try:
            product = Products.objects.get(id=product_id)
            product.current = history
            if product.lowest == None:
                product.lowest = History.objects.filter(
                    product=product_id).order_by('price')[0]
            elif product.lowest.price > history.price:
                product.lowest = history
            if product.highest == None:
                product.highest = History.objects.filter(
                    product=product_id).order_by('-price')[0]
            elif product.highest.price < history.price:
                product.highest = history
            update_products.append(product)
        except:
            product = Products(id=product_id, name=name, brand=brand, current=history, lowest=history, highest=history, url=url, image=image, created_date=datetime)
            new_products.append(product)

    History.objects.bulk_create(histories)
    if new_products:
        Products.objects.bulk_create(new_products)
    if update_products:
        Products.objects.bulk_update(update_products, ['current', 'lowest', 'highest'])


def brandsCrawler():
    brands = Brands.objects.all()
    for brand in brands:
        soup = BeautifulSoup(requests.get(brand.url).text, 'html.parser')
        last_page_num = int(soup.select_one(
            '#product_list > div.section_product_list > div > div.boxed-list-wrapper > div.thumbType_box.box > span.pagingNumber > span.totalPagingNum').text)
        pool = Pool(processes=cpu_count())
        pool.map(partial(_brandsCrawler, brand=brand), [
                 page_num for page_num in range(1, last_page_num+1)])
