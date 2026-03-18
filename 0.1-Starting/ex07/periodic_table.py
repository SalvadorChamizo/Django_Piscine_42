import sys


def create_html(elements):

    ROWS = 7
    COLS = 18

    html = ""

    html += "<!DOCTYPE html>\n"
    html += "<html lang=\"en\">\n"
    html += "<head>\n"
    html += "<meta charset=\"UTF-8\">\n"
    html += "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n"
    html += "<title>Periodic Table</title>\n"
    html += "<link rel=\"stylesheet\" href=\"periodic_table.css\">\n"
    html += "</head>\n"
    html += "<body>\n"
    html += "<table>\n"

    for r in range(ROWS):

        html += "<tr>\n"

        for c in range(COLS):

            if (r, c) in elements:
                e = elements[(r, c)]

                num = int(e["number"])
                if num in [1, 6, 7, 8, 15, 16, 34]:
                    cls = "nonmetal"
                elif num in [3, 11, 19, 37, 55, 87]:
                    cls = "alkalai"
                elif num in [4, 12, 20, 38, 56, 88]:
                    cls = "alkaline_earth"
                elif num in [2, 10, 18, 36, 54, 86, 118]:
                    cls = "noble_gas"
                elif num in [5, 14, 32, 33, 51, 52, 84]:
                    cls = "metalloid"
                elif num in [13, 31, 49, 50, 81, 82, 83, 113, 114, 115, 116]:
                    cls = "post_metal"
                elif num in [9, 17, 35, 53, 85, 117]:
                    cls = "halogen"
                else:
                    cls = "metal"

                html += f"<td class=\"{cls}\">\n"
                html += "<h4>" + e["name"] + "</h4>\n"
                html += "<ul>\n"
                html += "<li>No " + e["number"] + "</li>\n"
                html += "<li>" + e["symbol"] + "</li>\n"
                html += "<li>" + e["mass"] + "</li>\n"
                html += "<li>" + e["electron"] + "</li>\n"
                html += "</ul>\n"
                html += "</td>\n"
            else:
                html += "<td></td>\n"

        html += "</tr>\n"

    html += "</table>\n"
    html += "</body>\n"
    html += "</html>\n"

    with open("periodic_table.html", "w") as f:
        f.write(html)


def periodic_table():
    elements = {}

    row = 0
    prev_col = -1

    with open("periodic_table.txt", "r") as file:

        for line in file:
            line = line.strip()
            if not line:
                continue
                
            if "=" not in line:
                continue

            element = {}

            name, rest = line.split(" = ")
            element["name"] = name

            parts = rest.split(",")

            for part in parts:
                key, value = part.split(":")
                key = key.strip()
                value = value.strip()
                if key == "position":
                    col = int(value)

                    if col <= prev_col:
                        row += 1
                    prev_col = col

                elif key == "number":
                    element["number"] = value
                elif key == "small":
                    element["symbol"] = value
                elif key == "molar":
                    element["mass"] = value
                elif key == "electron":
                    element["electron"] = value

            elements[(row, col)] = element

    create_html(elements)


if __name__ == '__main__':
    periodic_table()
