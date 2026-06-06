from django.contrib import admin
from .models import Order, PaymentRequest


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'book',
        'is_paid',
        'purchased_at'
    )


@admin.register(PaymentRequest)
class PaymentRequestAdmin(admin.ModelAdmin):

    list_display = (
        'user',
        'book',
        'is_approved',
        'submitted_at'
    )

    actions = ['approve_payments']

    def approve_payments(self, request, queryset):

        for payment in queryset:

            if not payment.is_approved:

                payment.is_approved = True
                payment.save()

                Order.objects.get_or_create(
                    user=payment.user,
                    book=payment.book,
                    defaults={
                        'is_paid': True
                    }
                )

    approve_payments.short_description = (
        "Approve selected payments"
    )