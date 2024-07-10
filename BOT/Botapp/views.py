from django.shortcuts import render
from Botapp.form import Sform
def Bot(request):
    submit=False
    s=Sform()
    name=""
    mark=""
    bot=""
    if(request.method=='POST'):
        s=Sform(request.POST)
        if(s.is_valid()):
            name=s.cleaned_data['name']
            mark=s.cleaned_data['mark']
            bot=s.cleaned_data['bot_handle']
            print("submited")

    
    return render(request,'Pages/index.html',{"s":s,"mark":mark,"name":name,"bot":bot})


