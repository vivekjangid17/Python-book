'''6-11. Cities: Make a dictionary called cities. Use the names of three cities as keys in your dictionary. Create a dictionary of information about each city and include the country that the city is in, its approximate population, and one fact about that city. The keys for each city's dictionary should be something like country, population, and fact. Print the name of each city and all of the information you have stored about it.'''

cities = {
    'delhi': {
        'country': 'India',
        'population': '32 million',
        'fact': 'It is the capital of India and home to India Gate.'
    },
    'mumbai': {
        'country': 'India',
        'population': '20 million',
        'fact': 'It is the financial capital of India and home to Bollywood.'
    },
    'jaipur': {
        'country': 'India',
        'population': '3.1 million',
        'fact': 'Known as the Pink City and famous for its palaces and forts.'
    }
}

# print(cities)  # print the whole dictionary

for key, value in cities.items():
    print(key.title())              # print the key of outer dict
    for i,j in value.items():
        print(f"\t{i}: {j}")        # print the inner dict
