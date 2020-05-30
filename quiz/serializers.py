from rest_framework import serializers
from .models import Quiz, Html2, Quiz3, Quiz4, Quiz5
from .models import Quiz6, Quiz7, Quiz8, Quiz9, Quiz10, Quiz11, Quiz12,Quiz13,Quiz14,Quiz15,Quiz16,Quiz17,Quiz18,Quiz19,Quiz20



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
        model = Quiz3
        fields = ('id','slug','question','option1','option2','option3','option4','answer')


class Html4Serializers(serializers.ModelSerializer):
    class Meta:
        model = Quiz4
        fields = ('id','slug','question','option1','option2','option3','option4','answer')

class Html5Serializers(serializers.ModelSerializer):
    class Meta:
        model = Quiz5
        fields = ('id','name','slug','question','option1','option2','option3','option4','answer')


class Css1Serializers(serializers.ModelSerializer):
    class Meta:
        model = Quiz6
        fields = ('id','name','slug','question','option1','option2','option3','option4','answer')

class Css2Serializers(serializers.ModelSerializer):
    class Meta:
        model = Quiz7
        fields = ('id','name','slug','question','option1','option2','option3','option4','answer')


class Css3Serializers(serializers.ModelSerializer):
    class Meta:
        model = Quiz8
        fields = ('id','name','slug','question','option1','option2','option3','option4','answer')

# javascript

class Quiz9Serializers(serializers.ModelSerializer):
    class Meta:
        model = Quiz9
        fields = ('id','name','slug','question','option1','option2','option3','option4','answer')


class Quiz10Serializers(serializers.ModelSerializer):
    class Meta:
        model = Quiz10
        fields = ('id','name','slug','question','option1','option2','option3','option4','answer')


class Quiz11Serializers(serializers.ModelSerializer):
    class Meta:
        model = Quiz11
        fields = ('id','name','slug','question','option1','option2','option3','option4','answer')

class Quiz12Serializers(serializers.ModelSerializer):
    class Meta:
        model = Quiz12
        fields = ('id','name','slug','question','option1','option2','option3','option4','answer')


class Quiz13Serializers(serializers.ModelSerializer):
    class Meta:
        model = Quiz13
        fields = ('id','name','slug','question','option1','option2','option3','option4','answer')

class Quiz14Serializers(serializers.ModelSerializer):
    class Meta:
        model = Quiz14
        fields = ('id','name','slug','question','option1','option2','option3','option4','answer')

class Quiz15Serializers(serializers.ModelSerializer):
    class Meta:
        model = Quiz15
        fields = ('id','name','slug','question','option1','option2','option3','option4','answer')

class Quiz16Serializers(serializers.ModelSerializer):
    class Meta:
        model = Quiz16
        fields = ('id','name','slug','question','option1','option2','option3','option4','answer')

class Quiz17Serializers(serializers.ModelSerializer):
    class Meta:
        model = Quiz17
        fields = ('id','name','slug','question','option1','option2','option3','option4','answer')

class Quiz18Serializers(serializers.ModelSerializer):
    class Meta:
        model = Quiz18
        fields = ('id','name','slug','question','option1','option2','option3','option4','answer')

class Quiz19Serializers(serializers.ModelSerializer):
    class Meta:
        model = Quiz19
        fields = ('id','name','slug','question','option1','option2','option3','option4','answer')

class Quiz20Serializers(serializers.ModelSerializer):
    class Meta:
        model = Quiz20
        fields = ('id','name','slug','question','option1','option2','option3','option4','answer')
