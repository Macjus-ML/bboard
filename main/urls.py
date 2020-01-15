from django.urls import path

from .views import index, other_page, BBLoginView, BBLogoutView
from .views import BBPasswordChangeView
from .views import profile, ChangeUserInfoView

app_name = 'main'
urlpatterns = [
    path('accounts/password/change', BBPasswordChangeView.as_view(),name='password_change'),
    path('accounts/profile/change', ChangeUserInfoView.as_view(), name='profile_change'),
    path('accounts/profile/', profile, name='profile'),
    path('accounts/logout/', BBLogoutView.as_view(), name='logout'),
    path('accounts/login/', BBLoginView.as_view(), name='login'),
    path('<str:page>/', other_page, name='other'),
    path('', index, name='index'),

]
