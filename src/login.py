import os
def login(username, password):
    if not username or not password:
        return False
    admin_user = os.getenv('ADMIN_USER', 'admin')
    admin_pass = os.getenv('ADMIN_PASS', '123')
    return username == admin_user and password == admin_pass
