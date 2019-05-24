from django.conf.urls import include, url
from django.contrib import admin
from courses import views
urlpatterns = [
    # Examples:
    # url(r'^$', 'DP03.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^home/', views.index),
]
