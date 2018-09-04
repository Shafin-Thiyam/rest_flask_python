from werkzeug.security import safe_str_cmp
from models.user import UsersModel

'''users=[users(1,'Shafin','hamna'),
       users(1, 'Hamna', 'haiqa'),
       users(1, 'Haiqa', 'ShafinHamna'),]

username_mapping={u.username:u for u in users}
userid_mapping ={u.id:u for u in users}'''

def authenticate(username,password):
    #No longer needed since findbyuser in user class will take care of that
    #user= username_mapping.get(username,None)
    user= UsersModel.findByUserName(username)
    #if user and user.password==password:
    if user and safe_str_cmp(user.password,password):
        return user

def identity(payload):
    usr_id=payload['identity']
    #Same applicable here since user class has findbyid function
    #return userid_mapping.get(usr_id,None)
    return UsersModel.findById(usr_id)
