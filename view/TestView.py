
import threading
import time

class TestView(threading.Thread):
	"""Prints into console test interface"""

	CURSOR_UP_ONE = "\x1b[1A"
	ERASE_LINE = "\x1b[2K"
	TEXT_GREEN = "\x1b[32m"

	def startLoop(self):

		self.t_stop = threading.Event()
		t = threading.Thread(target = self.__workingLoop)
		t.start()

	def stopLoop(self):

		self.delSymbol()
		self.t_stop.set()


	def __workingLoop(self):
		while(not self.t_stop.is_set()):

			print "[+] Searching."
			time.sleep(1)
			self.delSymbol()
			if self.t_stop.is_set():
				break

			print "[+] Searching.."
			time.sleep(1)
			self.delSymbol()

			if self.t_stop.is_set():
				break

			print "[+] Searching..."
			time.sleep(1)
			self.delSymbol()


	def delSymbol(self):
		print(TestView.CURSOR_UP_ONE + TestView.ERASE_LINE + TestView.CURSOR_UP_ONE)
