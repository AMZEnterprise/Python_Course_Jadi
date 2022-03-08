import requests
from bs4 import BeautifulSoup

url = "https://divar.ir/s/tehran"

res = requests.get(url)

if res.status_code == 200:
    soup = BeautifulSoup(res.text, "html.parser")
    
    post_cards = soup.find_all("div", class_="post-card-item")

    filtered_post_cards = []

    for post_card in post_cards:
        desc = post_card.find("div", class_="kt-post-card__description")
        if desc is not None:
            if desc.get_text() == "توافقی":
                filtered_post_cards.append(post_card)

    for post_card in filtered_post_cards:
        print(post_card.find("div", class_="kt-post-card__title").get_text())

else:
    print("Error")