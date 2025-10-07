# BasicAuthentication class from rest framework
from rest_framework.authentication import BasicAuthentication
# checking permissions
from rest_framework.exceptions import PermissionDenied
# registers user
from django.contrib.auth import get_user_model
# settings from our project for secret key - setting from settings.py within project folder
from django.conf import settings  # show secret key in settings.py
# importing jwt package (the pyjwt package we installed in terminal)
import jwt

User = get_user_model()

# BasicAuthentication has stuff built in like password & email validation - now will build on top of it


# assertain users permissions # requests come through here # assign a permission level # if valid token -> given permission to see secure things
class JWTAuthentication(BasicAuthentication):
    def authenticate(self, request):  # check requets has token and return if so

        # first tries to get authorization header (e.g. the bearer token, aka auth header, from Postman)
        header = request.headers.get('Authorization')

        # if no headers, just return to end the request & don't get anywhere
        if not header:
            return None

        # if token is wrong format, throw error
        # Did user send a bearer token?
        if not header.startswith('Bearer'):
            # If header doesn't start with a Bearer token, then permission will be denied cause wrong type.
            raise PermissionDenied(detail='Invalid Auth token')

        # pass all checks, store token in variable - if does send bearer token
        # If they do send a Bearer token, then it passes and replace the Bearer with a string (empty string) so we just get the token.
        token = header.replace('Bearer ', '')

        # get payload with users id from token & algorithms
        try:
            # SO WE DECODE AND WE GET THE PAYLOAD (BELOW)
            # can show https://jwt.io again so they can see the alg and the secret
            # HS256 is default, it will be this unless we specify a different alg when we sign the token
            # payload - token, secret used to encrypt and decrypt, & the algorithm that it will be encryping and decrypting with (an encrypting algorithm) - the salt level/salting with algorithms an encryption algorithm
            payload = jwt.decode(token, settings.SECRET_KEY,
                                 algorithms=['HS256'])

            # find user with that id in db
            # gets user with primary key
            # GOING TO THE DATABASE & THEN RETRIEVING OUR USER BASED ON THE PRIMARY KEY.
            user = User.objects.get(pk=payload.get('sub'))
            # THEN PRINTING OUT WHAT THE USER ACTUALLY IS
            print('USER ->', user)
            # issue with the token

            # if we get an error and invalid token when decoding it will fall into the below exception
            # THIS IS THE "WHAT IF" SCENARIO HERE: IF INVALID TOKEN & CAN'T DECODE THEN, THEN...
        except jwt.exceptions.InvalidTokenError:
            raise PermissionDenied(detail='Invalid Token')

        # If the user does not exist it will fall into the below
        except User.DoesNotExist:
            raise PermissionDenied(detail='User Not Found')

        # if all good, return user and the token - This is where returns token.
        # THIS RETURNS THE USER AND TOKEN IF VALID. WE HAVEN'T SAID WHERE WE ARE GOING TO RETURN IT TO YET, HOWEVER THIS FUNCTION IS NOW WORKING and has the user and token.
        return (user, token)

#Need to tell Django that everything it's trying to render is in JSON and go to project settings.
#Need to add a few more things about rest framework in our project setttings.
