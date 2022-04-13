from django.shortcuts import render, get_object_or_404
from dogbook.models import users
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
import pymysql


def index(request):
    return render(request, 'index.html')


def register(request):
    return render(request, 'dogbook/register.html')


def create_process(request):
    user = users()
    user.username = request.POST.get('username')
    user.full_name = request.POST.get('full_name')
    user.email = request.POST.get('email')
    user.passwd = request.POST.get('passwd')
    user.phoneno = request.POST.get('phoneno')
    user.save()
    return render(request, 'dogbook/success.html')


def id_check(request):
    user = request.POST.get('username')
    con = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='wlgus7921', db='dogstagram_db', charset='utf8')
    cursor = con.cursor(pymysql.cursors.DictCursor)
    stmt = "SELECT username FROM dogbook_users WHERE username='{}'"
    stmt = stmt.format(user)
    cursor.execute(stmt)
    data = cursor.fetchall()
    # user = users.objects.get(username=username)
    if not data:
        # context = {'form': form, 'error': '이 아이디는 사용중입니다. 다른 아이디를 입력하세요.'}
        messages.success(request, f'This username can be used')
        return render(request, 'dogbook/id_success.html')
    else:
        messages.info(request, f'This username is already in use')
        return render(request, 'dogbook/id_fail.html')


def open_popup(request):
    if request.method == 'GET':
        return render(request, 'dogbook/popup.html')


def login(request):
    user = request.POST.get('username')
    passwd = request.POST.get('passwd')
    con = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='wlgus7921', db='dogstagram_db', charset='utf8')
    cursor = con.cursor(pymysql.cursors.DictCursor)
    stmt = "SELECT username FROM dogbook_users WHERE username='{}' and passwd='{}'"
    stmt = stmt.format(user, passwd)
    cursor.execute(stmt)
    data = cursor.fetchall()

    if not data:
        # messages.success(request, f'This username can be used')
        # context = get_object_or_404(users, username=username)
        return render(request, 'dogbook/login_fail.html')
    else:
        # messages.info(request, f'This username is already in use')
        usr = get_object_or_404(users, username=user)
        context = {'thisuser': usr}
        return render(request, 'dogbook/login_success.html', context)


def profile(request, username):
    username = get_object_or_404(users, username=username)
    return render(request, 'profile.html')
