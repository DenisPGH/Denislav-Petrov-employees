from django.urls import path

from CSV.sirma.views import StartPage

urlpatterns=(
    path('',StartPage.as_view(),name='index'),
    #path('',ShowResult.as_view(),name='result'),
)