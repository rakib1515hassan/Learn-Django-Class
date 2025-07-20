from django.shortcuts import render


def home(request):
    name = "Md Rakib Hassan"
    age = 30
    mylist = ["apple", "banana", "cherry"]
    mytuple = ("apple", "banana", "cherry")

    thisdict = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
    }

    context = {
        "name": name,
        "age": age,
        "mylist": mylist,
        "mytuple": mytuple,
        "thisdict": thisdict
    }
    return render(request, 'index.html', context)


def product(request):
    return render(request, "product.html")