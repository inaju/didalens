from django.contrib import admin
from .models import GoalList, GoalModel

# Register your models here.
admin.site.register(GoalList)
admin.site.register(GoalModel)