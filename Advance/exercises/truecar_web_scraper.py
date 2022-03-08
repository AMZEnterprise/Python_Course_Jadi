import requests
from bs4 import BeautifulSoup
import mysql.connector

class Car:
    def __init__(self, price,mileage):
        self.price = price
        self.mileage = mileage
    

def get_page(url):
    response = requests.get(url)
    return response.text

def get_cars(page):
    cars = []

    bs = BeautifulSoup(page, 'html.parser')
    car_cards = bs.find_all('div', class_='vehicle-card-body')
    car_cards = car_cards[:20]
   
    for card in car_cards:
        price = card.find('div',{"data-test":"vehicleCardPricingBlockPrice"}).text.replace('$','').strip()
        mileage = card.find('div',{"data-test":"vehicleMileage"}).text.replace('miles','').strip()
        cars.append(Car(price, mileage))

    return cars

def save_cars_to_db(cars):
    cnx = mysql.connector.connect(user='root', password='',
                              host='127.0.0.1',
                              database='cars')
    cursor = cnx.cursor()

    for car in cars:
        insert_query = "INSERT INTO info (price, mileage) VALUES (%s, %s)"
        record = (car.price, car.mileage)
        cursor.execute(insert_query, record)
        cnx.commit()
    
    print("Cars saved successfully")
    

brand_name = input("Enter brand name: ")
url = 'https://www.truecar.com/used-cars-for-sale/listings/' + brand_name + '/'

page = get_page(url)
cars = get_cars(page)
save_cars_to_db(cars)