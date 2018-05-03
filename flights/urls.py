from django.urls import path
from django.conf.urls import url
from django.contrib.auth.views import LogoutView

import flights.views

urlpatterns = [
    path('', flights.views.main_page, name='main_page'),
    path('flights/', flights.views.flight_list, name='flight_list'),
    path('login/', flights.views.login_view, name='login'),
    path('logout/', flights.views.logout_view, name='logout'),
    path('registration/', flights.views.registration_view, name='registration'),
    path('search/', flights.views.search_page, name='search_page'),
    path('flights/<int:flight_id>', flights.views.flight_page, name='flight_page'),
    path('airports/<slug:airport_id>', flights.views.airport_page, name='airport_page'),
    url(r'^planes/(?P<plane_id>[a-zA-Z\']+)$', flights.views.plane_page, name='plane_page'),
]