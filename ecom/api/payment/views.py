from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import  csrf_exempt
import braintree
# Create your views here.
import braintree

gateway = braintree.BraintreeGateway(
  braintree.Configuration(
    environment=braintree.Environment.Sandbox,
    merchant_id='yw9kyv984hdkqvtr',
    public_key='55t7yftz4m4ghty6',
    private_key='631c8f5341b2c49028cff22375e1ff29'
  )
)

def validate_user_session(id, token): #to ensure that only validated users can make payments
    UserModel = get_user_model()

    try:
        user = UserModel.objects.get(pk = id)
        if user.session_token == token:
            return True
        return False
    except UserModel.DoesNotExist:
        return False

@csrf_exempt
def generate_token(request,id,token):
    if not validate_user_session(id,token):
        return JsonResponse({'error':'Invalid Session,login again'})
    return JsonResponse({'clientToken': gateway.client_token.generate(),'sucess':True})

@csrf_exempt
def process_payment(request,id,token):
    if not validate_user_session(id,token):
        return JsonResponse({'error':'Invalid Session,login again'})

    nonce_from_the_client = request.POST["paymentMethodNonce"]
    amount_from_the_client = request.POST["amount"]

    result = gateway.transaction.sale({
        "amount": "10.00",
        "payment_method_nonce": nonce_from_the_client,
        #"device_data": device_data_from_the_client,
        "options": {
            "submit_for_settlement": True
        }
    })
    print("The payment result is")
    print(result)
    if result.is_success:
        return JsonResponse({
            'success':result.is_success,
            'transaction':{'id':result.transaction.id,'amount':result.transaction.amount}
        })
    else:
        return JsonResponse({'error':True,'success':False})