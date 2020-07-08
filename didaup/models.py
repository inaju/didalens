from django.db import models
from users.models import CustomUser
from django.utils.translation import ugettext as _

class GoalList(models.Model):
    id = models.AutoField(primary_key=True)
    goal=models.CharField(max_length=100)
    user=models.ForeignKey(CustomUser, verbose_name=_(""), on_delete=models.CASCADE, null=True)

    

    def __str__(self):
        return self.goal


class GoalModel(models.Model):
    id = models.AutoField(primary_key=True)
    user=models.ForeignKey(CustomUser, verbose_name=_(""), on_delete=models.CASCADE, null=True)
    datetogoal=models.ForeignKey(GoalList, on_delete=models.CASCADE, verbose_name='Goal')
    time=models.TimeField(auto_now=True)
    date=models.DateField(auto_now=True)
    is_true=models.BooleanField(default=False, verbose_name='Done')
    is_not_true=models.BooleanField(default=False, verbose_name="Didn't Do")

    def __str__(self):
        return str(self.datetogoal)

    