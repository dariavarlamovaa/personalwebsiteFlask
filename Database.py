class DataBase:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()

    def _get_objects(self, table, *args):
        try:
            columns = ', '.join(args)
            self.__cur.execute(f'SELECT {columns} FROM {table}')
            res = self.__cur.fetchall()
            if res:
                return res
        except IOError:
            print('Error while connecting to database')
        return []

    def get_menu(self):
        return self._get_objects('menu', 'title', 'url')

    def get_tools(self):
        tools = self._get_objects('tools', 'title', 'category')
        grouped_tools = {}
        for tool, category in tools:
            if not grouped_tools.get(category):
                grouped_tools[category] = []

            grouped_tools[category].append(tool)
        return grouped_tools
