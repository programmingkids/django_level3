from django import forms

from .models import Player
from .models import Job
from .models import User

from .validates import check_name


class MyModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.name


class PlayerForm (forms.ModelForm) :
    class Meta:
        model = Player
        fields = ['name','hp','mp','job']

    name = forms.CharField(
        label = "名前",
        widget = forms.TextInput(attrs={"class" : "form-control"}))
        
    hp = forms.IntegerField(
        label = "HP",
        widget = forms.NumberInput(attrs={"class" : "form-control"}))
        
    mp = forms.IntegerField(
        label = "MP",
        widget = forms.NumberInput(attrs={"class" : "form-control"}))

    job = MyModelChoiceField(
        label = "職業",
        empty_label = "選択してください",
        queryset = Job.objects.all(),
        widget = forms.Select(attrs={"class" : "form-control"}))


class UserForm (forms.ModelForm) :
    class Meta:
        model = User
        fields = ['name','email','age','hobby']

    name = forms.CharField(
        label = "名前",
        #required = False,
        #min_length = 3,
        #max_length = 6,
        #validators = [
        #    check_name
        #],
        widget = forms.TextInput(attrs={"class" : "form-control"}))
        
    email = forms.EmailField(
        label = "メール",
        #required = False,
        #min_length = 3,
        #max_length = 10,
        widget = forms.TextInput(attrs={"class" : "form-control"}))

    age = forms.IntegerField(
        label = "年齢",
        #required = True,
        #min_value = 10,
        #max_value = 20,
        #error_messages={
        #    "required"   : "絶対入力してね",
        #    "min_value"  : "10以上だよ",
        #    "max_value"  : "20以下だよ",
        #    "invalid"    : "整数を入力してください",
        #},
        widget = forms.NumberInput(attrs={"class" : "form-control"}))
        
    hobby = forms.CharField(
        label = "趣味",
        widget = forms.TextInput(attrs={"class" : "form-control"}))
    
    """
    def clean_name(self):
        name = self.cleaned_data["name"]
        if "山田" in name :
            raise forms.ValidationError("山田はダメだよ")
        return name
    """
    
    """
    def clean_age(self):
        age = self.cleaned_data["age"]
        if age == 15 :
            raise forms.ValidationError("15歳はNGです")
        return age
    """
    
    """
    def clean(self):
        cleaned_data = super().clean()
        if "name" in cleaned_data and "hobby" in cleaned_data and cleaned_data["name"] == cleaned_data["hobby"] :
            raise forms.ValidationError("名前と趣味が同じはダメだよ")
        return cleaned_data
    """
