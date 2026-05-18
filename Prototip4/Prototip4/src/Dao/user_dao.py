from Prototip4.Prototip4.src.db import get_connection

class UserDAO:

    def get_user_by_username_or_email(self, username):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT id, username, email, password, idrole, token
            FROM users
            WHERE username = ? OR email = ?
        """, (username, username))

        user = cursor.fetchone()
        conn.close()
        return dict(user) if user else None

    def get_user_by_token(self, token):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT id, username, email, password, idrole, token
            FROM users
            WHERE token = ?
        """, (token,))

        user = cursor.fetchone()
        conn.close()
        return dict(user) if user else None

    def validate_password(self, user, password):
        # (simplificat: en producció usar hash!)
        return user and user["password"] == password