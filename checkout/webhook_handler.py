from django.http import HttpResponse


class StripeWH_Handler:
    """Handle Stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        """
        intent = event.data.object
        print(intent)
        print(
            f'Handling unknown. Payment Intent ID: {intent.id}')
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment_intent.succeeded webhook from Stripe
        """
        intent = event.data.object
        print(intent)
        print(
            f'Handling payment_intent.succeeded. Payment Intent ID: {intent.id}')
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the payment_intent.payment_failed webhook from Stripe
        """
        intent = event.data.object
        print(intent)
        print(
            f'Handling payment_intent.payment_failed. Payment Intent ID: {intent.id}')
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
