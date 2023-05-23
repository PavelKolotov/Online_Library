import json
import os
import math

from jinja2 import Environment, FileSystemLoader, select_autoescape
from livereload import Server
from more_itertools import chunked


BOOKS_PER_PAGE = 10
BOOK_COLUMNS = 2


def on_reload():
    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html'])
    )
    template = env.get_template('template.html')

    with open("media/book_descriptions.json", "r") as file:
        books_json = file.read()
    book_descriptions = json.loads(books_json)
    book_descriptions_per_page = list(chunked(book_descriptions, BOOKS_PER_PAGE))
    pages_count = math.ceil(len(book_descriptions)/BOOKS_PER_PAGE)
    for id, books in enumerate(book_descriptions_per_page, start=1):
        books_for_page = list(chunked((books), BOOK_COLUMNS))
        rendered_page = template.render(
            book_descriptions=books_for_page,
            pages_count=pages_count,
            number_page=id
        )
        os.makedirs('pages', exist_ok=True)
        with open(f'pages/index{id}.html', 'w', encoding="utf8") as file:
            file.write(rendered_page)


def main():
    on_reload()

    server = Server()
    server.watch('template.html', on_reload)
    server.serve(root='.', default_filename='pages/index1.html')


if __name__ == '__main__':
    main()
