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
