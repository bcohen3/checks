from check50 import *

class Lab2_0(Checks):

	@check()
	def exists(self):
		"""Lab2_0.cpp exists"""
		self.require("Lab2_0.cpp")
