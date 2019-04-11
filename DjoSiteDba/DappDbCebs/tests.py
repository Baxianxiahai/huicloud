from django.test import TestCase

from DappDbCebs.views import dct_classDbiViewDebs

class GetInitConfTextCase(TestCase):
	def getInfo(self):
		dct_classDbiViewDebs.dft_dbi_cebs_init_config_read(self)
# Create your tests here.
