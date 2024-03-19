from django.urls import path
from. import views
app_name='myapp1'
urlpatterns = [
    path('register1/',views.hospitalregisterview,name='register1'),
    path('login/',views.hospitalloginview,name='login'),
    path('hospital/',views.hospital,name='hospital'),
    # path('appiontent/',views.appiontmentview,name='appiontmentlists')
]