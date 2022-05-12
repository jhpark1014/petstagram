from django.db import models


# Create your models here.
class users(models.Model):
    # id INT, AUTO_INCREMENT NOT NULL PK 이거는 자동으로 만들어짐
    username = models.CharField(max_length=20, unique=True)
    full_name = models.CharField(max_length=20, blank=False)
    email = models.CharField(max_length=50)
    passwd = models.CharField(max_length=20)
    phoneno = models.CharField(max_length=15, blank=True)
    # FK 설정
    # on_delete = models.CASCADE 하면 혹시나 FK가 지칭하는거 지워지면 항목도
    # 지워지게 설정
    # columnname = models.ForeignKey(Classname, condition)

    def __str__(self):
        return self.username


class Image(models.Model):
    author = models.CharField(max_length=20, default='hello')
    name = models.CharField(max_length=500)
    imagefile = models.FileField(upload_to='images/', null=True, verbose_name="")
    upload_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name + ": " + str(self.imagefile)


class Uploads(models.Model):
    author = models.CharField(max_length=20)
    content = models.CharField(max_length=500)
    imagefile = models.FileField(upload_to='images/')
    upload_date = models.DateTimeField(auto_now=True)

    # def __str__(self):
    #     return self.content + ": " + str(self.imagefile)


class Uploads2(models.Model):
    author = models.CharField(max_length=20)
    content = models.CharField(max_length=500)
    imagefile = models.ImageField(upload_to='images/', blank=True, max_length=200)
    upload_date = models.DateTimeField(auto_now=True)
