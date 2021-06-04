from django import forms


def check_name(value) :
    if value == "佐藤":
        raise forms.ValidationError("佐藤ではだめですよ")
