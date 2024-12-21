from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.index, name="index"),  # Ana sayfa için URL
    path("hakkinda/", views.about, name="about"),
    path("kimyasallar/", views.chemicals, name="chemicals"),
    path("ekibimiz/", views.team, name="team"),
    path("iletisim/", views.contact, name="contact"),
    path("siparis/", views.products, name="products"),
    path("galeri/", views.gallery, name="gallery"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

