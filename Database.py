import sqlite3


class DataBase:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()

    def _get_objects(self, table):
        try:
            self.__cur.execute(f'SELECT * FROM {table}')
            res = self.__cur.fetchall()
            if res:
                return res
        except IOError:
            print('Error while connecting to database')
        return []

    def _get_specific_objects(self, table, value):
        try:
            self.__cur.execute(f'SELECT * FROM {table} WHERE category={value}')
            res = self.__cur.fetchall()
            if res:
                return res
        except IOError:
            print('Error while connecting to database')
        return []

    def get_menu(self):
        return self._get_objects('menu')

    # def get_tools(self):
    #     return self._get_specific_objects('tools')
