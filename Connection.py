class DBConnection:
    def __init__(self, user, password, server, port, database):
        self.user = user
        self.password = password
        self.server = server
        self.port = port
        self.database = database

    def __enter__(self):
        self.connect_string = 'mongodb://' + self.user + ':' + self.password + '@' + self.server + ':' + self.port +\
                              '/' + self.database

        self.client = MongoClient(self.connect_string)

        self.access_db = self.client[self.database]

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.client.close()