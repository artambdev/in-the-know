from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path("", include("contact.urls"), name="contact-urls"),
    path("", include("list.urls"), name="list-urls"),
]
