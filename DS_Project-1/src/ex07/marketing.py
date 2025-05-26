import sys


def create():
    # адреса электронной почты ваших клиентов
    clients = ['andrew@gmail.com', 'jessica@gmail.com', 'ted@mosby.com',
               'john@snow.is', 'bill_gates@live.com', 'mark@facebook.com',
               'elon@paypal.com', 'jessica@gmail.com']
    # адреса электронной почты участников вашего последнего мероприятия
    participants = ['walter@heisenberg.com', 'vasily@mail.ru',
                    'pinkman@yo.org', 'jessica@gmail.com', 'elon@paypal.com',
                    'pinkman@yo.org', 'mr@robot.gov', 'eleven@yahoo.com']
    # адреса электронной почты ваших клиентов, которые просматривали ваше последнее рекламное письмо.
    recipients = ['andrew@gmail.com', 'jessica@gmail.com', 'john@snow.is']

    return clients, participants, recipients


def marketing(task: str):
    clients, participants, recipients = create()

    if task == "call_center":
        result = set(clients) - set(recipients)
        print(
            f"Cписок клиентов, которые ещё не получили рекламное письмо {result}")

    elif task == "potential_clients":
        result = set(participants) - set(clients)
        print(
            f"Cписок участников, которые не являются вашими клиентами {result}")

    elif task == "loyalty_program":
        result = set(clients) - set(participants)
        print(
            f"Cписок клиентов, которые не участвовали в мероприятии {result}")


if __name__ == "__main__":
    if len(sys.argv) == 2:
        marketing(sys.argv[1])
    else:
        pass
