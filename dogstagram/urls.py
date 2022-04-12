from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from dogbook import views

# client의 URL을 얘가 먼저 받음
# http://localhost:8000/polls/ -> 'polls/'
# 이 URLConf는 설정임 여기서 실행시키는게 아님
# views.index는 polls로 들어오면 index()함수를 쓸거라고 알려주는 것
# view.index() 괄호 절대 쓰면 안돼!!

urlpatterns = [
    # path('', TemplateView.as_view(template_name='index.html'), name='home'),
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    path('dogbook/', include('dogbook.urls'))
    ]