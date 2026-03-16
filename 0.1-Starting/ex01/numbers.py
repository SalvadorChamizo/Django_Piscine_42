def print_numbers(numbers):
    for number in numbers:
        print(number)


def open_file():
    with open("numbers.txt", "r") as file:
        data = file.read()
    number_list = [int(i) for i in data.split(',')]
    print_numbers(number_list)


if __name__ == '__main__':
    open_file()
