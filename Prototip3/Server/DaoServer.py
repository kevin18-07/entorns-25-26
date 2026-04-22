import mysql.connector
import hashlib
import time
import random


class UserDAO:

    def connectBBDD(self):
        connection = mysql.connector.connect(
            host="192.168.144.210",
            user="root",
            password="root",
            database="tapatap"
            
        )
        return connection

    def login(self, identifier, password):
        con = self.connectBBDD()
        cursor = con.cursor(dictionary=True)

        query = """
            SELECT * FROM User
            WHERE (username = %s OR email = %s)
            AND password = %s
        """

        cursor.execute(query, (identifier, identifier, password))
        user = cursor.fetchone()

        cursor.close()
        con.close()

        return user

    def setTokenUser(self, username):
        con = self.connectBBDD()
        cursor = con.cursor()

        token = self.getHash()

        query = "UPDATE User SET token = %s WHERE username = %s"
        cursor.execute(query, (token, username))

        con.commit()

        cursor.close()
        con.close()

        return token

    def getHash(self):
        milliseconds = str(time.time() * 1000)
        data = milliseconds + str(random.randrange(10000))
        hash_object = hashlib.sha256(data.encode('utf-8'))
        return hash_object.hexdigest()
