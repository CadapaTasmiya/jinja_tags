from django.shortcuts import render

# Create your views here.
def jinja_print(request):
    d={'name':'NAWAZ KHAN','age':7}
    return render(request,'jinja_print.html',context=d)