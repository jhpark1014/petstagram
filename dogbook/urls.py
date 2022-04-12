from django.contrib import admin
from django.urls import path, include
from dogbook import views

app_name = 'dogbook' # namespace

# <int>: 숫자 하나 들어올거야~
# question_id: 변수 하나 잡아주는 것 -> views.detail에 전달이 된다
urlpatterns = [
    path('register/', views.register, name='register'),
    path('create_process/', views.create_process, name='create_process'),
    path('register/popup/<int', views.open_popup, name='popup'),
    path('register/popup/idcheck/', views.id_check, name='id_check'),
    path('login/', views.login, name='login'),
    # path('id_check/', views.request_page, name='id_check')
    # path('<int:question_id>', views.detail, name = 'detail')
    # path('<int:question_id>/vote/', views.vote, name='vote'),
    # path('<int:question_id>/results/', views.results, name='results')
]
