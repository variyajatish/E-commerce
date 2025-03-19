from django.urls import path
from .views import HomePage, LoginPage, SignupPage, MainPage, ProductPage, Signupform, Loginform, Categories, AddCart, UserCart, RemoveId
from django.conf import settings  
from django.conf.urls.static import static 

urlpatterns = [ 
    path('', HomePage),
    path('login', LoginPage),
    path('signup', SignupPage),
    path('main', MainPage),
    path('product', ProductPage),
    path('creatuser', Signupform),
    path('loginuser', Loginform),
    path('categories', Categories),
    path('addcart', AddCart),
    path('cart', UserCart),
    path('remove', RemoveId),
]

if settings.DEBUG:  
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)  