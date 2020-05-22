from rest_framework import serializers
from .models import Quiz, Html2, Html3, Html4, Html5
from .models import Css1, Css2, Css3, Css4, Css5
from .models import Js1,Js2, Js3, Js4, Js5
from .models import Django1,Django2, Django3, Django4, Django5
from .models import Vue1,Vue2, Vue3, Vue4, Vue5






class QuizSerializers(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = ('id','slug','question','option1','option2','option3','option4','correct_answer')


#html2
class Html2Serializers(serializers.ModelSerializer):
    class Meta:
        model = Html2
        fields = ('id','slug','question','option1','option2','option3','option4','answer')


class Html3Serializers(serializers.ModelSerializer):
    class Meta:
        model = Html3
        fields = ('id','slug','question','option1','option2','option3','option4','answer')


class Html4Serializers(serializers.ModelSerializer):
    class Meta:
        model = Html4
        fields = ('id','slug','question','option1','option2','option3','option4','answer')

class Html5Serializers(serializers.ModelSerializer):
    class Meta:
        model = Html5
        fields = ('id','name','slug','question','option1','option2','option3','option4','answer')


class Css1Serializers(serializers.ModelSerializer):
    class Meta:
        model = Css1
        fields = ('id','name','slug','question','option1','option2','option3','option4','answer')

class Css2Serializers(serializers.ModelSerializer):
    class Meta:
        model = Css2
        fields = ('id','name','slug','question','option1','option2','option3','option4','answer')


class Css3Serializers(serializers.ModelSerializer):
    class Meta:
        model = Css3
        fields = ('id','name','slug','question','option1','option2','option3','option4','answer')

class Css4Serializers(serializers.ModelSerializer):
    class Meta:
        model = Css4
        fields = ('id','name','slug','question','option1','option2','option3','option4','answer')

class Css5Serializers(serializers.ModelSerializer):
    class Meta:
        model = Css5
        fields = ('id','name','slug','question','option1','option2','option3','option4','answer')

#javascript
class Js1Serializers(serializers.ModelSerializer):
    class Meta:
        model = Js1
        fields = ('id','name','slug','question','option1','option2','option3','option4','answer')

class Js2Serializers(serializers.ModelSerializer):
    class Meta:
        model = Js2
        fields = ('id','name','slug','question','option1','option2','option3','option4','answer')

class Js3Serializers(serializers.ModelSerializer):
    class Meta:
        model = Js3
        fields = ('id','name','slug','question','option1','option2','option3','option4','answer')

class Js4Serializers(serializers.ModelSerializer):
    class Meta:
        model = Js4
        fields = ('id','name','slug','question','option1','option2','option3','option4','answer')

class Js5Serializers(serializers.ModelSerializer):
    class Meta:
        model = Js5
        fields = ('id','name','slug','question','option1','option2','option3','option4','answer')


#django
class Django1Serializers(serializers.ModelSerializer):
    class Meta:
        model = Django1
        fields = ('id','name','slug','question','option1','option2','option3','option4','answer')

class Django2Serializers(serializers.ModelSerializer):
    class Meta:
        model = Django2
        fields = ('id','name','slug','question','option1','option2','option3','option4','answer')

class Django3Serializers(serializers.ModelSerializer):
    class Meta:
        model = Django3
        fields = ('id','name','slug','question','option1','option2','option3','option4','answer')

class Django4Serializers(serializers.ModelSerializer):
    class Meta:
        model = Django4
        fields = ('id','name','slug','question','option1','option2','option3','option4','answer')

class Django5Serializers(serializers.ModelSerializer):
    class Meta:
        model = Django5
        fields = ('id','name','slug','question','option1','option2','option3','option4','answer')


#Vuejs
class Vue1Serializers(serializers.ModelSerializer):
    class Meta:
        model = Vue1
        fields = ('id','name','slug','question','option1','option2','option3','option4','answer')

class Vue2Serializers(serializers.ModelSerializer):
    class Meta:
        model = Vue2
        fields = ('id','name','slug','question','option1','option2','option3','option4','answer')

class Vue3Serializers(serializers.ModelSerializer):
    class Meta:
        model = Vue3
        fields = ('id','name','slug','question','option1','option2','option3','option4','answer')

class Vue4Serializers(serializers.ModelSerializer):
    class Meta:
        model = Vue4
        fields = ('id','name','slug','question','option1','option2','option3','option4','answer')

class Vue5Serializers(serializers.ModelSerializer):
    class Meta:
        model = Vue5
        fields = ('id','name','slug','question','option1','option2','option3','option4','answer')
