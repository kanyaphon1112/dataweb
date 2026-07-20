"""
URL configuration for myabb project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.http import HttpResponse

def welcome(request):
    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>The install worked successfully! Congratulations!</title>
        <style>
            body { margin: 0; font-family: sans-serif; background: #fff; }
            header { background: #092e20; color: #fff; padding: 20px 40px; display: flex; justify-content: space-between; align-items: center; }
            header a { color: #fff; text-decoration: none; font-weight: bold; font-size: 1.1em; }
            .content { text-align: center; padding: 80px 20px; }
            .rocket { font-size: 80px; }
            h1 { color: #092e20; font-size: 2.5em; margin: 20px 0 10px; }
            p { color: #555; font-size: 1.1em; }
            a.btn { display: inline-block; margin: 10px; padding: 12px 28px; border-radius: 4px; text-decoration: none; font-weight: bold; }
            a.btn-green { background: #092e20; color: #fff; }
            a.btn-outline { border: 2px solid #092e20; color: #092e20; }
        </style>
    </head>
    <body>
        <header>
            <a href="https://www.djangoproject.com/">django</a>
            <a href="/admin/">Django administration</a>
        </header>
        <div class="content">
            <div class="rocket">🚀</div>
            <h1>The install worked successfully! Congratulations!</h1>
            <p>You are seeing this page because <code>DEBUG=True</code> is not set and you haven't configured any URLs.</p>
            <p>
                <a class="btn btn-green" href="https://docs.djangoproject.com/en/stable/">Django Documentation</a>
                <a class="btn btn-outline" href="/admin/">Admin Panel</a>
            </p>
        </div>
    </body>
    </html>
    """
    return HttpResponse(html)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', welcome, name='welcome'),
]
