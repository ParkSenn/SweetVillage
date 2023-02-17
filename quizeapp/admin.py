from django.contrib import admin
from .models import Answer, Question, PnuUser

admin.site.register(Answer)
admin.site.register(Question)
admin.site.register(PnuUser)

# Register your models here.
