from django.shortcuts import render, HttpResponse, redirect
from .models import Item

# Create your views here.

def index(request):
    return render(request, 'amadon/index.html', {"items": Item.objects.all()})

def buy(request):
    if request.method == 'POST':
        if 'total_spent' in request.session:
            request.session['total_spent'] = request.session['total_spent']
        else:
            request.session['total_spent'] = 0
        if 'item_count' in request.session:
            request.session['item_count'] = request.session['item_count']
        else:
            request.session['item_count'] = 0
        item = Item.objects.get(id=request.POST['item_id'])
        request.session['item'] = item.name
        request.session['price'] = item.price * float(request.POST['quantity'])
        request.session['total_spent'] = float(request.session['total_spent']) + item.price
        request.session['item_count'] = int(request.session['item_count']) + int(request.POST['quantity'])
        return redirect('/amadon/checkout/')
    else:
        return redirect('/')

def checkout(request):
    return render(request, 'amadon/checkout.html')
