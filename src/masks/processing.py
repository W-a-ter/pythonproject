def filter_by_state(inform: list, state="EXECUTED") -> list[str]:
    """функция, которая принимает на вход список словарей"""

    my_list = []

    for i in inform:
        if i["state"] == state:
            my_list.append(i)

    return my_list


def sort_by_date(info: list, date=True) -> list[str]:
    """функция, которая принимает на вход список словарей"""

    sorted_list = sorted(info, key=lambda x: x["date"])
    return sorted_list
