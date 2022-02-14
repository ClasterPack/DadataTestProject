import asyncio

from main import DadataRequest
from settings import APIKEY, LANG, SECRETKEY, URLCOORDINATES, URLDADATA


def welcome_print():
    dadata = DadataRequest(APIKEY, SECRETKEY, URLDADATA, URLCOORDINATES, LANG)
    print('Введите адрес для получения координат или введите "exit" для завершения работы.')
    responce = input()
    if responce == 'exit':
        return print('Завершение программы')
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    suggestions = loop.run_until_complete(dadata.get_suggestions(responce))
    while len(suggestions) == 0:
        print('Неверный запрос попробуйте еще раз.')
        responce = input()
        suggestions = loop.run_until_complete(dadata.get_suggestions(responce))
    while len(suggestions) > 0:
        print('Введите цифру с нужным адресом или введите "exit" для завершения работы.')
        for number, suggest in enumerate(suggestions):
            print(f'{number}) {suggest}')
        answer = input()
        break
    if answer == 'exit':
        return print('Завершение программы')
    while not answer.isdigit():
        print('Неверный ответ, необходимо ввести цифру ответ.')
        answer = input()
    while not 0 <= int(answer) < len(suggestions):
        print(f'Неверный ответ, цифры {answer} нет в выборе. Попробуй ещё раз.')
        answer = input()
    while answer.isdigit() and 0 <= int(answer) < len(suggestions):
        reply = loop.run_until_complete(dadata.get_coordinates(suggestions[int(answer)]))
        print(
            f'Координаты :\n'
            f'Широта{reply[0]}, Долгота{reply[1]}'
        )
        break
    loop.close()
    welcome_print()


if __name__ == "__main__":
    welcome_print()
