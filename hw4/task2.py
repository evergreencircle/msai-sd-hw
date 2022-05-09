from abc import ABC, abstractmethod


class UserStorage(ABC):
    @abstractmethod
    def save(self, user):
        pass

class UserDB(UserStorage):
    def save(self, user):
        print(f'Save the {user} to database')
        
class UserXML(UserStorage):
    def save(self, user):
        print(f'Save the {user} to a XML file')
        
        

class SendInfo(ABC):
    @abstractmethod
    def send_info(self, message):
        pass
    
class Email(SendInfo):
    def __init__(self, email):
        self.email = email

    def send_info(self, message):
        print(f'Sent "{message}" to {self.email}')
        
class SMS(SendInfo):
    def __init__(self, phone):
        self.phone = phone

    def send_info(self, message):
        print(f'Sent "{message}" to {self.phone}')

class SendManager:
    def __init__(self, notification):
        self.notification = notification

    def send(self, message):
        self.notification.send_info(message)
        


class ChatStorage(ABC):
    @abstractmethod
    def save(self, chat):
        pass

class ChatDB(ChatStorage):
    def save(self, chat):
        print(f'Save the {chat} to database')
        
class ChatXML(ChatStorage):
    def save(self, chat):
        print(f'Save the {chat} to a XML file')



class User:
    def __init__(self, login, name=None, phone=None, email=None):
        self.login = login
        self.name = name
        self.phone = phone
        self.email = email
    
    def __repr__(self):
        return f'User {self.__dict__}'

    def add_name():
        pass

    def add_phone():
        pass


class Chat(ABC):
    def __init__(self, users = {}):
        self.users = users 
    
    def __repr__(self):
        print(f'Chat {self.users}')
        return f'Chat {self.users}'
        
    @abstractmethod
    def publish(self):
        pass
    
class ChatWithCom(Chat):
    @abstractmethod
    def comment(self):
        pass
    
class BlogWithComment(ChatWithCom):
    def publish(self):
        print("Publishing")
        
    def comment(self):
        print("Commmenting")
    
class ChatWithoutCom(Chat):
    def publish(self):
        print("Publishing")  
    

class Messenger:
    def __init__(self, users = {}, chats = {}):
        self.users = users
        self.chats = chats

        

if __name__ == '__main__':
    user1 = User('sdfff', 'And', '+756777755', '123@rrf.org')
    user2 = User('sd555', 'Andrtt', '+75677775567')
    user3 = User('sddfffddd', 'An45656', '+756777755')
    user4 = User('sddfffd8887', 'An456ff56','+7567777556644')
    chat1 = BlogWithComment({'user1', 'user2', 'user3', 'user4'})
    db = UserDB()
    db.save(user1)
    xml = UserXML()
    xml.save(user1)
    cht = ChatDB()
    cht.save(chat1)
    sms_message = SMS(user1.phone)
    email_message = Email(user1.email)
    send_manager = SendManager(sms_message)
    send_manager.send('Hi')
    send_manager.notification = email_message
    send_manager.send('Hi')

