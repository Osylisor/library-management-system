from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name = 'home'),
    path('logout/', views.logout_user, name = "logout"),
    path('issue book/', views.issue_books, name = "issue_book"),
    path('new book/', views.add_new_book, name = 'new_book'),
    path('view books/', views.view_books, name = "view_books"),
    path('available books/', views.available_books,  name = "av_book"),
    path('update profile/', views.update_profile_pic, name = 'update_profile'),
    path('remove-issue/<int:id>', views.remove_issue, name = 'remove_issue'),
    path('remove-book/<int:id>', views.remove_book, name ='remove_book')
]