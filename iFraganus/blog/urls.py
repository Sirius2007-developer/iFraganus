from django.urls import path
from .views import index, formatDeleteView, formatCreateView, formatUpdateView, formatdetailview


urlpatterns = [
    path('', index, name="index"),
    path('team/<slug:team>/', formatdetailview, name="formatdetail"),
    path('team/edit/<slug>/', formatUpdateView.as_view(), name="formatUpdateView"),
    path('format/delete/<slug>/', formatDeleteView.as_view(), name="formatDeleteView"),
    path('format/create', formatCreateView.as_view(), name="formatCreateView"),
]