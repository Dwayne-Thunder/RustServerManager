# RustServerManager for Windows
A tool designed to Install, Update, Auto start RUST servers!

RustServerManager is a extremely light-weight, simplistic & efficient Wrapper for RUST servers hosted on Windows.

Это нада:
  - Python 3.9+
  - Python added to system path

Че могёт:
  - Auto установка (Game files, Oxide, Rust Edit).
  - Auto обновление (Game files, Oxide, Rust Edit).
  - Перезапуск при падении всего дерьма.

Установка:
  - Качаем здесь либо `https://github.com/8qBITs/RustServerManager/releases`
  - Создаем отдельную папку для сервера, кидаем туды файлы.
  - Прессуем `start.bat`
  - Усё!
 
Настройка:
  - Параметры запуска сервера тут: 'rust_data/config.cfg'
  - Для авто рестарта разраб рекомендует https://umod.org/plugins/smooth-restarter
  - If you are running vanilla (community) server make sure to set 'modded' to false inside oxide config!
  - Make sure to restart server after changing any startup parameters!
 
Troubleshooting:
  - Nothing happens after starting start.bat:
     - *1. No python3 installed.*
        - Download it here: https://www.python.org/ftp/python/3.10.4/python-3.10.4-amd64.exe 
     - *2. No python path found.*
        - Run python using cmd with `python` if there is an error: `'python' is not recognised as an internal or external command` you haven't           set up python             path properly. Watch for fix: https://www.youtube.com/watch?v=4bUOrMj88Pc&t=351s

