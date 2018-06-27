"""DjoSiteDba URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url

# from DappDbComm import views as DappDbComm_views
# from DappDbTest import views as DappDbTest_views
# from DappDbCebs import views as DappDbCebs_views
# from DappDbBfdf import views as DappDbBfdf_views
# from DappDbBfhs import views as DappDbBfhs_views
# from DappDbBfhs import views as DappDbCcl_views
# from DappDbBfhs import views as DappDbFaam_views

urlpatterns = [
    #BASIC
    path('admin/', admin.site.urls),
    # url(r'^$', DappDbTest_views.index, name='index'),
    # #url(r'^$', admin.site.urls),
    # path('index/', DappDbTest_views.index),
    #
    # #DappDbTest UserInfo
    # path('user_info_add/', DappDbTest_views.user_info_add),
    # path('user_info_show/', DappDbTest_views.user_info_show),
    # path('user_info_delete/', DappDbTest_views.user_info_delete),
    # path('user_info_modify/', DappDbTest_views.user_info_modify),
    # path('user_info_home/', DappDbTest_views.user_info_home),
    
    #TEST
    #url(r'^show/', DappDbBfdf_views.show),
    #url(r'^index/', DappDbBfhs_views.index),
    #url(r'^home/', DappDbTest_views.login()),  # CBV
    #path('index/', views.index),
]
