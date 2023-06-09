# Online_Library


## Описание работы скрипта:

Скрипт генерирует страницы сайта онлайн библиотеки ([Online_Library](https://pavelkolotov.github.io/Online_Library/pages/index1.html)) на основании ресурсов и данных, полученных с сайта 
 [tululu.org](https://tululu.org) с помощью [ParseOnlineLibrary](https://github.com/PavelKolotov/ParseOnlineLibrary).

## Как установить

Python3 должен быть уже установлен.

Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:

```
pip install -r requirements.txt
```

## Использование скрипта

- Используйте файлы полученные с помощью скрипта  [ParseOnlineLibrary](https://github.com/PavelKolotov/ParseOnlineLibrary), а именно:
  * файл `book_descriptions.json` необходимо поместить в каталог `media` (при использовании аргумента -j можно изменить путь к файлу)
  * файлы с изображением обложек и тексты книг в каталогах `images` и `books`, в папку `media` соответственно
  

- Запустите скрипт:
  * ```python render_website.py``` по умолчанию используется каталог `media`
  * ```python render_website.py -f path``` path - название каталога, где находится файл `book_descriptions.json`

В результате выполнения скрипта в каталог `pages` создадутся страницы сайта и запустится локальный сервер.
Для просмотра сайта перейдите по ссылке [http://127.0.0.1:5500/](http://127.0.0.1:5500/)

## Локальный сайт

Для работы с библиотекой в режиме офлайн, в папке pages запустите файл `index1.html` 