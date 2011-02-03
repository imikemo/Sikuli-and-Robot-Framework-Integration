import common 
from logger import *
from sikuli.Sikuli import Region as SikuliRegion


# enable slow motion if debug log level enabled
if common.cfgLoggingLevel.lower() == 'debug':
	setShowActions(True)

# =============================================== #
#          Overwritten sikuli methods             #
# =============================================== #

# function for calling native sikuli methods
def sikuli_method(name, *args, **kwargs):
	return sys.modules['sikuli.Sikuli'].__dict__[name](*args, **kwargs)

# overwritten Screen.exists method
def exists(target, timeout=None):
	addFoundImage(getFilename(target))
	return sikuli_method('exists', target, timeout)

# =============================================== #
#          Overwritten sikuli classes             #
# =============================================== #
	
# overwriten Sikuli Region class
class Region(SikuliRegion, BaseLogger):
	
	def click(self, target, modifiers=0):
		try:
			return SikuliRegion.click(self, target, modifiers)
		except FindFailed, e:			
			self.log.html_img("Find Filed", "images/" + getFilename(target))
			self.log.screenshot(msg="Region", region=(self.getX(), self.getY(), self.getW(), self.getH()))
			raise e
	def exists(self, target, timeout=None):
		img = getFilename(target)
		reg = (self.getX(), self.getY(), self.getW(), self.getH())
		addFoundImage(img, reg)
		return SikuliRegion.exists(self, target, timeout)