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


def dict_sorter():
    country_dict = {country: int(number)
                    for country, number in list_of_tuples}
    country_dict = sorted(country_dict.items(),
                          key=lambda x: x[1], reverse=True)

    for key, value in country_dict:
        print(key)


if __name__ == "__main__":
    list_of_tuples = create_list_of_tuples()
    dict_sorter()
