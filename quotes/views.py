from django.shortcuts import render
from django.contrib import messages

from django.shortcuts import render,redirect
from .models import Quote,Quote_Liked
from django.contrib.auth.models import User

# Create your views here.
def quotes(request):
    quotes=Quote.objects.all()
    context={'quotes':quotes}
    
    
    return render(request,"quotes/quotes.html",context)

def my_quotes(request,id):
    poster=User.objects.get(id=id)
    context={
        'the_user':poster
    }
    print(context)
    return render(request,"quotes/my_quotes.html",context)

def delete_quote(request,id):
    quote=Quote.objects.get(id=id)
    print(f"delete this quote{id},{quote.quote}")
    quote.delete()
    return redirect("quotes")

def quote_like(request,id):
    quote_faved=Quote.objects.get(id=id)
    # quote=Quote.objects.get(id=id)
    user=User.objects.get(username=request.user.username)
    quote_faved.favouriting_users.add(user)
    print(f"Like this quote{id},{quote_faved.quote} by {user.id}")
    # quote=Quote_Liked.objects.create(quote_liked=quote,liked_by=user)
    return redirect("quotes")

# post_quote
def post_quote(request):
    # validator
    errors = Quote.objects.validator(request.POST)
    print(errors)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.warning(request, value)
        return redirect("quotes")

    user=User.objects.get(username=request.user.username)
    quote=Quote.objects.create(quote=request.POST['quote'],author=request.POST['author'],poster=user)
    print("quote added****")
    return redirect("quotes")