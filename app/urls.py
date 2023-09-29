from django.urls import path

from app import views

urlpatterns = [
    path('generate-question', views.mcqView.as_view()),
    path('create-blog', views.createBlogView.as_view()),
    path('convert-content-to-blog-page', views.convertContentToBlogPage.as_view()),
]