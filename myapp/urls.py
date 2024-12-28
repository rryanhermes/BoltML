from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('build-model/', views.build_model_page, name='build_model'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('my-models/', views.my_models, name='my_models'),
    path('my-account/', views.my_account, name='my_account'),
    path('upload-csv/', views.upload_csv, name='upload_csv'),
    path('build-model-api/', views.build_model, name='build_model_api'),
    path('delete-model/<int:model_id>/', views.delete_model, name='delete_model'),
    path('rename-model/<int:model_id>/', views.rename_model, name='rename_model'),
]