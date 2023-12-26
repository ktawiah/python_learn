def add_new_country(country_name, number_of_times_visited, cities_been_to):
    travel_log = []
    travel_log.append(
        {
            "country": country_name,
            "visits": number_of_times_visited,
            "cities": cities_been_to,
        }
    )
    return travel_log


print(add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"]))
