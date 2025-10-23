# Инкапсуляция
# Метод 1 классика жанра
class Config:
    def __init__(self):
        self.__store = {}
    def set_store(self, key, value):
        if not key in self.__store:
            self.__store[key] = value
    def get_store(self, key):
        if key in self.__store:
           return self.__store[key]
        else:
            raise Exception(f"Нет такого ключа '{key}'")

cnf = Config()
cnf.set_store('db', 'llm')
cnf.set_store('host', 'localhost')
cnf.set_store('port', '5424')
cnf.set_store('user', 'postgres')
cnf.set_store('passwd', '123')
print(cnf.get_store('db'))
print(cnf.get_store('host'))
try:
    print(cnf.get_store('hosts'))
except Exception as e:
    print(e.__repr__())


# Метод 2 дандеры __getattr__  _setattr__
class SuperConfig():
    def __init__(self):
        self.__store = {}

    def __getattr__(self, key):
        # print(__store)
        if key in self.__store:
           return self.__store[key]
        else:
           raise Exception(f"Нет такого ключа '{key}'")

    def __setattr__(self, key, value):
        if key == '_SuperConfig__store':
            print(key)
            self.__dict__[key] = value
            return None
        if not key in self.__store:
           self.__store[key] = value
        else:
            raise Exception(f"Ключ уже существует '{key}'")

cnf = SuperConfig()
cnf.db = "llm"
cnf.host = "localhost"
print(cnf.db)
print(cnf.host)
print(cnf.__dict__)

# Метод 3 property
class DB:
    def __init__(self, namedb, host, port ):
            self.__namedb = namedb
            self.__host = host
            self.__port = port

    def __str__(self):
         return f"{self.__namedb} {self.__host} "

    @property
    def namedb(self):
        return self.__namedb

    @namedb.setter
    def namedb(self, value):
        self.__namedb = value

my_db = DB('llm', '127.0.0.1', 5424)
print(my_db.namedb)
