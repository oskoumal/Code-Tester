
from model.BOQueryRepository import BOQueryRepository
from model.MDQueryRepository import MDQueryRepository
from model.NPDQueryRepository import NPDQueryRepository
from model.DBInterface import DBInterface
from view.TestView import TestView
import time
import multiprocessing

class TestController(multiprocessing.Process):
	"""Tests codebase against Buffer-Overflow queries"""


	def __init__(self, limit, repository):
		self.__queryRepository = repository
		self.__dbInterface = DBInterface()
		self.__testView = TestView()
		self.__query_time_limit = limit


	def runAllTests(self):
		if not self.__dbInterface.connectToDB():
			return False

		print "[+] Fetching query list."
		queryList = self.__queryRepository.getQueryList()

		for q in queryList:

			# Define subprocess
			p = multiprocessing.Process(target = self.__runQueryInProcess, args=(q, ))

			print "\n[+] Running query {}, {}.".format(q.number, q.name)
			p.start()
			
			# Waiting on process to finish set ammount of time
			p.join(self.__query_time_limit)

			# Terminate process if it didn't finished in time
			if p.is_alive():
				self.__testView.delSymbol()
				print "[+] Query didn't finished in time limit, skipping."
				p.terminate()

		return True


	def __runQueryInProcess(self, query):
		# Set GUI Loop
		self.__testView.startLoop()

		# Measure processor time by time.clock() returns wrong numbers
		start = time.time()
		results = self.__dbInterface.runQuery(query.code)

		end = time.time()
		
		self.__testView.stopLoop()

		print "[+] Quering finished."
		print "[+] Elapsed time: {} seconds.".format(end - start)

		if results is None:
			print "[+] No vulnerabilities found."
			return

		elif len(results) == 0:
			print "[+] No vulnerabilities found."
			return


		print "[+] Number of positive samples: " + str(len(results))
		print "[+] Possible vulnerabilities:" 

		for r in results:
			print r








	





		











		


		

	
