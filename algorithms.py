from Crypto.PublicKey import RSA
from Crypto.Hash import SHA224, SHA256, SHA384, SHA512, keccak
from Crypto.Cipher import PKCS1_OAEP

class rsa():
	def __init__(self):
		self.public_key = None
		self.private_key = None

	def generate_key_pair(self):
		key = RSA.generate(2048)

		# Private key is being generated
		self.private_key = open("private.pem", "wb")
		self.private_key.write(key.export_key())
		self.private_key.close()

		# Public key is being generated
		self.public_key = open("public.pem", "wb")
		self.public_key.write(key.publickey().export_key())
		self.public_key.close()

		return self.private_key, self.public_key

	def encrypt_key(self, session_key):
		recipent_key = RSA.import_key(open("private.pem").read())

		# Encrypt the session key with the public RSA key
		cipher_rsa = PKCS1_OAEP.new(recipent_key)
		key_encrypted = cipher_rsa.encrypt(session_key)

		return key_encrypted

	def decrypt_key(self, key_encrypted):
		recipent_key = RSA.import_key(open("private.pem").read())
		cipher_rsa = PKCS1_OAEP.new(recipent_key)
		key_decrypted = cipher_rsa.decrypt(key_encrypted)

		return key_decrypted

class hash():
	def __init__(self, hash, text):
		self.hash = hash
		self.text = text
		self.digest = None
		
	def function(self):
		if (self.hash == 'keccak'):
			self.digest = keccak.new(digest_bits=512)
			self.digest.update(self.text)
		elif (self.hash == 'SHA224'):
			self.digest = SHA224.new()
			self.digest.update(self.text)
		elif (self.hash == 'SHA256'):
			self.digest = SHA256.new()
			self.digest.update(self.text)
		elif (self.hash == 'SHA384'):
			self.digest = SHA384.new()
			self.digest.update(self.text)
		elif (self.hash == 'SHA512'):
			self.digest = SHA512.new()
			self.digest.update(self.text)
			
		return self.digest.hexdigest()

class expanded_key():
	def __init__(self, password):
		self.password = password
		self.salt = None

	def salt(self, password):
		pass

	def digest(self, self.salt, password):
		pass