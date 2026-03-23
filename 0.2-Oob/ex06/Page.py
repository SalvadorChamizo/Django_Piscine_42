from elem import Elem, Text
from elements import Html, Head, Body, Title, H1, Img, H2, Li, Table, Th, Tr, Td, Ul, Ol, P, Div, Hr, Br, Span, Meta

ALLOWED_TAGS = {'html', 'head', 'body', 'title', 'meta', 'img', 'table',
                'th', 'tr', 'td', 'ul', 'ol', 'li', 'h1', 'h2', 'p', 'div',
                'span', 'br', 'hr'}


class Page:
    def __init__(self, elem):
        self.element = elem

    def __str__(self):
        if self.element.tag == 'html':
            return "<!DOCTYPE html>\n" + str(self.element)
        return str(self.element)

    def write_to_file(self, filename):
        with open(filename, 'w') as f:
            f.write(str(self))

    def is_valid(self):
        return self._validate(self.element)

    def _validate(self, node):

        if isinstance(node, Text):
            return True

        if not isinstance(node, Elem):
            return False

        if node.tag not in ALLOWED_TAGS:
            return False

        if not self._check_rules(node):
            return False

        for child in node.content:
            if not self._validate(child):
                return False

        return True

    def _check_rules(self, node):
        tag = node.tag
        children = node.content

        if tag == 'html':
            if len(children) != 2:
                return False
            return children[0].tag == 'head' and children[1].tag == 'body'

        if tag == 'head':
            if len(children) != 1:
                return False
            if children[0].tag != 'title':
                return False
            return True

        if tag == 'body' or tag == 'div':
            allowed = {'h1', 'h2', 'div', 'table', 'ul', 'ol', 'span'}
            for c in children:
                if not (isinstance(c, Text) or (isinstance(c, Elem) and c.tag in allowed)):
                    return False
            return True

        if tag == 'title' or tag == 'h1' or tag == 'h2' or tag == 'li' or tag == 'th' or tag == 'td':
            if len(children) != 1:
                return False
            if isinstance(children[0], Text):
                return True
            else:
                return False

        if tag == 'p':
            for c in children:
                if not isinstance(c, Text):
                    return False
            return True

        if tag == 'span':
            for c in children:
                if not (isinstance(c, Text) or (isinstance(c, Elem) and c.tag == 'p')):
                    return False
            return True

        if tag == 'ul' or tag == 'ol':
            if len(children) < 1:
                return False
            for c in children:
                if not c.tag == 'li':
                    return False
            return True

        if tag == 'tr':
            if len(children) < 1:
                return False
            if children[0].tag == 'th':
                for c in children:
                    if not c.tag == 'th':
                        return False
            elif children[0].tag == 'td':
                for c in children:
                    if not c.tag == 'td':
                        return False
            else:
                return False
            return True

        if tag == 'table':
            if len(children) == 0:
                return False
            for c in children:
                if not c.tag == 'tr':
                    return False
            return True
        return True


if __name__ == '__main__':

    print("Valid minimal page")

    page = Html([
        Head(Title(Text("Hello"))),
        Body([
            H1(Text("Hi"))
        ])
    ])

    print(Page(page).is_valid())

    print("Invalid: wrong order in html")

    page = Html([
        Body([]),
        Head(Title(Text("Hello")))
    ])

    print(Page(page).is_valid())

    print("Invalid: head with no title")

    page = Html([
        Head([]),
        Body([])
    ])

    print(Page(page).is_valid())

    print("Invalid: head with extra element (Meta)")

    page = Html([
        Head([
            Title(Text("Hello")),
            Meta(attr={"charser": "UTF-8"})
        ]),
        Body([])
    ])

    print(Page(page).is_valid())

    print("Invalid: multiple titles")

    page = Html([
        Head([
            Title(Text("Hello")),
            Title(Text("World"))
        ]),
        Body([])
    ])

    print(Page(page).is_valid())

    print("Invalid: H1 with multiple Text")

    page = Html([
        Head(Title(Text("Hello"))),
        Body([
            H1([Text("A"), Text("B")])
        ])
    ])

    print(Page(page).is_valid())

    print("Invalid: P containing element")

    page = Html([
        Head(Title(Text("Hello"))),
        Body([
            P([
                Text("Hello"),
                Div()
            ])
        ])
    ])

    print(Page(page).is_valid())

    print("Valid: span with text and p")

    page = Html([
        Head(Title(Text("Hello"))),
        Body([
            Span([
                Text("Hi"),
                P(Text("Paragraph"))
            ])
        ])
    ])

    print(Page(page).is_valid())

    print("Invalid: span with div")

    page = Html([
        Head(Title(Text("Hello"))),
        Body([
            Span([
                Div()
            ])
        ])
    ])

    print(Page(page).is_valid())

    print("Invalid: ul without li")

    page = Html([
        Head(Title(Text("Hello"))),
        Body([
            Span([
                Div()
            ])
        ])
    ])

    print(Page(page).is_valid())

    print("Invalid: ul with wrong child")

    page = Html([
        Head(Title(Text("Hello"))),
        Body([
            Ul([
                Div()
            ])
        ])
    ])

    print(Page(page).is_valid())

    print("Valid: table with td")

    page = Html([
        Head(Title(Text("Hello"))),
        Body([
            Table([
                Tr([
                    Td(Text("A")),
                    Td(Text("B"))
                ])
            ])
        ])
    ])

    print(Page(page).is_valid())

    print("Invalid: tr mixing th and td")

    page = Html([
        Head(Title(Text("Hello"))),
        Body([
            Table([
                Tr([
                    Td(Text("A")),
                    Th(Text("B"))
                ])
            ])
        ])
    ])

    print(Page(page).is_valid())

    print("Invalid: unknown tag")

    fake = Elem(tag='fake')

    page = Html([
        Head(Title(Text("Hello"))),
        Body([fake])
    ])

    print(Page(page).is_valid())

    print("Valid: deep nesting")

    page = Html([
        Head(Title(Text("Hello"))),
        Body([
            Div([
                Div([
                    H2(Text("Nested"))
                ])
            ])
        ])
    ])

    print(Page(page).is_valid())

    print("Print page:\n")
    print(page)

    Page(page).write_to_file("test.html")
