from django.contrib import admin
from .models import Quiz, Html2, Quiz3, Quiz4, Quiz5, Results
from .models import Quiz6, Quiz7, Quiz8, Quiz9, Quiz10
from .models import Quiz11, Quiz12,Quiz13,Quiz14,Quiz15,Quiz16,Quiz17,Quiz18,Quiz19,Quiz20

class ResultsAdmin(admin.ModelAdmin):
    list_display = ('id','username','quizname','score','status')

class Html2admin(admin.ModelAdmin):
    list_display = ('id','name', 'question')

# Register your models here.
admin.site.register(Quiz)
admin.site.register(Html2, Html2admin)
admin.site.register(Quiz3)
admin.site.register(Quiz4)
admin.site.register(Quiz5)
admin.site.register(Quiz6)
admin.site.register(Quiz7)
admin.site.register(Quiz8)
admin.site.register(Quiz9)
admin.site.register(Quiz10)


admin.site.register(Quiz11)
admin.site.register(Quiz12)
admin.site.register(Quiz13)
admin.site.register(Quiz14)
admin.site.register(Quiz15)
admin.site.register(Quiz16)
admin.site.register(Quiz17)
admin.site.register(Quiz18)
admin.site.register(Quiz19)
admin.site.register(Quiz20)
admin.site.register(Results,ResultsAdmin)


