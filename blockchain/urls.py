from django.urls import path, re_path
from .views import Coin, MiningArea


urlpatterns = [
    path('send/', Coin.as_view({'post': 'send'}), name="send"),
    path('mine/', MiningArea.as_view({'post': 'smash_rocks'}), name="smash_rocks")
]