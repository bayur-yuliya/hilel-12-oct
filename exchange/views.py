from django.http import JsonResponse, HttpResponse

from .models import Rate


def main_view(request):
    response_data = {
        "current_rates": [
            {
                "id": rate.id,
                "date": rate.date,
                "vendor": rate.provider,
                "currency_a": rate.currency_from,
                "currency_b": rate.currency_to,
                "sell": rate.sell,
                "buy": rate.buy,
            }
            for rate in Rate.objects.all()
        ]
    }
    return JsonResponse(response_data)


def calculator(request):
    #  Використовувати валюти з БД, з кращим курсом для користувача.
    return HttpResponse("")
