import functools

user = {"username": "john_doe", "access_level": "admin"}


def make_secure(access_level):
    def decorator(func):
        @functools.wraps(func)
        def secure_function(*args, **kwargs):
            if user["access_level"] == access_level:
                return func(*args, **kwargs)
            else:
                return f"Unauthorized user: {user['username']} does not have {access_level} access."
        return secure_function
    return decorator


@make_secure("admin")
def get_admin_password():
    return "1234"           

@make_secure("user")
def get_dashoard_password():
    return "user_password"


print(get_admin_password())
print(get_dashoard_password())  