from django.shortcuts import redirect, render
from .forms import UserRegisterForm

def index(request):
    if request.method=='POST':
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(request,'contents/thankyou.html')
    else:
        form=UserRegisterForm()

    return render(request,'contents/home.html',{'form':form})