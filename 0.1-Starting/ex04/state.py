import sys


def search_state():
    states = {
        "Oregon": "OR",
        "Alabama": "AL",
        "New Jersey": "NJ",
        "Colorado": "CO"
    }

    capital_cities = {
        "OR": "Salem",
        "AL": "Montgomery",
        "NJ": "Trenton",
        "CO": "Denver"
    }

    if len(sys.argv) != 2:
        return

    capital_name = sys.argv[1]

    for code, city in capital_cities.items():
        if city == capital_name:
            for state, state_code in states.items():
                if state_code == code:
                    print(state)
                    return

    print("Unknown capital city")


if __name__ == '__main__':
    search_state()
