
from joern.all import JoernSteps

class DBInterface(object):
	"""Provides database connection"""

	DATABASE_URL = "http://localhost:7474/db/data/"

	def __init__(self):
		self.connection = None
		
	def __getConnection(self):

		print "[+] Creating connection."
		try:
			self.connection = JoernSteps()
		except Exception as e:
			print "[Error] Cannot instantiate Python-Joern database interface, DBInterface says: {}".format(e.args)
			return False

		return True

	def connectToDB(self):

		if not self.__getConnection():
			return False

		print "[+] Connecting to the database."

		self.connection.setGraphDbURL(DBInterface.DATABASE_URL)

		try:
			self.connection.connectToDatabase()
		except Exception as e:
			print "[Error] Cannot connect to the database, DBInterface says: {}".format(e.args)
			return False

		
		return True

	def runQuery(self, code):
		results = None

		try:
			results = self.connection.runGremlinQuery(code)
		except Exception as e:
			print "[Error] Error occured during query execution, DBInterface says: {}".format(e.args)
			return None

		return results











