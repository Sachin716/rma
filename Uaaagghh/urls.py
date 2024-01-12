from django.urls import path
from . import views
from django.conf import settings 
from django.conf.urls.static import static

urlpatterns = [
    path("",views.home, name="home"),
    path("contacts",views.contacts , name="contacts"),
    path("services/<int:id>", views.servicess, name="services"),
    path("appointment" , views.appoint , name="appoint"),
    path("admin_login" , views.admin , name="admin"),
    path("View" , views.view , name="view"),
    path('register' , views.register , name='register'),
    path('cate/<str:cats>' , views.cat_page , name='WellShit'),
    path("Confirmed" , views.conf , name="conf"),
    path("admin_home" , views.admin_home , name="admin"),
    path("checked/<int:id>" , views.checked , name="checked"),
    path("logout" , views.logoutt , name="logout"),
    path("gallery" ,views.galle , name="gallery"),
    path("review" , views.reviewsss , name="review")
]

urlpatterns += static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)