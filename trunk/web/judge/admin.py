from django.contrib import admin
from web.judge.models import Contest,Problem,Solution,Onlinejudge

class ContestAdmin(admin.ModelAdmin):
	list_display = ('id', 'title', 'start_time', 'lock_time', 'end_time')
	list_filter = (['start_time','end_time'])#, 'is_running','is_ended')

admin.site.register(Contest,ContestAdmin)
admin.site.register(Problem)
admin.site.register(Solution)
admin.site.register(Onlinejudge)

