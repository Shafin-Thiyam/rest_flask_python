from user import users
user=[
    {'id':1,
     'username':'Shafin',
     'password':'hamna'},
    {'id': 2,
     'username': 'hamna',
     'password': 'haiqa'},
    {'id': 3,
     'username': 'haiqa',
     'password': 'shafinhamna'}
]
username_mapping={'shafin':{'id':1,
                  'username':'Shafin',
                  'password':'hamna'},

                  'hamna':{'id': 2,
                  'username': 'hamna',
                  'password': 'haiqa'},

                  'haiqa':{'id': 3,
                  'username': 'haiqa',
                  'password': 'shafinhamna'}}

userid_mapping = {1: {'id': 1,
                               'username': 'Shafin',
                               'password': 'hamna'},

                  2: {'id': 2,
                              'username': 'hamna',
                              'password': 'haiqa'},

                  3: {'id': 3,
                              'username': 'haiqa',
                              'password': 'shafinhamna'}}

def authenticate(username,password):
    usr= username_mapping.get(username,None)
    if usr and user.password==password:
        return user

def identity(payload):
    usr_id=payload['identity']
    return userid_mapping.get(usr_id,None)