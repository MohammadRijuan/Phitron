from django.shortcuts import render,redirect
from . forms import StudentData

# Create your views here.

def home(request):
    return render(request,'home.html',)

def student_form(request):
    if request.method == 'POST':
        form = StudentData(request.POST,request.FILES)
        if form.is_valid():
            # this one specially for upload a file
            file=form.cleaned_data['image']
            # to show my file in   upload folder...sob jate accept korte pare tai wb+ dilam
            with open('first_app/upload/' + file.name, 'wb+') as destination:
                
                # we will use chunck so that a bigger file turns into a smaller version
                for chunk in file.chunks():
                    destination.write(chunk)
            print(form.cleaned_data)
    
    else:
        form=StudentData()

    return render(request,'student_form.html',{'form' : form})