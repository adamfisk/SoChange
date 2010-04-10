from registration.forms import *

form = RegistrationForm()
form = RegistrationForm({
	'username': 'test',
    'email': 'test@example.com',
    'password1': 'test',
    'password2': 'test'
})

