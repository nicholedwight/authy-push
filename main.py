from authy.api import AuthyApiClient
from credentials import api_key


authy_api = AuthyApiClient(api_key)

user = authy_api.users.create(
    email='nichole@ginger.io',
    phone='678-756-8101',
    country_code=1)

if user.ok():
    print(user.id)
    # user.id is the `authy_id` needed for future requests
else:
	print(user.errors())