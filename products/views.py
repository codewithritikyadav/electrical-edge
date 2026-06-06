from django.shortcuts import render, get_object_or_404
from .models import Book, Category
from orders.models import Order, PaymentRequest


def book_list(request):
    query = request.GET.get('q')
    category_id = request.GET.get('category')

    books = Book.objects.all().order_by('-created_at')
    categories = Category.objects.all()

    if query:
        books = books.filter(title__icontains=query)

    if category_id:
        books = books.filter(category_id=category_id)

    return render(request, 'products/book_list.html', {
        'books': books,
        'categories': categories,
        'query': query,
        'selected_category': category_id
    })


def book_detail(request, id):
    book = get_object_or_404(Book, id=id)

    already_purchased = False
    pending_payment = False

    if request.user.is_authenticated:
        already_purchased = Order.objects.filter(
            user=request.user,
            book=book,
            is_paid=True
        ).exists()

        pending_payment = PaymentRequest.objects.filter(
            user=request.user,
            book=book,
            is_approved=False
        ).exists()

    return render(request, 'products/book_detail.html', {
        'book': book,
        'already_purchased': already_purchased,
        'pending_payment': pending_payment
    })