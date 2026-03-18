import sys


def split_argument(str_arg):
    word_list = [str(i) for i in str_arg.split(',')]

    return word_list


def search_city(word, capital_cities, states):

    for state, code in states.items():
        if state.lower() == word:
            capital = capital_cities[code]

            print(capital + " is the capital of " + state)
            return 0

    return 1


def search_state(word, capital_cities, states):

    for code, city in capital_cities.items():
        if city.lower() == word:
            for state, state_code in states.items():
                if state_code == code:
                    print(city + " is the capital of " + state)
                    return 0

    return 1


def all_in():
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

    word_list = split_argument(sys.argv[1])

    for raw_word in word_list:

        word = raw_word.strip().lower()
        if word == "":
            continue

        if (search_city(word, capital_cities, states)):
            if (search_state(word, capital_cities, states)):
                print(raw_word.strip() + " is neither a capital city nor a state")


if __name__ == '__main__':
    all_in()
