from django.contrib import admin
from django.urls import path
from core.views import index, dashboard


urlpatterns = [
    path("admin/", admin.site.urls),

    path("", index, name="index"),

    path(
        "admin-dashboard/",
        dashboard,
        name="dashboard"
    ),
]
