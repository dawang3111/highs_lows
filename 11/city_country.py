def get_city_country(city, country, population=''):
    if population:
        return city + "," + country + "-population: "+str(population)
    else:
        return city + "," + country


country = 'China'
city = 'Beijing'
population = 22000000
sentence = get_city_country(city, country, population)
print(sentence)
