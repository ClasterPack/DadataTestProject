import sqlite3

import requests


def check_settings():
    try:
        sqlite_connection = sqlite3.connect('settings.sqlite')
        cursor = sqlite_connection.cursor()
        settings_list = []
        for row in cursor.execute('SELECT * FROM Settings'):
            settings_list.append(row)
        if len(settings_list) == 0:
            while True:
                print('Параметры подключения к API Dadata не заданы пожалуста введите параметры.')
                print('Введите API key:')
                apikey = input()
                dadataurl = 'https://suggestions.dadata.ru/suggestions/api/4_1/rs/suggest/address'
                urlcoordinates = "https://cleaner.dadata.ru/api/v1/clean/address"
                print('Введите SecretKey к API Dadata:')
                secretkey = input()
                print('Введите язык ответа "ru" или "en"')
                lang = input()
                if lang != 'ru' and lang != 'en':
                    print(lang)
                    print('Неверно введен параметр языка ответа попробуйте еще раз.\n'
                          'Ответом может быть только en или ru:')
                    lang = input()
                dadata = DadataRequest(apikey, secretkey, dadataurl, urlcoordinates, 'ru')
                testdadata = dadata.get_suggestions('г Москва, ул Кремль, д 9')
                if testdadata[0] == "г Москва, ул Кремль, д 9":
                    print(
                        'Оставить Dadata Url по умолчанию для обрашения или изменить адрес?\n',
                        'Для того чтобы оставить по умолчанию напишите "y"',
                        ' для того чтобы изменить напишите "n"\n',
                        'Замена URL Dadata может привести к неисправности работы программы.'
                    )
                    url_answer = input()
                    while True:
                        if url_answer == 'y':
                            dadataurl = 'https://suggestions.dadata.ru/suggestions/api/4_1/rs/suggest/address'
                            urlcoordinates = "https://cleaner.dadata.ru/api/v1/clean/address"
                            break
                        if url_answer == 'n':
                            print('Введите Url Dadata Api с подсказками выбора адреса:')
                            dadataurl = input()
                            print('Введите Url Dadata Api с выводом координат:')
                            urlcoordinates = input()
                            break
                        else:
                            print('Неверный ответ.Попробуйте еще раз:\n'
                                  '"y"- оставить значение ulrs по умолчанию.\n'
                                  '"n" - изменить значение urls на свои.')
                            url_answer = input()
                    db_list = (0, 'default', apikey, dadataurl, urlcoordinates, secretkey, lang)
                    cursor.execute("INSERT INTO Settings VALUES (?, ?, ?, ?, ?, ?, ?);", db_list)
                    sqlite_connection.commit()
                    cursor.close()
                    print('Настройки сохранены в базу данных.')
                    return [apikey, dadataurl, urlcoordinates, secretkey, lang]
                else:
                    print('Неверно введен ApiKey. Введите снова:')
                    apikey = input()
        else:
            apikey, dadataurl, urlcoordinates, secretkey, lang = settings_list[0][2:7]
            return [apikey, dadataurl, urlcoordinates, secretkey, lang]
    finally:
        if sqlite_connection:
            sqlite_connection.close()


def check_address(params):
    apikey, dadataurl, urlcoordinates, secretkey, lang = params
    dadata = DadataRequest(apikey, secretkey, dadataurl, urlcoordinates, lang)
    print('Введите адрес для получения координат или введите "exit" для завершения работы.')
    response = input()
    while True:
        suggestions = dadata.get_suggestions(response)
        if len(suggestions) > 0:
            for number, suggest in enumerate(suggestions):
                print(f'{number}) {suggest}')
            print('Выберете нужный вариант и введите цифру искомого адреса.')
            answer = input()
            if answer == 'exit':
                return print('Завершение программы.')
            while True:
                if answer.isdigit():
                    if 0 <= int(answer) < len(suggestions):
                        coordinates = dadata.get_coordinates(suggestions[int(answer)])
                        print(
                            f'Координаты :\n'
                            f'Широта{coordinates[0]}, Долгота{coordinates[1]}'
                        )
                        check_address(params)
                    else:
                        print(f'"{answer}" нет в списке адресов, попробуйте ввести ответ еще раз.')
                        answer = input()
                if not answer.isdigit():
                    print('Отведом должна быть цифра, введите ответ еще раз.')
                    answer = input()
        if len(suggestions) == 0:
            print(f'Неверный запрос не можем найти адрес "{response}". Попробуйте еще раз')
            response = input()
        if response == 'exit':
            return print('Завершение программы.')


class DadataRequest:

    def __init__(self, token, secretkey, baseurl, url_coordinates, lang):
        self.token = token
        self.baseurl = baseurl
        self.secretkey = secretkey
        self.coordinates_url = url_coordinates
        self.lang = lang

    def get_suggestions(self, suggest):
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Authorization": "Token " + self.token,
        }
        list_suggestions = []
        body = {"query": suggest,
                "language": self.lang}
        response = requests.post(self.baseurl, headers=headers, json=body)
        response = response.json()
        for result in response['suggestions']:
            list_suggestions.append(result['value'])
        return list_suggestions

    def get_coordinates(self, address):
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Authorization": "Token " + self.token,
            "X-Secret": self.secretkey,
        }
        body = [address]
        response = requests.post(self.coordinates_url, headers=headers, json=body)
        response = response.json()
        return {response[0]['geo_lat']}, {response[0]['geo_lon']}


if __name__ == "__main__":
    check_address(params=check_settings())
