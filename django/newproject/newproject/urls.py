from django.contrib import admin
from django.urls import path, include
from newproject.core import views

urlpatterns = [
    path('',views.home,name='home'),
    path('signup/',views.signup,name="signup"),
    path('accounts/', include('django.contrib.auth.urls')),
    # path('secret/',views.secret_page,name='secret'),
    # path('secret2/',views.Secretpage.as_view(),name='secret2'),
    path('admin/', admin.site.urls),
]
