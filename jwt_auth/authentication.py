from rest_framework.authentication import BasicAuthentication
# checking permissions
from rest_framework.exceptions import PermissionDenied
# registers user
from django.contrib.auth import get_user_model
# settings from our project for secret key
from django.conf import settings  # show secret key in settings.py
# importing jwd package
import jwt

User = get_user_model()

# BasicAuthentication has stuff built in like password & email validation - now will build on top of it


# assertain users permissions # requests come through here # assign a permission level # if valid token -> given permission to see secure things
class JWTAuthentication(BasicAuthentication):
    def authenticate(self, request):  # check requets has token and return if so

        # first tries to get authorization header
        header = request.headers.get('Authorization')

        # if no headers, just return to end the request & don't get anywhere
        if not header:
            return None

        # if token is wrong format, throw error
        # did user send bearer token
        if not header.startswith('Bearer'):
            raise PermissionDenied(detail='Invalid Auth token')

        # pass all checks, store token in variable - if does send bearer token
        token = header.replace('Bearer ', '')

        # get payload with users id from token & algorithms
        try:
            # can show https://jwt.io again so they can see the alg and the secret
            # HS256 is default, it will be this unless we specify a different alg when we sign the token
            # payload - token, secret, saltin with algorithms an encryption algorithm
            payload = jwt.decode(token, settings.SECRET_KEY,
                                 algorithms=['HS256'])

            # find user with that id in db
            # gets user with primary key
            user = User.objects.get(pk=payload.get('sub'))
            print('USER ->', user)
            # issue with the token

            # if we get an error and invalid token when decoding it will fall into the below exception
        except jwt.exceptions.InvalidTokenError:
            raise PermissionDenied(detail='Invalid Token')

        # If the user does not exist it will fall into the below
        except User.DoesNotExist:
            raise PermissionDenied(detail='User Not Found')

        # if all good, return user and the token - This is where returns token.
        return (user, token)

#Need to tell Django that everything is in JSON and go to project settings.
