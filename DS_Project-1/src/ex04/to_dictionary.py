def create_list_of_tuples():
    list_of_tuples = [
        ('Russia', '25'),
        ('France', '132'),
        ('Germany', '132'),
        ('Spain', '178'),
        ('Italy', '162'),
        ('Portugal', '17'),
        ('Finland', '3'),
        ('Hungary', '2'),
        ('The Netherlands', '28'),
        ('The USA', '610'),
        ('The United Kingdom', '95'),
        ('China', '83'),
        ('Iran', '76'),
        ('Turkey', '65'),
        ('Belgium', '34'),
        ('Canada', '28'),
        ('Switzerland', '26'),
        ('Brazil', '25'),
        ('Austria', '14'),
        ('Israel', '12')
    ]
    return list_of_tuples


def output_country_dict(country_dict: dict):
    for number, countries in country_dict.items():
        for country in countries:
            print(f"'{number}' : '{country}'")


def to_dictionary(list_of_tuples: list):
    country_dict = {}
    for country, number in list_of_tuples:
        if number not in country_dict:
            country_dict[number] = []
        country_dict[number].append(country)

    return country_dict


if __name__ == "__main__":
    list_of_tuples = create_list_of_tuples()
    country_dict = to_dictionary(list_of_tuples)
    output_country_dict(country_dict)
