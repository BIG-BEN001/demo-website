from django.urls import path
# from .views import about_page_view, home_page_view, contact_page_view
from .views import HomePageView, AboutPageView, BlogPageView, ContactPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about-us', AboutPageView.as_view(), name='about'),
    path('blog', BlogPageView.as_view(), name='blog'),
    path('contact-us', ContactPageView.as_view(), name='contact'),
    
        
    # path('', home_page_view, name='home'),
    # path('about', about_page_view, name='about'),
    # path('contact', contact_page_view, name='conatct')
    
]
