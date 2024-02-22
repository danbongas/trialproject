from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerPage, name="register"),
    path('',views.home, name="home"),
    path('recipe/<int:pk>/', views.stories, name="recipes"),
    path('create-recipe/', views.createRecipe, name="create-recipe"),   
    path('update-recipe/<int:pk>/', views.updateRecipe, name="update-recipe"),
    path('delete-recipe/<int:pk>/', views.deleteRecipe, name="delete-recipe"), 
    

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
