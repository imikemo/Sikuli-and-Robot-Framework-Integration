from __future__ import with_statement
from sikuliwrapper import *

#add custom image library
addImagePath(common.cfgImageLibrary)

class Calculator(BaseLogger):
	
	ROBOT_LIBRARY_SCOPE = 'TEST SUITE'
	
	def __init__(self):
		self.appCoordinates = (0, 0, 1024, 768)
	
	def startApp(self):
		calcApp = App("Calculator")
		if not calcApp.window():
				App.open("calc.exe"); wait(2)
		calcApp.focus(); wait(1)

	def verifyApp(self):
		# check application
		if exists("CalcApp.png"):
			self.log.passed("Calculator window appeared")
		else:
			self.log.failed("No calculator window")

	def performAction(self, *args):
		# get application region
		find("CalcApp.png")
		
		match = getLastMatch()
		self.appCoordinates = (match.getX(), match.getY(), match.getW(), match.getH())
		appRegion = Region(*self.appCoordinates)
		
		#rewrite action
		action = args[1]
		if args[1] == '+':
			action = 'Plus'
		elif args[1] == 'exp':
			action = 'Exp'
		
		appRegion.click("btnC.png")

		appRegion.click( "btn%s.png" % (args[0],) )
		appRegion.click( "btn%s.png" % (action,) )
		appRegion.click( "btn%s.png" % (args[2],) )

		appRegion.click("btnEqual.png")

	def verifyResult(self, *args):
		expected_result = str(eval(''.join(args)))
		actual_result = self.getResultFromClipboard()
		
		#verification
		if actual_result == expected_result:
			self.log.passed("Action performed correctly and result equals %s" % expected_result)
		else:
			self.log.failed("Actual result '%s' is not equal to expected result '%s'" % (actual_result, expected_result))
		
	def getResultFromClipboard(self):
		type('c', KEY_CTRL)
		return str(Env.getClipboard())
		
	def getResultFromOCR(self):
		# text recognition
		textCoordinates = (self.appCoordinates[0] + 220, self.appCoordinates[1] + 45, 25, 15)
		textRegion = Region(*textCoordinates)
		return str(textRegion.text())
		
	def runTest(self):
		self.startApp()
		self.verifyApp()
		
		actions = '2+2'
		self.performAction(*actions)
		self.verifyResult(*actions)

#calc = Calculator()
#calc.runTest()
