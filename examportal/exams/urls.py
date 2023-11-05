from django.urls import path
from . import views
urlpatterns = [
    path('liveexams/',views.liveexams,name='liveexams'),
    path('conductexak/',views.conductexam,name='conductexam'),
    path('addquestion/',views.addquestion,name='addquestion'),
    path('liveexam/',views.liveexams,name='liveexam'),
    path('viewquestion/',views.viewquestions,name='viewquestion'),
    path('viewquestions/<int:pk>', views.viewquestions, name='viewquestions'),
]