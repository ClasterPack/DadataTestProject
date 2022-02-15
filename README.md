# Тестовое задание для CARBIS
Описание задания: [docs.google.com](https://docs.google.com/document/d/1E_LMzWsoXW-BTZDzJ1p6w3ScKgIw5tfd7FHh-NKn1SA/edit#)

## Рабочее окружение:

Для начала разработки необходимо настроить рабочее окружение. Нам понадобятся следующие системные зависимости: 
- [python](https://www.python.org/downloads/) версии 3.9 или выше
- менеджер зависимостей [pip](https://pip.pypa.io/en/stable/installation/)

Настройка окружения:
1. Настроить репозиторий
    ```shell script
    gh repo clone ClasterPack/DadataTestProject 
    cd DadataTestProject
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
   1. При первом запуске внесите необходимые параметры:
      1. API key
      2. secretkey
      3. язык API
      4. При необходимости можно записать свой url
      
   2. Запуск в консоле
      ```shell script
      python main.py
      ```
   3. Чтобы выйти из программы введите
      >exit
