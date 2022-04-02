
class User:
    def __init__(self, login, name=None, phone=None):
        self.login = login
        self.name = name
        self.phone = phone
        
    def add_name():
        pass
    
    def add_phone():
        pass


class Messenger:
    def __init__(self, users = {}):
        self.users = users
        
    def add_user(user):
        if user.login in users:
            print('The user with this login is already in the base. Try another name')
        else:
            users[user.login] = user


#structure
base = [{'Andrey' : {'personal' : ['65', 'Moscow', '+756777755'],
                 'chats' : ['chat1']}
                 },
        {'Julia': {'personal':['33', 'Moscow', '+7654433666'],
                   'chats':['chat3']}   
        }]
                


#initialize users
user1 = User('sdfff', 'And', '+756777755')
user2 = User('sd555', 'Andrtt', '+75677775567')
user3 = User('sddfffddd', 'An45656', '+756777755')
user4 = User('sddfffd8887', 'An456ff56','+7567777556644')


#initialize messengers
msg1 = Messenger({user1,user2})
msg2 = Messenger({user3})
phones1 = [obj.phone for obj in msg1.users]
phones2 = [obj.phone for obj in msg2.users]

#results
print(f'Users quantity in messenger 1 is less than in messenger 2 : {len(msg1.users) < len(msg2.users)}')
print(f'Difference by phone : {set(phones1) - set(phones2)}')
print(f'Union by phone : {set(phones1 + phones2)}')
print(f'Intersection by phone : {list(set(a) & set(b))}')






