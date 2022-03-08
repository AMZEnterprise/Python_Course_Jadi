import requests
from bs4 import BeautifulSoup
import mysql.connector
from sklearn import tree


class Car:
    def __init__(self, name, year, mileage, location, price):
        self.name = name
        self.year = year
        self.mileage = mileage
        self.location = location
        self.price = price


def get_page(url):
    response = requests.get(url)
    return response.text


def get_cars(page):
    cars = []

    bs = BeautifulSoup(page, "html.parser")
    car_cards = bs.find_all("div", class_="vehicle-card-body")
    car_cards = car_cards[:20]

    for card in car_cards:

        name = card.find("div", {"data-test": "vehicleCardTrim"}).text.strip()
        year = card.find("span", class_="vehicle-card-year").text.strip()
        mileage = (
            card.find("div", {"data-test": "vehicleMileage"})
            .text.replace("miles", "").replace(",", "")
            .strip()
        )
        location = (
            card.find("div", {"data-test": "vehicleCardLocation"})
            .text
            .split(",")[1]
            .strip()
        )  # get only the state name
        price = (
            card.find("div", {"data-test": "vehicleCardPricingBlockPrice"})
            .text.replace("$", "").replace(",", "")
            .strip()
        )

        cars.append(Car(name, year, mileage, location, price))
    return cars


def save_cars_to_db(cars):
    cnx = mysql.connector.connect(
        user="root", password="", host="127.0.0.1", database="cars"
    )
    cursor = cnx.cursor()

    for car in cars:
        insert_query = "INSERT INTO info (name, year, mileage, location, price) VALUES (%s, %s, %s, %s, %s)"
        record = (car.name, car.year, car.mileage, car.location, car.price)
        cursor.execute(insert_query, record)
        cnx.commit()

    print("Cars saved successfully")


def get_cars_from_db():
    cnx = mysql.connector.connect(
        user="root", password="", host="127.0.0.1", database="cars"
    )
    cursor = cnx.cursor()

    query = "SELECT * FROM info"
    cursor.execute(query)

    cars = []
    for (name, year, mileage, location, price) in cursor:
        cars.append(Car(name, year, mileage, location, price))

    return cars


brand_name = input("Enter brand name: ") #ex : alfa-romeo
url = "https://www.truecar.com/used-cars-for-sale/listings/" + brand_name + "/"

cars = []

for i in range(1, 20):
    if i >= 2:
        url = (
            "https://www.truecar.com/used-cars-for-sale/listings/"
            + brand_name
            + "/?page="
            + str(i)
        )

    page = get_page(url)

    result_cars = get_cars(page)

    if (
        len(result_cars) == 0
    ):  # When there is no more car on the page (or pages finished)
        break
    
    for car in result_cars:
        cars.append(car)

save_cars_to_db(cars)



# Machine learning

print("Training started...")
def get_machine_learning_data(cars):
    X = []
    y = []

    for car in cars:
        X.append([car.year, car.mileage])
        y.append(car.price)

    return X, y


X, y = get_machine_learning_data(cars)
cars = get_cars_from_db()

clf = tree.DecisionTreeClassifier()
clf = clf.fit(X, y)

year = int(input("Enter car year: "))
mileage = int(input("Enter car mileage: "))
answer = clf.predict([[year, mileage]])
print("Predicted price: " + str(answer[0]))
