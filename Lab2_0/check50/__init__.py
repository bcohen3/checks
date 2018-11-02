from check50 import *

class Lab2_0(Checks):

	@check()
	def exists(self):
		"""Lab2_0.cpp exists"""
		self.require("Lab2_0.cpp")
	
	@check("exists")
	def compiles(self):
		"""Lab2_0.cpp compiles"""
		self.spawn("clang -o g++ Lab2_0.cpp -lcs50 -lm").exit(0)

	@check("compiles")
	def test_41_cents(self):
		"""input of 0.41 yields output of 4"""
		self.spawn("./a.out").stdin("1 1").stdout("Your horoscope sign is: Capricorn\n", "Your horoscope sign is: Capricorn\n").exit(0)
