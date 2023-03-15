from django.shortcuts import render

# Create your views here.
def condition(request):
    d={"name":'gangadhara',"a":200,"b":300,"c":40}
    return render(request,"condition.html",d)