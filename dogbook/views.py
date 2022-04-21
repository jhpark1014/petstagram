from django.shortcuts import render, get_object_or_404, get_list_or_404
from dogbook.models import users, Image
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
import pymysql
from dogbook import models


def index(request):
    return render(request, 'index.html')


def register(request):
    return render(request, 'dogbook/register.html')


def create_process(request):
    new_user = request.POST.get('username')
    con = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='wlgus7921', db='dogstagram_db', charset='utf8')
    cursor = con.cursor(pymysql.cursors.DictCursor)
    stmt = "SELECT username FROM dogbook_users WHERE username='{}'"
    stmt = stmt.format(new_user)
    cursor.execute(stmt)
    data = cursor.fetchall()

    if not data:
        user = users()
        user.username = request.POST.get('username')
        user.full_name = request.POST.get('full_name')
        user.email = request.POST.get('email')
        user.passwd = request.POST.get('passwd')
        user.phoneno = request.POST.get('phoneno')
        user.save()
        return render(request, 'dogbook/success.html')

    else:
        return render(request, 'dogbook/login_fail.html')

    # if 'id_check_btn' in request.POST:
    #     user = request.POST.get('username')
    #     return render(request, 'dogbook/popup.html')


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
    return render(request, 'dogbook/popup.html')

def open_popup2(request, username):
    context = {'usr': username}
    return render(request, 'dogbook/popup.html', context)


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
        # context = get_object_or_404(users, username=username)
        return render(request, 'dogbook/login_fail.html')
    else:
        usr = get_object_or_404(users, username=user)
        context = {'thisuser': usr}
        return render(request, 'dogbook/login_success.html', context)


def profile(request, username):
    usr = get_object_or_404(users, username=username)
    imgs = Image.objects.filter(author=username)
    context = {'thisuser': usr, 'usrimgs': imgs}
    return render(request, 'dogbook/profile.html', context)


def pet_register(request):
    return render(request, 'dogbook/pet_register.html')


def missing(request):
    return render(request, 'dogbook/practice.html')


def upload_page(request, username):
    usr = get_object_or_404(users, username=username)
    context = {'thisuser': usr}
    return render(request, 'dogbook/upload_page.html', context)


def upload(request, username):
    if request.method == "POST":
        # Fetching the form data
        contents = request.POST["content"]
        upload_image = request.FILES["upload_image"].name
        author = request.POST['author']

        # Saving the information in the database
        document = models.Image(
            name = contents,
            imagefile = upload_image,
            author = author
        )
        document.save()
        # doc = Image()
        # doc.author = request.POST.get('author')
        # doc.name = request.POST['content']
        # doc.imagefile = upload_image
        # doc.save()

    # documents = get_object_or_404(Image, username=username)
    # documents = Image.objects.all()
    # context = {'my_posts': documents}

    return render(request, 'dogbook/profile.html')
# HttpResponseRedirect(reverse('dogbook:profile', args=(username,)))
