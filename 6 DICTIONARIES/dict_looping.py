# Looping Through All the Keys in a Dictionary

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}
for name in favorite_languages.keys(
):  # The keys() method is useful when you don’t need to work with all of the values in a dictionary
    print(name.title())
print()

# Looping through the keys is actually the default behavior when looping through a dictionary
for name in favorite_languages:
    print(name.title())

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(f'Hii, {name.title()}')
    if name in friends:
        language = favorite_languages[name].title()
        print(f'\t{name.title()}, I see you love {language}!')
