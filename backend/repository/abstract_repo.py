from abc import ABC, abstractmethod
from fastapi import HTTPException
from models.product import TableProduct
from models.user import TableUser
from config import host, db_user, password, db_name
import psycopg2


class AbstractRepository(ABC):
    @abstractmethod
    def add(self, data: tuple):
        raise NotImplementedError
    
    @abstractmethod
    def get(self, obj_id: str, string_of_param: str = "*") -> tuple:
        raise NotImplementedError
    
    @abstractmethod
    def get_all(self, string_of_param: str = "*"):
        raise NotImplementedError
    
    @abstractmethod
    def obj_is_exists(self, connection: psycopg2.connect, obj_id: str):
        raise NotImplementedError
    
    @abstractmethod
    def get_by_id(self, obj_ids: list[int], string_of_param: str = "*"):
        raise NotImplementedError

class SQLRepository(AbstractRepository):
    model: TableUser | TableProduct
    def add(self, data: tuple):
        try:
            connection = psycopg2.connect(
                host=host, user=db_user, password=password, database=db_name
            )
            with connection.cursor() as cursor:
                if self.obj_is_exists(connection, obj_id=data[2]):
                    raise HTTPException(status_code=400, detail="User already exists")
                else: 
                    cursor.execute(
                        f"INSERT INTO {self.model.tablename} ({self.model.string_of_columns}) VALUES ({','.join(['%s'] * data.__len__())})", 
                        data
                    )
                    connection.commit()
                    raise HTTPException(status_code=200, detail="User added")
        except psycopg2.Error as _ex:
            print("[INFO] Error", _ex)
            raise HTTPException(status_code=500, detail="Internal Server Error")
        finally:
            if connection:
                connection.close()
                print("[INFO] Connection to Database closed")

    def obj_is_exists(self, connection: psycopg2.connect, obj_id: str):
        with connection.cursor() as cursor:
            cursor.execute(
                f"SELECT COUNT({self.model.obj_id_column}) FROM {self.model.tablename} WHERE {self.model.obj_id_column} = %s",
                (obj_id, )
            )
            return cursor.fetchone()[0] != 0
        
    def get(self, obj_id: str, string_of_param: str = "*") -> tuple:
        try:
            connection = psycopg2.connect(
                host=host, user=db_user, password=password, database=db_name
            )
            with connection.cursor() as cursor:
                cursor.execute(
                    f"SELECT {string_of_param} FROM {self.model.tablename} WHERE {self.model.obj_id_column} = %s",
                    (obj_id, )
                )
                data = cursor.fetchone  ()
                if data.__len__() == 0:
                    raise HTTPException(status_code=404, detail=f"Object with id: '{obj_id}' don't exist")
                return data
        except psycopg2.Error as _ex:
            print("[INFO] Error", _ex)
            raise HTTPException(status_code=500, detail="Internal Server Error")
        finally:
            if connection:
                connection.close()
                print("[INFO] Connection to Database closed")

    def get_all(self, string_of_param: str = "*") -> list[tuple]:
        try:
            connection = psycopg2.connect(
                host=host, user=db_user, password=password, database=db_name
            )
            with connection.cursor() as cursor:
                cursor.execute(
                    f"SELECT {string_of_param} FROM {self.model.tablename}"
                )
                return cursor.fetchall()
        except Exception as _ex:
            print("[INFO] Error", _ex)
            raise HTTPException(status_code=500, detail="Internal Server Error")
        finally:
            if connection:
                connection.close()
                print("[INFO] Connection to Database closed")

    def get_by_id(self, obj_ids: list[int], string_of_param: str = "*") -> list[tuple]:
        try:
            connection = psycopg2.connect(
                host=host, user=db_user, password=password, database=db_name
            )
            with connection.cursor() as cursor:
                cursor.execute(
                    f"SELECT {string_of_param} FROM {self.model.tablename} WHERE {self.model.obj_id} IN %s",
                    (tuple(obj_ids), )
                )
                return cursor.fetchall()
        except Exception as _ex:
            print("[INFO] Error", _ex)
            raise HTTPException(status_code=500, detail="Internal Server Error")
        finally:
            if connection:
                connection.close()
                print("[INFO] Connection to Database closed")