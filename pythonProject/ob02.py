# Разработай систему управления учетными записями пользователей для небольшой компании.
# Компания разделяет сотрудников на обычных работников и администраторов.
# У каждого сотрудника есть уникальный идентификатор (ID), имя и уровень доступа.
# Администраторы, помимо обычных данных пользователей, имеют дополнительный уровень доступа
# и могут добавлять или удалять пользователя из системы.
#
# Требования:
#
# 1.Класс `User*: Этот класс должен инкапсулировать данные о пользователе:
# ID, имя и уровень доступа ('user' для обычных сотрудников).
#
# 2.Класс Admin: Этот класс должен наследоваться от класса User.
# Добавь дополнительный атрибут уровня доступа, специфичный для администраторов ('admin').
# Класс должен также содержать методы add_user и remove_user, которые позволяют добавлять
# и удалять пользователей из списка (представь, что это просто список экземпляров User).
#
# 3.Инкапсуляция данных: Убедись, что атрибуты классов защищены от прямого доступа и модификации снаружи.
# Предоставь доступ к необходимым атрибутам через методы (например, get и set методы).

class User:
    def __init__(self):
        self.__user_id = None
        self.user_name = None
        self.access_level = 'user'

    def get_user_id(self):
        return self.__user_id

    def set_user_id(self, user_id):
        self.__user_id = user_id
        return self.__user_id

class Admin(User):
    def __init__(self):
        super().__init__()
        self.__users = []
        self.__admin_users = []
        self.user_id_counter = 1

    def add_admin_user(self, user_name):
        self.user_name = user_name
        self.access_level = 'admin'
        self.__admin_users.append({'userid': self.user_id_counter, 'name': user_name, 'access_level': self.access_level})
        print(f"Admin user {user_name}, id - {self.user_id_counter}, access level - {self.access_level} added")
        self.user_id_counter += 1


    def add_user(self, user_name):
        user = User()
        user.user_name = user_name
        user_id = user.set_user_id(self.user_id_counter)
        self.__users.append({'userid': user_id, 'name': user_name, 'access_level': user.access_level})
        print(f"User {user_name}, id - {user_id}, access level - {user.access_level} added")
        self.user_id_counter += 1

    def remove_user(self, user_id):
        for user in self.__users:
            if user['userid'] == user_id:
                self.__users.remove(user)
                print(f"User named {user['name']} with id {user_id} removed")
                return
        print(f"User with id {user_id} not found")

    def print_users(self):
        print("\nUsers:")
        for user in self.__users:
            print(f"ID: {user['userid']}, Name: {user['name']}, Access Level: {user['access_level']}")


admin = Admin()
admin.add_admin_user('admin1')
admin.add_user('user1')
admin.add_user('user2')
admin.add_user('user3')
admin.add_user('user4')
admin.print_users()
admin.remove_user(4)
admin.print_users()

user = User()
user.user_name = 'user1'

print(f"User {user.user_name}, id - {user.get_user_id()}, access level - {user.access_level}")

