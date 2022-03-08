voters_count = int(input())

dict_genres = {"Horror": {"name": "Horror", "count":0}, "Romance": {"name": "Romance", "count":0}, "Comedy": {"name": "Comedy", "count":0},
               "History": {"name": "History", "count":0}, "Adventure": {"name": "Adventure", "count":0}, "Action": {"name": "Action", "count":0}}

for i in range(0, voters_count):
    vouter_input = input()
    vouter_generes = vouter_input.split(" ")[1:]

    for genere in vouter_generes:
        if genere in dict_genres:
            dict_genres[genere]["count"] += 1

result = sorted(dict_genres.items(), key=lambda x: (-x[1]["count"], x[1]["name"]))

for i in result:
    print(i[1]["name"] + " : " + str(i[1]["count"]))
