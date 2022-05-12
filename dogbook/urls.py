from django.contrib import admin
from django.urls import path, include
from dogbook import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'dogbook' # namespace

# <int>: 숫자 하나 들어올거야~
# question_id: 변수 하나 잡아주는 것 -> views.detail에 전달이 된다
urlpatterns = [
    path('register/', views.register, name='register'),
    path('create_process/', views.create_process, name='create_process'),
    path('register/popup/', views.open_popup, name='popup'),
    path('register/popup/<str:username>', views.open_popup2, name='popup'),
    path('register/popup/idcheck/', views.id_check, name='id_check'),
    path('login/', views.login, name='login'),
    path('pet_register/', views.pet_register, name='pet_register'),
    path('missing/', views.missing, name='missing'),
    path('<str:username>/upload/', views.upload_page, name='upload_page'),
    path('uploading', views.upload, name='uploading'),
    path('<str:username>/', views.profile, name='profile'),


    # path('id_check/', views.request_page, name='id_check')
    # path('<int:question_id>', views.detail, name = 'detail')
    # path('<int:question_id>/vote/', views.vote, name='vote'),
    # path('<int:question_id>/results/', views.results, name='results')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
