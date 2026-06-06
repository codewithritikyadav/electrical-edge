from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from products.models import Book
from .models import Order, PaymentRequest


@login_required
def dashboard(request):

    orders = Order.objects.filter(
        user=request.user,
        is_paid=True
    )

    pending_payments = PaymentRequest.objects.filter(
        user=request.user,
        is_approved=False
    )

    return render(
        request,
        'orders/dashboard.html',
        {
            'orders': orders,
            'pending_payments': pending_payments
        }
    )
@login_required
def manual_payment(request, book_id):

    book = get_object_or_404(Book, id=book_id)

    already_purchased = Order.objects.filter(
        user=request.user,
        book=book,
        is_paid=True
    ).exists()

    if already_purchased:
        return redirect('dashboard')

    pending_payment = PaymentRequest.objects.filter(
        user=request.user,
        book=book,
        is_approved=False
    ).exists()

    if pending_payment:
        return redirect('dashboard')

    if request.method == "POST":

        upi_transaction_id = request.POST.get('upi_transaction_id')
        payment_screenshot = request.FILES.get('payment_screenshot')

        PaymentRequest.objects.create(
            user=request.user,
            book=book,
            upi_transaction_id=upi_transaction_id,
            payment_screenshot=payment_screenshot
        )

        return redirect('payment_success')

    return render(request, 'orders/manual_payment.html', {'book': book})


@login_required
def payment_success(request):
    return render(request, 'orders/payment_success.html')