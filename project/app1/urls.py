from django.urls import path,include
from.import views
urlpatterns = [
    path('',views.homefunction,name='home'),
    path("products",views.productfunction,name='products'),
    path("categories",views.categoryfunction),
    path('cat_prod<int:id>',views.cat_products,name='cat_pro'),
    path('view<int:id>',views.view_products,name='view_pro'),
    path('cart<int:id>',views.cartfunction,name='cart'),
    path('signup',views.signfunction),
    path('login',views.loginfunction,name='login'),
    path('logout',views.logoutfunction,name='logout'),
    path('cartpage',views.cartpage,name='cartpage'),
    path('remove<int:id>',views.removefunction,name='remove'),
    path('placeorder',views.placeorderfunction,name='placeorder'),
    path('thankyou',views.orderconfirmfunction,name='thankyou'),
    path('wishlist<int:id>',views.wishfunction,name='wishlist'),
    path('wishpage',views.wishpage,name='wishpage'),
    
    path('createcategory',views.createcategory,name='createcategory'),
    path('createproduct',views.createproduct,name='createproduct'),
    path('adminhome',views.adminsite,name='adminsite'),
    path('viewcreatedProd',views.viewcreatedProd,name='viewcreatedProd'),
    path('viewcreatedCat',views.viewcreatedCat,name='viewcreatedCat'),
    path('delete<int:id>',views.deletebysuper,name='delete'),
    path('edit<int:id>',views.editbysuper,name='editby'),
]