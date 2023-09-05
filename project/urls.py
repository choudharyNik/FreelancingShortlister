from django.contrib import admin
from django.urls import path
from scrap_freelancer import views
from django.views.generic import RedirectView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("jobs/", views.ScrapList.as_view()),
    path("favicon\.ico$",RedirectView.as_view(url='/static/images/favicon.ico')),
]
