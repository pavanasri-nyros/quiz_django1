from django.contrib import admin
from .models import Quiz, Html2, Html3, Html4, Html5
from .models import Css1, Css2, Css3, Css4, Css5
from .models import Js1, Js2, Js3, Js4, Js5
from .models import Django1, Django2, Django3, Django4, Django5
from .models import Vue1, Vue2, Vue3, Vue4, Vue5,Results
class ResultsAdmin(admin.ModelAdmin):
    list_display = ('id','username','quizname','score')

class Html2admin(admin.ModelAdmin):
    list_display = ('id','name', 'question')

# Register your models here.
admin.site.register(Quiz)
admin.site.register(Html2, Html2admin)
admin.site.register(Html3)
admin.site.register(Html4)
admin.site.register(Html5)
admin.site.register(Css1)
admin.site.register(Css2)
admin.site.register(Css3)
admin.site.register(Css4)
admin.site.register(Css5)
admin.site.register(Js1)
admin.site.register(Js2)
admin.site.register(Js3)
admin.site.register(Js4)
admin.site.register(Js5)
admin.site.register(Django1)
admin.site.register(Django2)
admin.site.register(Django3)
admin.site.register(Django4)
admin.site.register(Django5)
admin.site.register(Vue1)
admin.site.register(Vue2)
admin.site.register(Vue3)
admin.site.register(Vue4)
admin.site.register(Vue5)
admin.site.register(Results,ResultsAdmin)


