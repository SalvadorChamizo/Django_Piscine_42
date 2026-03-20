class Intern:
    def __init__(self, name=None):

        if name:
            self.name = name
        else:
            self.name = "My name? I'm nobody, an intern, I have no name."

    def __str__(self):
        return self.name

    def work(self):
        raise Exception("I´m just an intern, I can´t do that...")

    def make_coffee(self):
        return Coffee()


class Coffee:
    def __str__(self):
        return "This is the worst coffee you ever tasted."


def main():
    intern = Intern()
    mark = Intern("Mark")

    print(intern)
    print(mark)

    mark_coffee = mark.make_coffee()
    print(mark_coffee)

    try:
        intern.work()
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
