from bs4 import BeautifulSoup
import httplib2

http = httplib2.Http()

city_name = input('Enter with the city name')
currency = input('Enter with the currency of the price').upper()

def get_cost_living_data(city):
    city_arr = city.split(' ')
    city_arr = list(map(lambda word: word.capitalize(), city_arr))
    city = '-'.join(city_arr)

    url = 'https://www.numbeo.com/cost-of-living/in/' + city + '?displayCurrency='+currency
    status, response = http.request(url)
    soup = BeautifulSoup(response, "html.parser")
    '''test_soup = soup.find_all(attrs={"id": 'displayCurrency'})'''
    all_tds = soup.find_all('td')

    get_meal_price(all_tds)
    get_market_prices(all_tds)

def get_meal_price(tds):

    domestic_beer = False

    for ind, td in enumerate(tds):
        if 'Meal, Inexpensive' in td.text:
            print('Usual meal in unexpensive restaurant: '+ tds[ind + 1].text)

        if 'McDonalds' in td.text:
            print('McMeal Combo price: '+ tds[ind + 1].text)

        if 'Domestic Beer' in td.text and domestic_beer == False:
            domestic_beer = True
            print('Domestic beer in restaurant: '+ tds[ind + 1].text)


def get_market_prices(tds):

    water_bottle = False

    for ind, td in enumerate(tds):
        if 'Milk' in td.text:
            print('Milk price: '+ tds[ind + 1].text)

        if 'Rice' in td.text:
            print('Rice price: '+ tds[ind + 1].text)

        if 'Potato' in td.text:
            print('Potato price: '+ tds[ind + 1].text)

        if 'Water' in td.text:
            if water_bottle == True:
                print('1.5L bottle of water price: '+ tds[ind + 1].text)
            water_bottle = not water_bottle

get_cost_living_data(city_name)
