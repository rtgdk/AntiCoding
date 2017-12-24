from django.shortcuts import render
from .models import Info
from .forms import InfoForm

def index(request):
    context_dict={}
    if request.method == 'POST':
        form = InfoForm(request.POST,request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            context_dict["success"] = "Submitted!"
            form = InfoForm()
            context_dict["form"]= form
            return render(request, 'app/index.html', context_dict)
        else :
            context_dict["error"] = form.errors
            form = InfoForm()
            context_dict["form"] = form
            return render(request,'app/index.html',context_dict)
    else :
        form = InfoForm()
        context_dict["form"] = form
        return render(request, 'app/index.html', context_dict)

