import sys
import os
import settings


def render_template(filename):
    with open(filename, "r") as f:
        content = f.read()

    variables = vars(settings)

    for key, value in variables.items():
        content = content.replace("{" + key + "}", str(value))

    # Using variable expansion
    # try:
    #     content = content.format(**variables)
    # except KeyError as e:
    #     print(f"Missing variable: {e}")
    #     return

    output = filename.replace(".template", ".html")

    with open(output, "w") as f:
        f.write(content)


def main():
    if len(sys.argv) != 2:
        print("Error")
        return

    filename = sys.argv[1]

    if not filename.endswith(".template"):
        print("Error")
        return

    if not os.path.isfile(filename):
        print("Error")
        return

    render_template(filename)


if __name__ == '__main__':
    main()
