from django.urls import path,include
from oauth.views import TokenPairLoginView

urlpatterns = [
    path('login/', TokenPairLoginView)
]