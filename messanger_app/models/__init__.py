from clcrypto import password_hash

"""
CREATE TABLE Users(
id serial,
username varchar(255),
email varchar(255),
hashed_password varchar(255),
PRIMARY KEY (id)
);
"""

class User:
    __id = -1
    username = None
    __hashed_password = None
    email = None

    @staticmethod
    def get_user_by_email(cursor, email):
        sql = "SELECT id, username, email, hashed_password FROM users WHERE email=%s"
        cursor.execute(sql, (email,))  # (email, ) - bo tworzymy krotkę
        data = cursor.fetchone()
        if data:
            loaded_user = User()
            loaded_user.__id = data[0]
            loaded_user.username = data[1]
            loaded_user.email = data[2]
            loaded_user.__hashed_password = data[3]
            return loaded_user

    def save_to_db(self, cursor):
        if self.__id == -1:
            sql = """INSERT INTO Users(username, email, hashed_password)
                             VALUES(%s, %s, %s) RETURNING id"""
            cursor.execute(sql, (self.username, self.email, self.__hashed_password))
            (id,) = cursor.fetchone()
            self.__id = id
            #self.__id = cursor.fetchone()[0]  # albo cursor.fetchone()['id']
            return True

    def set_password(self, new_pasword):
        self.__hashed_password = password_hash(new_pasword)

    def delete_user(self):
        raise NotImplementedError

    @staticmethod
    def get_all_users():
        return [User(), User()]