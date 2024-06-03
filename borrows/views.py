from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from books.models import Book
from .models import Borrow
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from accounts.models import Account

# Create your views here.
@login_required
def borrow_book(request, id):
    if request.method == 'POST':
        book = get_object_or_404(Book, pk=id)
        if book and book.quantity > 0:
           if request.user.account.balance >= book.price:
              book.quantity -= 1
              book.save(update_fields=['quantity'])
              Account.objects.filter(user=request.user).update(balance=request.user.account.balance - book.price)
              Borrow.objects.create(user=request.user, book=book, balance_after_borrow=request.user.account.balance)
              messages.success(request, f"You have successfully Borrowed '{book.title}'")
              return redirect('book_details', book.id)
           else:
               messages.warning(request, "You don't have enough balance please deposit some money")
               return redirect('profile')
        else:
            messages.warning(request, 'Sorry this book is not available!!!')
            return redirect('book_details', book.id)
    else:
        messages.warning(request, 'Something is wrong, please try again')
        return redirect('home')