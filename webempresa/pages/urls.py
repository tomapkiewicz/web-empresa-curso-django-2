from django.urls import path
from . import views  

urlpatterns = [
    path('<int:page_id>/<page_title>', views.page, name='page'),
]
