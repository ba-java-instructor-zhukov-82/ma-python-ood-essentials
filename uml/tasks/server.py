class User:

    def __init__(self, name, login, password):
        self.name = name
        self.login = login
        self.password = password


class ProxyServer:

    def __init__(self):
        self.data_base = dict()

    def sign_up(self, name, login, password):
        self.data_base[login] = [name, password]

    def sign_in(self, user: User):
        if user.login in self.data_base and\
           user.password == self.data_base[user.login][1]:
            print('Welcome, {}'.format(user.name))
        else:
            print('Access denied! Login and/or password is incorrect!')


mykola = User('Mykola', 'mykola1974_ua', '*_ua_mykola_74_*')
server = ProxyServer()
server.sign_up(mykola.name, mykola.login, mykola.password)
server.sign_in(mykola)
server.sign_in(User('test', 'test_log', 'test_pass'))