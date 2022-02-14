import sqlite3

APIKEY = ""
URLDADATA = "https://suggestions.dadata.ru/suggestions/api/4_1/rs/suggest/address"
URLCOORDINATES = "https://cleaner.dadata.ru/api/v1/clean/address"
SECRETKEY = ""
LANG = "ru"


def sqlite_save_default_settings():
    try:
        sqlite_connection = sqlite3.connect('settings.sqlite')
        cursor = sqlite_connection.cursor()
        db_list = (0, 'default', APIKEY, URLDADATA, URLCOORDINATES, SECRETKEY, LANG)
        cursor.execute("INSERT INTO Settings VALUES (?, ?, ?, ?, ?, ?, ?);", db_list)
        sqlite_connection.commit()
        cursor.close()
    finally:
        if sqlite_connection:
            sqlite_connection.close()


def sqlite_save_settings(name, apikey, urldadata, urlcoordinates, secretkey, language):
    try:
        sqlite_connection = sqlite3.connect('settings.sqlite')
        cursor = sqlite_connection.cursor()
        db_list = (name, apikey, urldadata, urlcoordinates, secretkey, language)
        cursor.execute("INSERT INTO Settings"
                       "(name, apikey, urldadata, urlcoordinates, secretkey, language)"
                       " VALUES (?,?,?,?,?,?)", db_list)
        sqlite_connection.commit()
        cursor.close()
    finally:
        if sqlite_connection:
            sqlite_connection.close()


if __name__ == "__main__":
    sqlite_save_default_settings()
