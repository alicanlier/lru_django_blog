from django.urls import path
from bookmark.views import BookmarkLV,BookmarkDV
from bookmark import views

app_name = 'bookmark'
# templates(view단위) 까지 안내하는 방법을 기술한것
urlpatterns = [
    path('', BookmarkLV.as_view(),name='index'),
    path('<int:pk>/', BookmarkDV.as_view(), name='detail'),
        # Example: /bookmark/add/
    path('add/', views.BookmarkCreateView.as_view(), name="add"),
    
    # Example: /bookmark/change/
    path('change/', views.BookmarkChangeLV.as_view(), name="change"),
    
    # Example: /bookmark/99/update/
    path('<int:pk>/update/', views.BookmarkUpdateView.as_view(), name="update"),
    
    # Example: /bookmark/99/delete/
    path('<int:pk>/delete/', views.BookmarkDeleteView.as_view(), name="delete"),
    path('', BookmarkLV.as_view(),name='bookmark_index'),
    path('<int:pk>/', BookmarkDV.as_view(), name='bookmark_detail'),
]