from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .models import Recipe, User
from .forms import RecipeForm

# recipes = [
#      {'id':1, 'name':'Meal 1', 'description':'Eggs, Bacon, Fries'},
#      {'id':2, 'name':'Meal 2', 'description':'Oatmeal & Milk'},
# ]

def loginPage(request):
    page = 'login'
    if request.user.is_authenticated:
         return redirect('home')


    if request.method == 'POST':
         email = request.POST.get('email')
         password = request.POST.get('password')

         try:
              email = User.objects.get(email=email)
         except:
              messages.error(request, 'User does not exist')

         email = authenticate(request, email=email, password=password)    

         if email is not None:
              login(request, email)
              return redirect('home')
         else:
              print('email: '+ email)
              messages.error(request, 'User OR password does not exist')  

    context = {'page': page}
    return render(request, 'base/login_register.html', context)

def logoutUser(request):
    logout(request)
    return redirect('home')

def registerPage(request):
    page = 'register'
    form = UserCreationForm()

    if request.method == 'POST':
         form = UserCreationForm(request.POST)
         if form.is_valid():
             user = form.save(commit=False) 
             user.username = user.username.lower()
             user.save()
             login(request, user)
             return redirect('home')
         else:
              messages.error(request, 'An error occured during registeration')

    return render(request,'base/login_register.html', {'form': form})


def home(request):   

     recipes = Recipe.objects.all()    
     context = {'recipes': recipes}
     return render(request, 'base/home.html',  context)

def stories(request, pk):
     recipe = Recipe.objects.get(id=pk)
     
     context =  {'recipe': recipe}          
     return render(request, 'base/recipes.html', context)

@login_required(login_url='login')
def createRecipe(request):
     form = RecipeForm()
    

     if request.method == 'POST':
     #     form = RecipeForm(request.POST)
     #     if form.is_valid():                             
     #          form.save()
     #          return redirect('home')
          
        
         
          Recipe.objects.create(
               creator=request.user,
               name=request.POST.get('name'),
               servings=request.POST.get('servings'),
               preparationTime=request.POST.get('preparationTime'),
               foodart=request.POST.get('foodart'),
               ingredients=request.POST.get('ingredients'),
               instructions=request.POST.get('instructions'),
          )
          return redirect('home')

     context = {'form': form}
     return render(request, 'base/recipe_form.html', context)

@login_required(login_url='login')
def updateRecipe(request, pk):
     recipe = Recipe.objects.get(id=pk)
     form = RecipeForm(instance=recipe)

     if request.user != recipe.creator:
         return HttpResponse('You are not allowed here!!')

     if request.method =='POST':
          recipe.name = request.POST.get('name')
          recipe.servings = request.POST.get('servings')
          recipe.preparationTime = request.POST.get('preparationTime')
          recipe.foodart = request.POST.get('foodart')
          recipe.ingredients = request.POST.get('ingredients')
          recipe.instructions = request.POST.get('instructions')
          recipe.save()
          return redirect('home')

     context = {'form': form}
     return render(request, 'base/recipe_form.html', context)

@login_required(login_url='login')
def deleteRecipe(request, pk):
     recipe = Recipe.objects.get(id=pk)

     if request.user != recipe.creator:
         return HttpResponse('You are not allowed to do that here!!')

     if request.method == 'POST':
          recipe.delete()
          return redirect('home')
     return render(request, 'base/delete.html', {'obj': recipe})

# Create your views here.
