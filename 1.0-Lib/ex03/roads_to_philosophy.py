import sys
import requests
from bs4 import BeautifulSoup


def search_link_in_paragraphs(paragraphs):

    for p in paragraphs:
        parentheses = 0

        for element in p.descendants:

            if element.name is None:
                text = str(element)

                parentheses += text.count("(")
                parentheses -= text.count(")")

            elif element.name == "a":
                href = element.get("href")

                if not href:
                    continue

                if href.startswith("#"):
                    continue

                if not href.startswith("/wiki/"):
                    continue

                if ":" in href:
                    continue

                if element.find_parent("i") or element.find_parent("em"):
                    continue

                if parentheses == 0:
                    return href


def get_content_paragraphs(title):

    base_url = "https://en.wikipedia.org/wiki/"

    headers = {
        "User-Agent": "wikipedia-script/1.0"
    }

    title = title.replace(" ", "_")

    url = base_url + title

    res = requests.get(url, headers=headers)

    if res.status_code != 200:
        raise Exception("Request failed")

    soup = BeautifulSoup(res.text, "html.parser")

    content = soup.find("div", {"id": "mw-content-text"})
    paragraphs = content.find_all("p")

    title_tag = soup.find("h1")
    real_title = title_tag.get_text()

    return paragraphs, real_title


def main():
    if len(sys.argv) != 2:
        raise Exception("Invalid number of arguments")

    link_list = []

    title = sys.argv[1]

    title = title.replace(" ", "_")

    while True:

        paragraphs, real_title = get_content_paragraphs(title)

        if real_title in link_list:
            for link in link_list:
                print(link)
            print("It leads to an infinite loop !")
            return

        link_list.append(real_title)

        next_link = search_link_in_paragraphs(paragraphs)

        if not next_link:
            for link in link_list:
                print(link)
            print("It leads to a dead end !")
            return

        next_link = next_link.replace("/wiki/", "")
        next_link = next_link.replace("_", " ")

        if next_link == "Philosophy":
            link_list.append(next_link)
            for link in link_list:
                print(link)
            print(len(link_list), "roads from", link_list[0], "to philosophy")
            return

        title = next_link


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e.args[0])
        sys.exit(1)
