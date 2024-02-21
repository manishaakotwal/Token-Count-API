from django.urls import path
from .views import TokenCountAPIView

urlpatterns = [
    path('count-tokens/', TokenCountAPIView.as_view(), name='count-tokens'),
]


'''from tokenProject.urls import path
#from .views import TokenCount
from . import views
urlpatterns= [
    #path('api/token-count/', TokenCount, name='TokenCount'),
    path('messages/',views.TokenCountAPI(), name='count_token'),
]'''