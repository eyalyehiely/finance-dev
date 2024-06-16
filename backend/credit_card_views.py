from django.shortcuts import get_object_or_404
import jwt,datetime,json
from django.http import  JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import *
import logging
from django.utils import timezone
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.decorators import login_required
from rest_framework import status



current_datetime = timezone.now()
current_month = current_datetime.month
current_year = current_datetime.year
current_day = current_datetime.day
logger = logging.getLogger('backend')




#add
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_credit_card(request):
    try:
        user_id= request.user.id
        user = CustomUser.objects.get(id=user_id)
        request.data['user'] = user.id
        request.data['family'] = user.family_id

        serializer = CreditCardSerializer(data=request.data)
        if serializer.is_valid():
            card = serializer.save()
            logger.debug('Credit card added')
            return Response({'successful': 'Credit card added'})
        else:
            logger.debug(f'Credit card not added: {str(e)}')
            return Response({'error': str(e)}, status=500)
        
    except CustomUser.DoesNotExist:
        return Response({'error': 'User does not exist'}, status=404)
    except Exception as e:
        logger.debug(f'Credit card not added: {str(e)}')
        return Response({'error': str(e)}, status=500)
    


#delete
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_credit_card(request, credit_card_id):
    try:
        credit_card = CreditCard.objects.get(id=credit_card_id)
        credit_card.delete()
        return Response({"message": "Credit card deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
    except CreditCard.DoesNotExist:
        return Response({"error": "Credit card not found"}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


#get all credit cards per user
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def get_credit_card(request):
    user_id= request.user.id
    try:
        
        credit_cards = CreditCard.objects.filter(user_id=user_id)
        serializer = CreditCardSerializer(credit_cards,many=True)
        return Response({
        'status':200,
        'credit_cards':serializer.data,
        })
        
    except Exception as e:
        print(f"Error: {str(e)}")  # Debug: Print the error message
        return Response({
            'status': 500,
            'message': 'An error occurred while fetching data.',
            'error': str(e)
        }, status=500)
    






#get chosen card
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_chosen_credit_card(request,card_id):
    user_id= request.user.id
    try:
        
        credit_card = CreditCard.objects.filter(user_id=user_id)
        serializer = CreditCardSerializer(credit_card)
        return Response({
        'status':200,
        'chosen_card':serializer.data,
        })
        
    except Exception as e:
        print(f"Error: {str(e)}")  # Debug: Print the error message
        return Response({
            'status': 500,
            'message': 'An error occurred while fetching data.',
            'error': str(e)
        }, status=500)
    
    except CreditCard.DoesNotExist:
        return Response({"error": "Credit card not found"}, status=status.HTTP_404_NOT_FOUND)

# -------------------------------------------------------------------------------
    # TODO: fix this view
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def reset_credit_card_transactions(self):
    today = timezone.now()
    day_of_month = today.day
    time = day_of_month.strftime("%00:%00")
    if day_of_month == 1 & time:
        CreditCard.credit_left = CreditCard.line_of_credit
        CreditCard.debit_left = 0
        CreditCard.amount_to_charge = 0









