from django.urls import path
from meetings import views
from meetings.views import MeetingCreateView, MeetingUpdateView, MeetingDeleteView


urlpatterns = [
    path('<int:id>', views.detail, name='detail'),
    path('rooms', views.rooms, name='rooms'),
    #when using function based views, the url pattern should be like this:
    #path('new', views.new, name='new'),
    #path('edit/<int:id>', views.edit, name='edit'),
    #path('delete/<int:id>', views.delete, name='delete'),
    
    #when using class based views, the url pattern should be like this:
    path('new/', MeetingCreateView.as_view(), name='new'),
    path('<int:pk>/edit/', MeetingUpdateView.as_view(), name='edit'),
    path('<int:pk>/delete/', MeetingDeleteView.as_view(), name='delete'),
]
