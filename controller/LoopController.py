
from view.MenuView import MenuView
from controller.TestController import TestController
from model.BOQueryRepository import BOQueryRepository
from model.MDQueryRepository import MDQueryRepository
from model.NPDQueryRepository import NPDQueryRepository
import argparse

class LoopController(object):
	"""Defines main program loop and parse arguments"""

	def __init__(self, query_time_limit):
		self.__menuView = MenuView()
		self.args = self.__parseArgs()

		if self.args.limit is not None and self.args.limit > 0:
			self.__query_time_limit = self.args.limit * 60
		else:
			self.__query_time_limit = query_time_limit

	def mainLoop(self):
		if self.args.option is None:
			self.__menuView.printStart()

		while(True):
			choice = 0

			if self.args.option is None:
				choice = self.__menuView.getChoice()
			else:
				choice = self.args.option
			
			if choice == 1:
				if self.args.option is None:
					self.__menuView.delSymbol()
				
				self.runBufferOverflow()

				if self.args.option is not None:
					break

			elif choice == 2:
				if self.args.option is None:
					self.__menuView.delSymbol()
				
				self.runMemoryDisclosure()

				if self.args.option is not None:
					break

			elif choice == 3:
				if self.args.option is None:
					self.__menuView.delSymbol()
				
				self.runNullPointerDeref()

				if self.args.option is not None:
					break

			elif choice == 4:
				if self.args.option is None:
					self.__menuView.delSymbol()
				
				if not self.runBufferOverflow():
					continue

				if not self.runMemoryDisclosure():
					continue

				self.runNullPointerDeref()

				if self.args.option is not None:
					break

			elif choice == 5:
				if self.args.option is None:
					self.__menuView.delSymbol()

				#todo interactive settings

				if self.args.option is not None:
					break

			elif choice == 6:
				if self.args.option is None:
					self.__menuView.delSymbol()
				
				#todo interactive help

				if self.args.option is not None:
					break

			elif choice == 7:
				self.__menuView.delSymbol()
				break

			else:
				self.__menuView.printPlease()

	def runBufferOverflow(self):
		__bOQueryRepository = BOQueryRepository()
		controller = TestController(self.__query_time_limit, __bOQueryRepository)

		self.__menuView.printLine()
		print "[+] Running Buffer-Overflow tests."
		return controller.runAllTests()

	def runMemoryDisclosure(self):
		__mDQueryRepository = MDQueryRepository()
		controller = TestController(self.__query_time_limit, __mDQueryRepository)

		self.__menuView.printLine()
		print "[+] Running Memory disclosure tests."
		return controller.runAllTests()

	def runNullPointerDeref(self):
		__nPDQueryRepository = NPDQueryRepository()
		controller = TestController(self.__query_time_limit, __nPDQueryRepository)		
		
		self.__menuView.printLine()
		print "[+] Running Null-pointer dereference tests."
		return controller.runAllTests()

	def __parseArgs(self):
		parser = argparse.ArgumentParser(description = "Run withount arguments for interactive program menu and additional info.")
		
		parser.add_argument("-o", "--option", type = int, choices = [1, 2, 3, 4, 5, 6], 
			help = ("Options:\n"  
			   "  1) Run all Buffer Overflow tests\n"  
			   "  2) Run all Memory Disclosure tests\n"
			   "  3) Run all Null Pointer Dereference tests\n"
			   "  4) Run all tests\n"
			   "  5) Settings\n"  
			   "  6) Help\n"))

		parser.add_argument("-l", "--limit", type = int, help = "maximum execution time of query in minutes")

		return parser.parse_args()




