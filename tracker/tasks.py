import requests
from background_task import background
from bs4 import BeautifulSoup
from django.utils import timezone

from tracker.models import Stock

url = "https://www.sashares.co.za/shares-list/"

page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')


@background(schedule=10, name="get_data")
def get_data():

    for i in range(550):

        if soup.find(id=f'table_1_row_{i}'):
            JSE_CODE = soup.find(id=f'table_1_row_{i}').find_all('td')[
                0].get_text(),
            SHARE = soup.find(id=f'table_1_row_{i}').find_all('td')[
                1].get_text(),
            PRICE = soup.find(id=f'table_1_row_{i}').find_all('td')[
                3].get_text(),
            MOVE = soup.find(id=f'table_1_row_{i}').find_all('td')[
                4].get_text(),
            MOVE_CHANGE = soup.find(id=f'table_1_row_{i}').find_all('td')[
                5].get_text(),
            MARKET_CAP = soup.find(id=f'table_1_row_{i}').find_all('td')[
                6].get_text()

            defaults = {
                'price': PRICE[0].replace(",", " "),
                'move': MOVE[0],
                'move_change': MOVE_CHANGE[0],
                'market_cap': MARKET_CAP.replace(",", " "),
                'time': timezone.now()
            }

            Stock.objects.update_or_create(
                jse_code=JSE_CODE[0],
                share=SHARE[0],
                defaults=defaults
            )

        else:
            break
