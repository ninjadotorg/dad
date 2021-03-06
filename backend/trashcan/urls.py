"""trashcan URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from api import views
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'api/signup/', views.user_signup),
    path(r'api/signin/', views.user_signin),
    path(r'api/profile/', views.ProfileList.as_view()),
    path(r'api/withdraw/', views.WithdrawList.as_view()),
    path(r'api/oscar/image/', views.OscarUpload.as_view()),
    path(r'api/profile/<int:pk>/', views.ProfileDetail.as_view()),
    path(r'api/product/', views.ProductList.as_view()),
    path(r'api/product/<int:pk>/', views.ProductDetail.as_view()),
    path(r'api/profile-category/follow/', views.FollowCategory.as_view()),
    path(r'api/profile-category/unfollow/', views.UnfollowCategory.as_view()),
    path(r'api/profile-following/follow/', views.FollowProfile.as_view()),
    path(r'api/profile-following/unfollow/', views.UnfollowProfile.as_view()),
    path(r'api/image/', views.ImageList.as_view()),
    path(r'api/image/<int:pk>/', views.ImageDetail.as_view()),
    path(r'api/image-profile/', views.ImageProfileList.as_view()),
    path(r'api/image-profile/<int:pk>/', views.ImageProfileDetail.as_view()),
    path(r'api/image-profile/like/', views.LikeImage.as_view()),
    path(r'api/image-profile/unlike/', views.UnlikeImage.as_view()),
    path(r'api/category/', views.CategoryList.as_view()),
    path(r'api/category/<int:pk>/', views.CategoryDetail.as_view()),
    path(r'api/explore-category/', views.ExploreCategory.as_view()),
    path(r'api/classify/', views.ClassifyList.as_view()),
    path(r'api/classify/<int:pk>/', views.ClassifyDetail.as_view()),
    path(r'api/feed/', views.Feed.as_view()),
    path(r'api/search/', views.Search.as_view()),
    path(r'api/buy/', views.Buy.as_view()),
    path(r'api/contract/inc-balance/', views.inc_balance_contract),
    path(r'api/contract/pay/', views.Pay.as_view()),
    path(r'docs/', include_docs_urls(title='Trashcan API docs', public=True))

]
