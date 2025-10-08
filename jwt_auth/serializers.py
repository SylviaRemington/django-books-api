from rest_framework import serializers
# the password validation function runs on top of the model when creating superuser
from django.contrib.auth import get_user_model, password_validation # function runs when creating superuser
from django.contrib.auth.hashers import make_password # hashes the password for us
from django.core.exceptions import ValidationError

# Start by getting user model
User = get_user_model()

# More full one than regular serializers because adding validation on the user.
class UserSerializer(serializers.ModelSerializer): # never converted to json and returned in response
    # user has a password...
    # Can't see password - write only not read - can't see data. Prevent it from being shown.
    password = serializers.CharField(write_only=True) # write_only=True ensures never sent back in JSON
    password_confirmation = serializers.CharField(write_only=True)

    # WRITING VALIDATOR HERE BELOW:

    # validate function is going to:
    # 1. check our passwords match
    # 2. hash our passwords
    # 3. add them back to the database
    def validate(self, data): # data comes from the request body
        print('DATA',data)

        # remove fields from request body and save to vars
        password = data.pop('password')
        password_confirmation = data.pop('password_confirmation')

        # check if they match - #1
        # if password is not the same as password confirmation, raise a validation error
        if password != password_confirmation:
            raise ValidationError({'password_confirmation': 'do not match'})

        # checks if password is valid, comment this out so it works - #2
        try:
            password_validation.validate_password(password=password)
        except ValidationError as err:
            print({'VALIDATION ERROR:': err.message})
            raise ValidationError({'password: ': err.message })

        # add it to the database & hash the password, reassigning value on dict - #3
        # updating the data to hash it

        # updating the data object to hash it
        # If password works, we add to to the database and hash it.
        # hash the pswd if it is valid
        data['password'] = make_password(password)

        print('DATA ->', data)
        return data

    class Meta:
        model = User
        # In future, might want to not have this for all fields
        # Might be certain fields we don't want to return so we'll cut this down.
        fields = '__all__'

# Next we are going to work on jwt auth views.py because working towards having a login endpoint and a register endpoint.


