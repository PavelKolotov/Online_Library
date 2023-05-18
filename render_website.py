import json

from more_itertools import chunked

from livereload import Server

from jinja2 import Environment, FileSystemLoader, select_autoescape


def on_reload():
    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html'])
    )
    template = env.get_template('template.html')

    with open("book_descriptions.json", "r") as file:
        books_json = file.read()
        book_descriptions = json.loads(books_json)
        books = list(chunked(book_descriptions, 2))
        rendered_page = template.render(book_descriptions=books)
        with open('index.html', 'w', encoding="utf8") as file:
            file.write(rendered_page)


def main():
    on_reload()

    server = Server()
    server.watch('template.html', on_reload)
    server.serve(root='.', default_filename='index.html')


if __name__ == '__main__':
    main()
