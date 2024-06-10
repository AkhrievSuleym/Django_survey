from django.urls import path

from . import views

app_name = "polls"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("new_question/", views.get_question, name="new_question"),
    path("<int:pk>/new_comment", views.get_comment, name="new_comment"),
]