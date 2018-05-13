"""
CREATE TABLE Users(
id serial,
username varchar(255),
email varchar(255),
hasher_password varchar(255),
PRIMARY KEY (id)
);
"""

class User:
    __id = None
    username = None
    __hashed_password = None
    email = None

    @staticmethod
    def get_user_by_email(email):
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


    def set_password(self, new_pasword):
        self.__hashed_password = new_pasword

    def delete_user(self):
        pass

    @staticmethod
    def get_all_users():
        return [User(), User()]