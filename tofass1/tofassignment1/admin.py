from django.contrib import admin
from .models import info,voterinfo,votercred,distrcred,constcred
# Register your models here.
admin.site.register(info)
admin.site.register(voterinfo)
admin.site.register(distrcred)
admin.site.register(constcred)
admin.site.register(votercred)

