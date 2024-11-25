from utils.s2t_handler import S2THandler


def get_auth_token(username, password):
    token = S2THandler.get_auth_token(username, password)
    return token
