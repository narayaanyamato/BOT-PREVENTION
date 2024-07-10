from django import forms

class Sform(forms.Form):
    name=forms.CharField()
    mark=forms.IntegerField()
    bot_handle=forms.CharField(required=False,widget=forms.HiddenInput)

    def clean(self):
        print("vlidating")
        data=super().clean()
        name=data['name']
        mark=data['mark']
        bot=data['bot_handle']
             raise forms.ValidationError("Request from BOT....can't submit")
             return data
