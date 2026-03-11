from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

# temporary view for testing the login redirect
def temp_browse(request):
    return HttpResponse("<h1>🎉 Welcome to the Browse Page! You are successfully logged in!</h1>")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    
    # map the root URL to our temporary browse view
    path('', temp_browse, name='browse'), 
]