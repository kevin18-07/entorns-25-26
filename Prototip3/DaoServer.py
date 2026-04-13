from flask import Flask, request, jsonify
import mysql.connector


class UserDAO:

    def connectBBDD(self):
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="tapatap"
        )
        return connection

    def login(self, identifier, password):
        # connexió a BBDD
        con = self.connectBBDD()
        cursor = con.cursor(dictionary=True)
        query = """
        SELECT * FROM User
        WHERE (username = %s OR email = %s) AND password = %s
        """
        cursor.execute(query, (identifier, identifier, password))
        user = cursor.fetchone()
        cursor.close()
        con.close()
        return user


dao = UserDAO()
u = dao.login("mare", "mare")
print(u)

       