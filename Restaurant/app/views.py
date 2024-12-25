from django.shortcuts import render

from app.models import Tiffen, Veglunch, Vegdinner, Nonlunch, Nondinner, Cveglunch, Cnonlunch, Cvegdinner, Cnondinner, \
    Ctiffen


# Create your views here.
def home(request):
    return render(request,'home.html')


def food(request):
    return render(request,'food.html')


def veg(request):
    return render(request,'veg.html')
def nonveg(request):
    return render(request,'nonveg.html')


def breakfast(request):
    t = Tiffen.objects.all()
    data = {'tiffens':t}
    return render(request,'breakfast.html',data)


def veglunch(request):
    vl = Veglunch.objects.all()
    data = {'vegl':vl}
    return render(request,'veglunch.html',data)


def vegdinner(request):
    vd = Vegdinner.objects.all()
    data = {'vegd': vd}
    return render(request,'vegdinner.html',data)


def nonlunch(request):
    nl = Nonlunch.objects.all()
    data = {'nonl':nl}
    return render(request,'nonlunch.html',data)


def nondinner(request):
    nd = Nondinner.objects.all()
    data = {'nond':nd}
    return render(request,'nondinner.html',data)


def chefs(request):
    return render(request,'chefs.html')


def cfood(request):
    return render(request,'cfood.html')


def lunch(request):
    v = Cveglunch.objects.all()
    n = Cnonlunch.objects.all()
    d1 = {'vl':v,'cnl':n}
    return render(request,'clunch.html',d1)


def dinner(request):
    vd = Cvegdinner.objects.all()
    nd = Cnondinner.objects.all()
    d2 = {'vd':vd,'cnd':nd}
    return render(request,'cdinner.html',d2)


def bfast(request):
    cb = Ctiffen.objects.all()
    d3 = {'cb':cb}
    return render(request,'cbreakfast.html',d3)