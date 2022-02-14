# Тестовое задание для CARBIS
Описание задания: [docs.google.com](https://docs.google.com/document/d/1E_LMzWsoXW-BTZDzJ1p6w3ScKgIw5tfd7FHh-NKn1SA/edit#)

## Рабочее окружение:

Для начала разработки необходимо настроить рабочее окружение. Нам понадобятся следующие системные зависимости: 
- [python](https://www.python.org/downloads/) версии 3.9 или выше
- менеджер зависимостей [pip](https://pip.pypa.io/en/stable/installation/)

Настройка окружения:
1. Настроить репозиторий
    ```shell script
   ```
2. Подключение виртуального окружения
    ```shell script
    python3 -m venv env
    ```
3. Установить зависимости. Зависимости установятся в виртуальное окружение.
    ```shell script
   pip install -r requirements.txt   
    ```
## Запуск
1. Внесите ваш APIkey и Secretkey от Dadata API в settings.py
2. Для сохранения данных в базу данных settings.sqlite:
    ```shell script
    python settings.py
    ```
3. Запуск в консоле
   ```shell script
   python console_dadata.py
   ```
4. Чтобы выйти из программы введите
   >exit
