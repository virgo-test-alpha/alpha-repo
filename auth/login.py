def check_login(users: dict[str, str], username: str, password: str) -> bool:
    return users.get(username) == password
