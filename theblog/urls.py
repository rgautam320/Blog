from django.urls import path
# from . import views
from .views import HomeView, ArticleDetailView, AddPostView, UpdatePostView, CategoryView, AddCategoryView,  DeletePostView, LikeView, AddCommentView

urlpatterns = [
    # path('', views.home, name="home"),
    path('', HomeView.as_view(), name="home"),

    path('article/<int:pk>', ArticleDetailView.as_view(), name="article_detail"),

    path('addblogpost/', AddPostView.as_view(), name="addblogpost"),

    path('addcategory/', AddCategoryView.as_view(), name="addcategory"),

    path('article/edit/<int:pk>', UpdatePostView.as_view(), name="update_post"),

    path('article/<int:pk>/remove', DeletePostView.as_view(), name="delete_post"),

    path('category/<str:cats>/', CategoryView, name="category"),

    path('like/<int:pk>/', LikeView, name="like_post"),

    path('article/<int:pk>/comment/',
         AddCommentView.as_view(), name="add_comment"),
]
