from radicale.auth import BaseAuth
from ldap3 import Server, Connection, Tls, ALL

class Auth(BaseAuth):
	def is_authenticated(self, user, password):
		ldap_basedn = ''
		if self.configuration.has_option("auth", "ldap_basedn"):
			ldap_basedn = self.configuration.get("auth", "ldap_basedn")
		self.logger.info("Configuration option %r is %r", "ldap_basedn", ldap_basedn)

		ldap_uri = ''
		if self.configuration.has_option("auth", "ldap_uri"):
			ldap_uri = self.configuration.get("auth", "ldap_uri")
		self.logger.info("Configuration option %r is %r", "ldap_uri", ldap_uri)

		ldap_port=389

		ldap_tls = ''
		if self.configuration.has_option("auth", "ldap_tls"):
			ldap_tls = self.configuration.get("auth", "ldap_tls")
		self.logger.info("Configuration option %r is %r", "ldap_tls", ldap_tls)

		ldap_rdn = ''
		if self.configuration.has_option("auth", "ldap_rdn"):
			ldap_rdn = self.configuration.get("auth", "ldap_rdn")
		self.logger.info("Configuration option %r is %r", "ldap_rdn", ldap_rdn)

		ldap_dn = ldap_rdn + '=' + user + ',' + ldap_basedn

		self.logger.info("Login attempt by %r with password %r", user)

		# Check authentication
		self.logger.info("Server configure uri", ldap_uri, "Port:", ldap_port)
		server = Server(ldap_uri, port=ldap_port)
		try:
			# Start TLS
			if ldap_tls:
				tls_config = Tls()
				conn = Connection(server, user=ldap_dn, password=password)
				conn.open()
				conn.start_tls()
			else:
				conn.open()
	
			if conn.bind():
				conn.unbind()
				return True
			else:
				self.logger.info("Couldnt not bind: ", conn.result)
				conn.unbind()
				return False
		except:
			self.logger.info("LDAP ERROR!!!!")
			return False
