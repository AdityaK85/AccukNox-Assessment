from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated  
from rest_framework_simplejwt.authentication import JWTAuthentication 
from rest_framework.decorators import api_view , permission_classes, authentication_classes, throttle_classes
from django.views.decorators.csrf import csrf_exempt
from .models import *
from Project_utilty.authenticate_pair import *
from Project_utilty.regex_validator import *
from .serializer import *
from datetime import datetime
from django.db.models import Q

# ############################### User Login/Signup API ##############################
'''

User Login/Signup

• Users should be able to login with their email and password(email should be case insensitive)

• User should be able to signup with their email only(no otp verification required, valid email format is sufficient)

• Except signup and login every api should be called for authenticated users only

'''



@api_view(['POST'])
@csrf_exempt
def user_login(requst):
    try:
        email = requst.data.get('email')
        password = requst.data.get('password')
        response = {'status':403, 'msg':"Please enter valid email"}

        if re_validate_email(email):
            if Userdetails.objects.filter(email = email , password = password ).exists():
                user = Userdetails.objects.filter(email = email, password = password).last()
                api_token = MyTokenObtainPairSerializer().validate(user)
                response = {'status':200, 'msg': 'Login Successfully...', 'api_token': api_token }
            else:
                response = {'status':403, 'msg': 'Invalid Credentials' }
    except:
        response = {'status':403, 'msg':"Something went wrong"}
    return JsonResponse(response)



@api_view(['POST'])
@csrf_exempt
def user_signup(request):
    try:
        name = request.data.get('name')
        email = request.data.get('email')
        password = request.data.get('password')
        response = {'status':403, 'msg':"Please enter valid email"}

        if re_validate_email(email):
            if Userdetails.objects.filter(email = email).exists():
                response = {'status':403, 'msg':"Email Already Registered !Please login"}

            else:
                user = Userdetails.objects.create(name = name, email = email, password = password , created_dt = datetime.now())
                api_token = MyTokenObtainPairSerializer().validate(user)
                response = {'status':200, 'msg':"Register successfully", "api_token": api_token}
    except:
        response = {'status':403, 'msg':"Something went wrong"}
    return JsonResponse(response)




# ############################### Search & Get User API ##############################
'''

Develop API for following functionalities:
• API to search other users by email and name(paginate up to 10 records per page).

a) If search keyword matches exact email then return user associated with the
    email.

b) If the search keyword contains any part of the name then return a list of all
    users.
    eg:- Amarendra, Amar, aman, Abhirama are three users and if users search with "am"
    then all of these users should be shown in the search result because "am"
    substring is part of all of these names.

c) There will be only one search keyword that will search either by name or email.


'''


@api_view(['POST']) 
@permission_classes((IsAuthenticated,)) 
@authentication_classes((JWTAuthentication,))
@csrf_exempt
def get_user_by_email(request):
    try:
        email = request.data.get('email')
        response = {'status':403, 'msg':"Enter Valid Email"}
        if re_validate_email(email):
            if  Userdetails.objects.filter(email = email).exists():
                user_obj = Userdetails.objects.filter(email = email)
                serializer = UserdetailsSerializer(user_obj , many = True)
                match_msg = f'{user_obj.count()} Matches Found'
                response = {'stauts': 200, 'msg': match_msg , 'payload': serializer.data}
            else:
                response = {'stauts': 403, 'msg': 'No matches found'}
    except:
        response = {'status':403, 'msg':"Something went wrong"}
    return JsonResponse(response)



@api_view(['POST']) 
@permission_classes((IsAuthenticated,)) 
@authentication_classes((JWTAuthentication,))
@csrf_exempt
def get_user_by_name(request):
    try:
        name = request.data.get('name')
        page = request.data.get('page') if request.data.get('page') else 1

        per_page = 10
        start = (page - 1) * per_page
        end = start + per_page

        response = {'status':403, 'msg':"Enter Valid Email"}

        if  Userdetails.objects.filter(Q(name__icontains = name) | Q(email__icontains = name)).exists():
            user_obj = Userdetails.objects.filter(Q(name__icontains = name) | Q(email__icontains = name))[start:end]

            serializer = UserdetailsSerializer(user_obj , many = True)
            match_msg = f'{user_obj.count()} Matches Found'

            response = {'stauts': 200, 'msg': match_msg , 'payload': serializer.data}
        else:
            response = {'stauts': 403, 'msg': 'No matches found'}

    except:
        response = {'status':403, 'msg':"Something went wrong"}
    return JsonResponse(response)



@api_view(['POST']) 
@permission_classes((IsAuthenticated,)) 
@authentication_classes((JWTAuthentication,))
@throttle_classes([UserMinuteThrottle])
@csrf_exempt
def send_frnd_request(request):
    try:
        user_id = request.data.get('user_id')
        request_user_id = request.data.get('request_user_id')   # Request Send user ID
        response = {'status':403, 'msg':'Something went wrong'}

        if not Userdetails.objects.filter(id = user_id).exists():
            return JsonResponse({'status':403, 'msg':"User not available"}) 

        elif not Userdetails.objects.filter(id = request_user_id).exists():
            return JsonResponse({'status':403, 'msg':"User not available"})

        else:
            if FrndRequest.objects.filter(fk_user_id = user_id, fk_request_user_id = request_user_id):
                response = {'status':200, 'msg':'Request already sent'}

            else:
                FrndRequest.objects.create(fk_user_id = user_id, fk_request_user_id = request_user_id, created_dt = datetime.now() )
                response = {'status':200, 'msg':'Friend request sent'}
    except:
        response = {'status':403, 'msg':'Something went wrong'}
    return JsonResponse(response)



'''
API to list friends(list of users who have accepted friend request)
List pending friend requests(received friend request)

'''

@api_view(['POST']) 
@permission_classes((IsAuthenticated,)) 
@authentication_classes((JWTAuthentication,))
@csrf_exempt
def my_requests(request):
    type = request.data.get('type') # Accepted / Rejected / Pending
    user_id = request.data.get('user_id')
    obj = FrndRequest.objects.filter(fk_request_user_id = user_id , request_status = type )
    searilzer = FrndRequestSerializer(obj, many=True)
    res_msg = f'{type} Request ' 
    return JsonResponse({'status':200, 'msg' : res_msg , 'payload': searilzer.data})


@api_view(['POST']) 
@permission_classes((IsAuthenticated,)) 
@authentication_classes((JWTAuthentication,))
@csrf_exempt
def accept_reject_request(request):
    type = request.data.get('type')    # Accepted / Rejected
    user_id = request.data.get('user_id')
    request_user_id = request.data.get('request_user_id')
    FrndRequest.objects.filter(fk_request_user_id = user_id , fk_user_id = request_user_id ).update(request_status = type)
    res_msg = f'Request {type}'
    return JsonResponse({'status':200, 'msg': res_msg})



