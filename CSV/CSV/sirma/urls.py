from django.urls import path

from CSV.sirma.views import StartPage,ShowResult

urlpatterns=(
    path('',StartPage.as_view(),name='index'),
    path('result/',ShowResult.as_view(),name='result'),
)