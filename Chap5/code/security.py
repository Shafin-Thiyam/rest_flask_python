from werkzeug.security import safe_str_cmp
from models.user import UsersModel

'''users=[users(1,'Shafin','hamna'),
       users(1, 'Hamna', 'haiqa'),
       users(1, 'Haiqa', 'ShafinHamna'),]

username_mapping={u.username:u for u in users}
userid_mapping ={u.id:u for u in users}'''

def authenticate(username,password):
    user= UsersModel.findByUserName(username)
    if user and safe_str_cmp(user.password,password):
        return user

def identity(payload):
    usr_id=payload['identity']
    return UsersModel.findById(usr_id)
