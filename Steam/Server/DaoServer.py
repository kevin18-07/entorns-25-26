import mysql.connector


class SteamDAO:

    def connectBBDD(self):
        connection = mysql.connector.connect(
            host="127.0.0.1",
            user="steam",
            password="steam123",
            database="steam_clone"
        )
        return connection

    # ---------------- USERS ----------------

    def create_user(self, username, password):
        con = self.connectBBDD()
        cursor = con.cursor(dictionary=True)

        try:
            query = "INSERT INTO User (username, password) VALUES (%s, %s)"
            cursor.execute(query, (username, password))
            con.commit()
            return {"msg": "User created", "coderesponse": "1"}
        except Exception as e:
            return {"msg": str(e), "coderesponse": "0"}
        finally:
            cursor.close()
            con.close()

    def login(self, username, password):
        con = self.connectBBDD()
        cursor = con.cursor(dictionary=True)

        query = """
            SELECT * FROM User
            WHERE username = %s AND password = %s
        """

        cursor.execute(query, (username, password))
        user = cursor.fetchone()

        cursor.close()
        con.close()

        return user

    def get_user(self, user_id):
        con = self.connectBBDD()
        cursor = con.cursor(dictionary=True)

        cursor.execute("SELECT * FROM User WHERE id = %s", (user_id,))
        user = cursor.fetchone()

        cursor.close()
        con.close()

        return user

    # ---------------- GAMES ----------------

    def add_game(self, game_id, title, description, price):
        con = self.connectBBDD()
        cursor = con.cursor(dictionary=True)

        try:
            query = """
                INSERT INTO Game (id, title, description, price)
                VALUES (%s, %s, %s, %s)
            """
            cursor.execute(query, (game_id, title, description, price))
            con.commit()
            return {"msg": "Game added", "coderesponse": "1"}
        except Exception as e:
            return {"msg": str(e), "coderesponse": "0"}
        finally:
            cursor.close()
            con.close()

    def get_games(self):
        con = self.connectBBDD()
        cursor = con.cursor(dictionary=True)

        cursor.execute("SELECT * FROM Game")
        games = cursor.fetchall()

        cursor.close()
        con.close()

        return games

    def get_game(self, game_id):
        con = self.connectBBDD()
        cursor = con.cursor(dictionary=True)

        cursor.execute("SELECT * FROM Game WHERE id = %s", (game_id,))
        game = cursor.fetchone()

        cursor.close()
        con.close()

        return game

    # ---------------- LIBRARY ----------------

    def add_to_library(self, user_id, game_id):
        con = self.connectBBDD()
        cursor = con.cursor(dictionary=True)

        try:
            query = """
                INSERT INTO Library (user_id, game_id)
                VALUES (%s, %s)
            """
            cursor.execute(query, (user_id, game_id))
            con.commit()
            return {"msg": "Added to library", "coderesponse": "1"}
        except Exception as e:
            return {"msg": str(e), "coderesponse": "0"}
        finally:
            cursor.close()
            con.close()

    def get_library(self, user_id):
        con = self.connectBBDD()
        cursor = con.cursor(dictionary=True)

        query = """
            SELECT Game.*
            FROM Library
            JOIN Game ON Library.game_id = Game.id
            WHERE Library.user_id = %s
        """

        cursor.execute(query, (user_id,))
        games = cursor.fetchall()

        cursor.close()
        con.close()

        return games