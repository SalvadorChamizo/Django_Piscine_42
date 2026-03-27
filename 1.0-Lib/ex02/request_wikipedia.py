import requests
import json
import sys
from dewiki import from_string


def get_title(query):
    url = "https://en.wikipedia.org/w/api.php"

    params = {
        "action": "query",
        "list": "search",
        "srsearch": query,
        "format": "json"
    }

    headers = {
        "User-Agent": "wikipedia-script/1.0"
    }

    res = requests.get(url, params=params, headers=headers)

    if res.status_code != 200:
        raise Exception("API request failed")

    data = res.json()

    if not data["query"]["search"]:
        raise Exception("No results found")

    return data["query"]["search"][0]["title"]


def search_content(title):

    url = "https://en.wikipedia.org/w/api.php"

    params = {
        "action": "query",
        "format": "json",
        "prop": "extracts",
        "titles": title,
        "explaintext": True,
    }

    headers = {
        "User-Agent": "wikipedia-script/1.0"
    }

    res = requests.get(url, params=params, headers=headers)

    if res.status_code != 200:
        raise Exception("API request failed")

    data = res.json()

    pages = data["query"]["pages"]

    page = next(iter(pages.values()))

    if "extract" not in page or not page["extract"]:
        raise Exception("No content found")

    return page["extract"]


def main():
    try:
        if len(sys.argv) != 2:
            raise Exception("Invalid number of arguments")

        title = get_title(sys.argv[1])
        content = search_content(title)

        content = from_string(content)

        filename = title.replace(" ", "_") + ".wiki"

        with open(filename, "w", encoding="utf-8") as f:
            f.write(content)

    except Exception as e:
        print(e.args)
        sys.exit(1)


if __name__ == '__main__':
    main()
