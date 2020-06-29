known_users = ['bob', 'julian', 'mike', 'carmen', 'sue']
loggedin_users = ['mike', 'sue']


def login_required(func):
    def check_user(user):
        if user in loggedin_users:
            return func(user)
        elif user in known_users:
            return f'please login'
        else:
            return f'please create an account'
    return check_user
    pass


@login_required
def welcome(user):
    '''Return a welcome message if logged in'''
    return f'welcome back {user}'
    pass