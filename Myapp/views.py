from django.shortcuts import render, redirect
from Myapp.forms import Newuser
from Myapp.models import user
from bs4 import BeautifulSoup
from urllib.request import urlopen


def index(request):
    return render(request, 'Myapp/index.html')


def view1(request):
    form = Newuser
    if request.method == 'POST':
        form = Newuser(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('/view2')
    return render(request, 'Myapp/view1.html', {'form': form})


def view2(request):
    if request.method == 'GET':
        search = request.GET.get('search')
        query1 = user.objects.filter(name__iexact=search)
    return render(request, 'Myapp/view2.html', {'sea': query1})


def view3(request):
    return render(request, 'Myapp/view3.html')


def view31(request):
    link = request.GET.get("input_link")
    fi = test(link)
    my_dict = {'bloat': fi}
    return render(request, 'Myapp/view31.html', my_dict)


def test(theurl):
    thepage = urlopen(theurl).read()
    soup = BeautifulSoup(thepage, "html.parser")
    images = soup.findAll("img")
    for image in images:
        yield image["src"]
