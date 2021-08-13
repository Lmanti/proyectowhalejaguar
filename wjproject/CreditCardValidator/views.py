from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from CreditCardValidator.validator import *
from CreditCardValidator.luhn import luhnAlgoritm

# Create your views here.

@csrf_exempt
def validatorAPI(request, id = 0):
    if request.method == 'GET':
        return JsonResponse("hola mundo", safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        data["cardNumber"] =data["cardNumber"].replace(" ", "")
        if int(data["cardNumber"][0]) >= 3 and int(data["cardNumber"][0]) <= 6 and luhnAlgoritm(data["cardNumber"]) == "valid":
            if isAmericanExpress(data["cardNumber"]): return JsonResponse({"message": "American Express"}, safe=False)
            elif isChinaTUnion(data["cardNumber"]): return JsonResponse({"message": "China T-Union"}, safe=False)
            elif isChinaUnionPay(data["cardNumber"]): return JsonResponse({"message": "China UnionPay"}, safe=False)
            elif isDinersClubInternational(data["cardNumber"]): return JsonResponse({"message": "Diners Club International"}, safe=False)
            elif isDinersClubUC(data["cardNumber"]): return JsonResponse({"message": "Diners Club United States & Canada"}, safe=False)
            elif isDiscoverCard(data["cardNumber"]): return JsonResponse({"message": "Discover Card"}, safe=False)
            elif isUkrCard(data["cardNumber"]): return JsonResponse({"message": "UkrCard"}, safe=False)
            elif isRuPay(data["cardNumber"]): return JsonResponse({"message": "RuPay"}, safe=False)
            elif isInterPayment(data["cardNumber"]): return JsonResponse({"message": "InterPayment"}, safe=False)
            elif isInstaPayment(data["cardNumber"]): return JsonResponse({"message": "InstaPayment"}, safe=False)
            elif isJCB(data["cardNumber"]): return JsonResponse({"message": "JCB"}, safe=False)
            elif isMaestroUK(data["cardNumber"]): return JsonResponse({"message": "Maestro UK"}, safe=False)
            elif isMaestro(data["cardNumber"]): return JsonResponse({"message": "Maestro"}, safe=False)
            elif isDankort(data["cardNumber"]): return JsonResponse({"message": "Dankort"}, safe=False)
            elif isMIR(data["cardNumber"]): return JsonResponse({"message": "MIR"}, safe=False)
            elif isNPSPridnestrovie(data["cardNumber"]): return JsonResponse({"message": "NPS Pridnestrovie"}, safe=False)
            elif isMastercard(data["cardNumber"]): return JsonResponse({"message": "Mastercard"}, safe=False)
            elif isTroy(data["cardNumber"]): return JsonResponse({"message": "Troy"}, safe=False)
            elif isVisaElectron(data["cardNumber"]): return JsonResponse({"message": "Visa Electron"}, safe=False)
            elif isVisa(data["cardNumber"]): return JsonResponse({"message": "Visa"}, safe=False)
            else: return JsonResponse("El número no pertenece a ninguna franquicia", safe=False)
        else: return JsonResponse("Número inválido", safe=False)