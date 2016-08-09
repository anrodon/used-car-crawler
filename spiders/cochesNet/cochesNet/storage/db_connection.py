import psycopg2

class CarDB:
    def __init__(self, host, db_name, user, password):
        # Define our connection string
        conn_string = "host='" + host + "' dbname='" + db_name + "' user='" + user + "' password='" + password + "'"
        # get a connection, if a connect cannot be made an exception will be raised here
        self.__conn = psycopg2.connect(conn_string)


    def cursor(self):
        return self.__conn.cursor()

    def commit(self):
        return self.__conn.commit()

    def close(self):
        return self.__conn.close()