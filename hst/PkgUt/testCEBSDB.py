import unittest
import time
import django
import sys
import os

sys.path.append('../../DjoSiteDba/')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DjoSiteDba.settings")
django.setup()
from django.db import transaction
from DappDbCebs import views as DappDbCebs

from DappDbCebs import models

from PkgUt import ModTestSuitComFunc
print(models.t_cebs_object_profile.objects.all().last().objid)
