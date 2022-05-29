from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('sneakers/', views.sneakers_index, name='index'),
    path('sneakers/<int:sneaker_id>/', views.sneakers_detail, name='detail'),
    path('sneakers/create/', views.SneakerCreate.as_view(), name='sneakers_create'),
    path('sneakers/<int:pk>/update/', views.SneakerUpdate.as_view(), name='sneakers_update'),
    path('laces/', views.LaceList.as_view(), name='laces_index'),
    path('laces/<int:pk>/', views.LaceDetail.as_view(), name='laces_detail'),
    path('laces/create/', views.LaceCreate.as_view(), name='laces_create'),
    path('laces/<int:pk>/update/', views.LaceUpdate.as_view(), name='laces_update'),
    path('laces/<int:pk>/delete/', views.LaceDelete.as_view(), name='laces_delete'),
    path('sneakers/<int:pk>/delete/', views.SneakerDelete.as_view(), name='sneakers_delete'),
    path('sneakers/<int:sneaker_id>/add_cleaning/', views.add_cleaning, name='add_cleaning'),
    path('sneakers/<int:sneaker_id>/assoc_lace/<int:lace_id>/', views.assoc_lace, name='assoc_lace'),
    path('sneakers/<int:sneaker_id>/add_photo/', views.add_photo, name='add_photo'),
      path('accounts/signup/', views.signup, name='signup')
]