from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from CreditCardValidator.validator import *
from CreditCardValidator.luhn import luhnAlgoritm

# Create your views here.

@csrf_exempt
def validatorAPI(request, id = 0):

    # El método GET te saluda!
    if request.method == 'GET':
        return JsonResponse("hola querido visitante!", safe=False)
    
    # El método POST recibe el número de la tarjeta como string, lo valida y devuelve la respuesta
    elif request.method == 'POST':

        # Parseamos la request a diccionario
        data = JSONParser().parse(request)

        # Limpiamos la String de espacios
        data["cardNumber"] =data["cardNumber"].replace(" ", "")

        # Sólo las tarjétas que empiezan por 3 hasta 6 son relacionadas al sector de la banca, se valida tambien el número de tarjeta con el algoritmo de Luhn 
        if int(data["cardNumber"][0]) >= 3 and int(data["cardNumber"][0]) <= 6 and luhnAlgoritm(data["cardNumber"]) == "valid":

            # Hacemos la ronda de validaciones para cada una de las tarjetas
            if isAmericanExpress(data["cardNumber"]): return JsonResponse({"message": "American Express"}, safe=False)
            elif isChinaTUnion(data["cardNumber"]): return JsonResponse({"message": "China T-Union"}, safe=False)
            elif isChinaUnionPay(data["cardNumber"]): return JsonResponse({"message": "China UnionPay"}, safe=False)
            elif isDinersClubInternational(data["cardNumber"]): return JsonResponse({"message": "Diners Club International"}, safe=False)
            elif isMastercard(data["cardNumber"]): return JsonResponse({"message": "Mastercard"}, safe=False)
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
            elif isTroy(data["cardNumber"]): return JsonResponse({"message": "Troy"}, safe=False)
            elif isVisaElectron(data["cardNumber"]): return JsonResponse({"message": "Visa Electron"}, safe=False)
            elif isVisa(data["cardNumber"]): return JsonResponse({"message": "Visa"}, safe=False)
            else: return JsonResponse({"message": "El número no pertenece a ninguna franquicia"}, safe=False)
        else: return JsonResponse({"message": "Número inválido"}, safe=False)