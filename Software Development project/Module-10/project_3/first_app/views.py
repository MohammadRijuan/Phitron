from django.shortcuts import render
import datetime

# Create your views here.
# we have sent our data to frontend
def home(request):
    d = {'author' : 'Rijuan' ,'age' : 15 , 'lst' : ['python is best'] ,'birthday' :datetime.datetime.now(),'val' :'','courses': [{
        'id' : 1,
        'name' : 'python',

    },
    {
        'id' : 2,
        'name' : 'java',

    },
    {
        'id' : 3,
        'name' : 'cpp',

    }
    ]}
    return render(request,'home.html',context=d)


# when backend has sent its data to frontend that is called context