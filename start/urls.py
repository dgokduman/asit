from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.index, name="index"),  # Ana sayfa için URL
    path("hakkimizda/", views.about, name="about"),
    path("urunlerimiz/", views.chemicals, name="chemicals"),
    path("ekibimiz/", views.team, name="team"),
    path("iletisim/", views.contact, name="contact"),
    path("siparis/", views.products, name="products"),
    path("fotograflar/", views.gallery, name="gallery"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'start.views.view_404' 
# replace `myapp` with your app's name where the above view is located