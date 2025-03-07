import psycopg2
from pydantic import BaseModel
from config import host, user, password, db_name, Status
import jwt
from base64 import b64decode
import bcrypt


class GameCard(BaseModel):
    game_name: str
    game_img: str
    game_price: int
    game_id: int
    

def add_new_user(name: str, surname: str, mail: str, _password: str):
    try:
        connection = psycopg2.connect(
            host=host, user=user, password=password, database=db_name
        )
        with connection.cursor() as cursor:
            if user_is_exists(mail, connection):
                return Status.UserExistsError.value
            else:
                salt = bcrypt.gensalt()
                key = bcrypt.hashpw(password=_password.encode(), salt=salt).decode() 
                cursor.execute(
                    "INSERT INTO users (name, surname, mail, password, secret) VALUES (%s, %s, %s, %s, %s)",
                    (name, surname, mail, key, salt.decode()) 
                )
                connection.commit()
                return Status.OK.value
    except Exception as _ex:
        print("[INFO] Error", _ex)
        return Status.InternalServerError.value
    finally:
        if connection:
            connection.close()
            print("[INFO] Connection to Database closed")


def user_is_exists(mail: str, connection: psycopg2.connect):
    with connection.cursor() as cursor:
        cursor.execute("SELECT COUNT(user_id) FROM users WHERE mail = (%s)", (mail, ))
        return cursor.fetchone()[0] != 0


def add_new_game(game_card: GameCard):
    try:
        connection = psycopg2.connect(
            host=host, user=user, password=password, database=db_name
        )
        with connection.cursor() as cursor:
            cursor.execute(
                "INSERT INTO games_cards (game_name, game_price, game_img) VALUES (%s, %s, %s)",
                (game_card.game_name, game_card.game_price, game_card.game_price)
            )
            connection.commit()
            return Status.OK.value
    except Exception as _ex:
        print("[INFO] Error", _ex)
        return Status.InternalServerError.value
    finally:
        if connection:
            connection.close()
            print("[INFO] Connection to Database closed")

def get_all_game_cards():
    try:
        connection = psycopg2.connect(
            host=host, user=user, password=password, database=db_name
        )
        with connection.cursor() as cursor:
            cursor.execute(
                f"SELECT * FROM games_cards"
            )
            result: list[GameCard] = []
            for game in cursor.fetchall():
                result.append(GameCard(game_id=game[0], game_name=game[1], game_price=game[2], game_img=game[3]))
            return result
    except Exception as _ex:
        print("[INFO] Error", _ex)
        return Status.InternalServerError.value
    finally:
        if connection:
            connection.close()
            print("[INFO] Connection to Database closed")

def get_user_password(mail: str):
    try:
        connection = psycopg2.connect(
            host=host, user=user, password=password, database=db_name
        )
        with connection.cursor() as cursor:
            if user_is_exists(mail, connection):
                cursor.execute(
                    f"SELECT password, secret FROM users WHERE mail = %s",
                    (mail, )
                )
                return cursor.fetchone()
            else:
                return Status.UserDontExistError
    except Exception as _ex:
        print("[INFO] Error", _ex)
        return Status.InternalServerError.value
    finally:
        if connection:
            connection.close()
            print("[INFO] Connection to Database closed")


def get_user_id(mail: str):
    try:
        connection = psycopg2.connect(
            host=host, user=user, password=password, database=db_name
        )
        with connection.cursor() as cursor:
            if user_is_exists(mail, connection):
                cursor.execute(
                    f"SELECT user_id FROM users WHERE mail = %s",
                    (mail, )
                )
                return cursor.fetchone()[0]
            else:
                return Status.UserDontExistError
    except Exception as _ex:
        print("[INFO] Error", _ex)
        return Status.InternalServerError.value
    finally:
        if connection:
            connection.close()
            print("[INFO] Connection to Database closed")

