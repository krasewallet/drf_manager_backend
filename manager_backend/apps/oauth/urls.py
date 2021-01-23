from oauth.views import TokenPairLoginView

urlpatterns = [
    path('login/', TokenPairLoginView)
]