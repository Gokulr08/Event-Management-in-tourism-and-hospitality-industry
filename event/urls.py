from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'), 
    path('profile/', views.profile, name='profile'), 
    path('logout',views.logout_page,name="logout"),
    path('service',views.service,name="service"),
    path('aboutus',views.aboutus,name="aboutus"),
    path('contact/', views.contact, name='contact'),
    path('contact/success/', views.contact_success, name='contact_success'),
    path('eventlist', views.eventlist, name="eventlist"),
    path('eventdetail/<str:ename>/', views.eventdetail, name='eventdetail'),
    path('create/', views.registerevent, name='registerevent'),
    path('success/<int:event_id>/', views.event_success, name='event_success'),
    path('terms/', views.terms, name='terms'),
    path('faqs/', views.faqs, name='faqs'),
    path('event/<str:ename>/', views.event_detail, name='event_detail'),
    path('eventregistration/<str:ename>/', views.eventregistration, name='eventregistration'),
    path('eventsuccess/<int:registration_id>/', views.eventsuccess, name='eventsuccess'),
]



