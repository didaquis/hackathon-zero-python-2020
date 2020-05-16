import secrets

class PasswordGenerator:
	_nbytes = 16
	def new_password(self):
		return secrets.token_hex(self._nbytes)
