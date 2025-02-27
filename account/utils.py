from jwt import decode
from django.conf import settings
from rest_framework.exceptions import AuthenticationFailed

def unhash_token(request_header):
    token = request_header.get("Authorization", "")
    if token:
        try:
            token = token.split(" ")[1]
            decoded_token = decode(token, settings.SECRET_KEY, algorithms=["HS256"])
            return decoded_token
        except IndexError:
            raise AuthenticationFailed("Invalid token format")
        except Exception as e:
            raise AuthenticationFailed("Invalid or expired token")
    else:
        raise AuthenticationFailed("Authorization header missing")


