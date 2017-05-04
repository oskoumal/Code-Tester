
class MenuView(object):
	"""Prints main menu interface and receives user input"""

	CURSOR_UP_ONE = "\x1b[1A"
	ERASE_LINE = "\x1b[2K"
	TEXT_GREEN = "\x1b[32m"

	def printStart(self):
		print ("  /////////////////////////////\n"
			   " ///    Code-tester 1.0    ///\n"
			   "/////////////////////////////\n")
		print ("Options:\n"  
			   "  1) Run all Buffer Overflow tests\n"  
			   "  2) Run all Memory Disclosure tests\n"
			   "  3) Run all Null Pointer Dereference tests\n"
			   "  4) Run all tests\n"
			   "  5) Settings\n"  
			   "  6) Help\n"
			   "  7) Quit\n")

	def getChoice(self):
		choice = 0
		try:
			choice = int(raw_input())
		except ValueError:
			pass

		return choice

	def delSymbol(self):
		print(MenuView.CURSOR_UP_ONE + MenuView.ERASE_LINE + MenuView.CURSOR_UP_ONE)

	def printPlease(self):
		print "Please choose an option."

	def printLine(self):
		print "\n========================================="





