travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]


def add_new_county(country, count, visit):
    my_data = {
        "country": country,
        "visits": count,
        "cities": visit
    }

    travel_log.append(my_data)


add_new_county("Russia", 2, ["Moscow", "saint Petersburg"])
print(travel_log[2])
