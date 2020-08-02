from django.db import models

# Create your models here.
class T2(models.Model):
    id = models.BigAutoField(primary_key=True)
    n_star = models.IntegerField()
    short = models.CharField(max_length=1000)

    # 元数据，不属于任何一个字段的数据
    class Meta:
        managed = True
        db_table = 't2'