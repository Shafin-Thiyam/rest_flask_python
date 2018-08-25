from user import users

users=[users(1,'Shafin','hamna'),
       users(1, 'Hamna', 'haiqa'),
       users(1, 'Haiqa', 'ShafinHamna'),]

username_mapping={u.username:u for u in users}
userid_mapping ={u.id:u for u in users}

def authenticate(username,password):
    user= username_mapping.get(username,None)
    if user and user.password==password:
        return user

def identity(payload):
    usr_id=payload['identity']
    return userid_mapping.get(usr_id,None)