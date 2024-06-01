# AccukNox Assessment Test Completed 
## Project Installation Guide
- Clone this repository
- Install required packages : pip install -r requirements.txt
- Activate env : .\env\Scripts\activate
- Run application : python manage.py runserver 


## USE API IN POSTMAN 
### POSTMEN SETUP 
- Import API Collections
- Click on import button
- Enter this link in the input field : https://api.postman.com/collections/35427381-b3080f3b-c9c9-4c5e-af66-67d33690a7ca?access_key=PMAT-01HZ91TPWARS3S8BX9D47A5YJN


### DIRECT POSTMEN ACCESS
- **URL** : https://elements.getpostman.com/redirect?entityId=35427381-b3080f3b-c9c9-4c5e-af66-67d33690a7ca&entityType=collection



## API GUIDE 
> [!NOTE]

```
> User Login/Signup
> • Users should be able to login with their email and password(email should be case insensitive)
> • User should be able to signup with their email only(no otp verification required, valid email format is sufficient)
> • Except signup and login every api should be called for authenticated users only
> 1 Develop API for following functionalities:
> • API to search other users by email and name(paginate up to 10 records per page).
> a) If search keyword matches exact email then return user associated with the email.
> b) If the search keyword contains any part of the name then return a list of all users.
eg:- Amarendra, Amar, aman, Abhirama are three users and if users search with "am"
then all of these users should be shown in the search result because "am"
substring is part of all of these names.
c) There will be only one search keyword that will search either by name or email.
• API to send/accept/reject friend request
• API to list friends(list of users who have accepted friend request)
• List pending friend requests(received friend request)
• Users can not send more than 3 friend requests within a minute.
```

### API's Endpoints

**BASE URL : http://127.0.0.1:8000**


```python

**User Login**  :   
                End point : /user_login/
                Content-Type : application/json
                Request Body :  {
                                    "email":"adityakotheakr79@gmail.com",
                                    "password":"pass123"
                                }
                ________________________________________________________________RESPONSE________________________________________________________
                Response :
                          Success Response : 
                                  {
                                      "status": 200,
                                      "msg": "Login Successfully...",
                                      "api_token": {
                                          "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjM5NjkyNCwiaWF0IjoxNzE3MjEyOTI0LCJqdGkiOiJiNmFhYWM0NWNhMTA0NmQ3OTJmNTk0ZGY3MDFhODg4NSIsInVzZXJfaWQiOjF9.5NhHo9G8sjmOuIZCge3tdtXCAXGtifrxldxfM9-q4Uk",
                                          "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE5ODA0OTI0LCJpYXQiOjE3MTcyMTI5MjQsImp0aSI6IjgzMjQzZTI0MWMwZjQwMzE5YmNlNzRhOTI1ZDRmZjM4IiwidXNlcl9pZCI6MX0.sFdHRJEoDwvZxxCBGg_t0t1YX661KiWthHEqHJxY7sw"
                                      }
                                  }

                            Failed Response :
                                    {
                                          'status':403, 
                                          'msg': 'Invalid Credentials' 
                                    }




```


**Sign Up API**

```python

**User Signup**  :   
                End point : /user_signup/
                Content-Type : application/json
                Request Body :  {
                                    "name":"vedant",
                                    "email":"vedant@gmail.com",
                                    "password":"123456"
                                }
                ________________________________________________________________RESPONSE________________________________________________________
                Response :
                          Success Response : 
                                  {
                                      "status": 200,
                                      "msg": "Register successfully",
                                      "api_token": {
                                          "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjM5Nzk4NywiaWF0IjoxNzE3MjEzOTg3LCJqdGkiOiI1MWY1NzBjMDE5OWM0MTk1OGY2YWQzYTBiMGI2OWMxOCIsInVzZXJfaWQiOjEzfQ.DePDEgpDfNmfaeVy-0htqri54x7bOuADI98PIEeBu4A",
                                          "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE5ODA1OTg3LCJpYXQiOjE3MTcyMTM5ODcsImp0aSI6IjRmNTIwNTE2ODk4ZDRhOWNiMTFjYzNjODUzMGRmZDA3IiwidXNlcl9pZCI6MTN9.advJTAraR1Oo5Zh7ly-942B-psiIu1eWjO2QqTQDDzA"
                                      }
                                  }

                            Failed Response :
                                    Response 1 : 
                                              {
                                                  "status": 403,
                                                  "msg": "Email Already Registered !Please login"
                                              }
                                    Response 2 :
                                              {
                                                  "status": 403,
                                                  "msg": "Something went wrong"
                                              }


```




**Get User By Email API**

```python

**Get User By Email**  :   
                End point : /get_user_by_email/
                Content-Type : application/json
                Authorization : 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE5NzY2MTE0LCJpYXQiOjE3MTcxNzQxMTQsImp0aSI6IjE5YWM4NDgzNTk3ZjRiMTZhYWVhMzgxNTIxYTAxNTgyIiwidXNlcl9pZCI6MX0.yqzWu9HsReArIKoKVmccRpvNCIqMDvas8tTY2zhmjnk'

                Request Body :  {
                                    "email":"vedantkothekar@gmail.com"
                                }
                ________________________________________________________________RESPONSE________________________________________________________
                Response :
                          Success Response : 
                                  {
                                      "stauts": 200,
                                      "msg": "1 Matches Found",
                                      "payload": [
                                          {
                                              "id": 2,
                                              "name": "vedant",
                                              "email": "vedantkothekar@gmail.com",
                                              "password": "123456",
                                              "created_dt": "2024-05-31T22:57:32.701403Z"
                                          }
                                      ]
                                  }

                            Failed Response :
                                    Response 1 :
                                              {
                                                  "status": 403,
                                                  "msg": "Something went wrong"
                                              }


```

**Get User By Name API**

```python

**Get User By Name**  :   
                End point : /get_user_by_name/
                Content-Type : application/json
                Authorization : 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE5NzY2MTE0LCJpYXQiOjE3MTcxNzQxMTQsImp0aSI6IjE5YWM4NDgzNTk3ZjRiMTZhYWVhMzgxNTIxYTAxNTgyIiwidXNlcl9pZCI6MX0.yqzWu9HsReArIKoKVmccRpvNCIqMDvas8tTY2zhmjnk'

                Request Body :  {
                                    "name":"an",
                                    "page":1
                                }
                ________________________________________________________________RESPONSE________________________________________________________
                Response :
                          Success Response : 
                                  {
                                    "stauts": 200,
                                    "msg": "7 Matches Found",
                                    "payload": [
                                        {
                                            "id": 2,
                                            "name": "vedant",
                                            "email": "vedantkothekar@gmail.com",
                                            "password": "123456",
                                            "created_dt": "2024-05-31T22:57:32.701403Z"
                                        },
                                        {
                                            "id": 5,
                                            "name": "aman",
                                            "email": "aman54656@gmail.com",
                                            "password": "123456",
                                            "created_dt": "2024-05-31T22:58:22.873457Z"
                                        },
                                        {
                                            "id": 8,
                                            "name": "Anavawar",
                                            "email": "anwarsns0000875@gmail.com",
                                            "password": "123456",
                                            "created_dt": "2024-05-31T23:09:43.776456Z"
                                        },
                                        {
                                            "id": 9,
                                            "name": "Anna",
                                            "email": "anna@gmail.com",
                                            "password": "123456",
                                            "created_dt": "2024-05-31T23:09:57.525203Z"
                                        },
                                        {
                                            "id": 10,
                                            "name": "anmol",
                                            "email": "anmoldev156@gmail.com",
                                            "password": "123456",
                                            "created_dt": "2024-05-31T23:11:41.663361Z"
                                        },
                                        {
                                            "id": 12,
                                            "name": "afjanl",
                                            "email": "afjanl325@gmail.com",
                                            "password": "123456",
                                            "created_dt": "2024-05-31T23:12:08.483845Z"
                                        },
                                        {
                                            "id": 13,
                                            "name": "vedant",
                                            "email": "vedant@gmail.com",
                                            "password": "123456",
                                            "created_dt": "2024-06-01T09:23:07.746657Z"
                                        }
                                    ]
                                }

                            Failed Response :

                                    Response 1 :
                                              {
                                                  "stauts": 403,
                                                  "msg": "No matches found"
                                              }

                                    Response 2 :
                                              {
                                                  "status": 403,
                                                  "msg": "Something went wrong"
                                              }


```



**Send Friend Request API (Only 3 Hits In a Minute)**

```python

**Send Friend Request**  :   
                End point : /send_frnd_request/
                Content-Type : application/json
                Authorization : 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE5NzY2MTE0LCJpYXQiOjE3MTcxNzQxMTQsImp0aSI6IjE5YWM4NDgzNTk3ZjRiMTZhYWVhMzgxNTIxYTAxNTgyIiwidXNlcl9pZCI6MX0.yqzWu9HsReArIKoKVmccRpvNCIqMDvas8tTY2zhmjnk'

                Request Body :  {
                                    "user_id": 4,
                                    "request_user_id": 3
                                }
                ________________________________________________________________RESPONSE________________________________________________________
                Response :
                          Success Response : 
                                  {
                                      "status": 200,
                                      "msg": "Friend request sent"
                                  }

                            Failed Response :
                                    Response 1 :
                                              {
                                                  "status": 200,
                                                  "msg": "Request already sent"
                                              }
                                    Response 2 :
                                              {
                                                  "status": 403,
                                                  "msg": "Something went wrong"
                                              }


```

**Accept & Reject Friend Request API**

```python

**Accept & Reject Friend Request**  :   
                End point : /accept_reject_request/
                Content-Type : application/json
                Authorization : 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE5NzY2MTE0LCJpYXQiOjE3MTcxNzQxMTQsImp0aSI6IjE5YWM4NDgzNTk3ZjRiMTZhYWVhMzgxNTIxYTAxNTgyIiwidXNlcl9pZCI6MX0.yqzWu9HsReArIKoKVmccRpvNCIqMDvas8tTY2zhmjnk'

                Request Body :  {
                                    "user_id": 2,
                                    "request_user_id" : 1,
                                    "type":"Accepted"     // Accepted | Rejected
                                }
                ________________________________________________________________RESPONSE________________________________________________________
                Response :
                          Success Response : 
                                  {
                                      "status": 200,
                                      "msg": "Request Accepted"
                                  }

                            Failed Response :
                                    Response 1 :
                                              {
                                                  "status": 403,
                                                  "msg": "Something went wrong"
                                              }


```

**Recived My Request API**

```python

**Accept & Reject Friend Request**  :   
                End point : /my_requests/
                Content-Type : application/json
                Authorization : 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE5NzY2MTE0LCJpYXQiOjE3MTcxNzQxMTQsImp0aSI6IjE5YWM4NDgzNTk3ZjRiMTZhYWVhMzgxNTIxYTAxNTgyIiwidXNlcl9pZCI6MX0.yqzWu9HsReArIKoKVmccRpvNCIqMDvas8tTY2zhmjnk'

                Request Body :  {
                                    "user_id": 2,
                                    "type":"Pending"    // Pending / Accepted / Rejected
                                }
                ________________________________________________________________RESPONSE________________________________________________________
                Response :
                          Success Response :
                                  Pending Respone 1 : 
                                              {
                                                  "status": 200,
                                                  "msg": "Pending Request ",
                                                  "payload": [
                                                      {
                                                          "id": 2,
                                                          "request_status": "Pending",
                                                          "created_dt": "2024-06-01T01:00:58.498457Z",
                                                          "user_id": 4,
                                                          "name": "Amar",
                                                          "email": "amar54@gmail.com"
                                                      }
                                                  ]
                                              }
                                  Accepted Respone 2 :
                                              {
                                                  "status": 200,
                                                  "msg": "Accepted Request ",
                                                  "payload": [
                                                      {
                                                          "id": 1,
                                                          "request_status": "Accepted",
                                                          "created_dt": "2024-06-01T00:38:21.668548Z",
                                                          "user_id": 1,
                                                          "name": "aditya",
                                                          "email": "adityakotheakr79@gmail.com"
                                                      }
                                                  ]
                                              }

                            Failed Response :
                                    Response 1 :
                                              {
                                                  "status": 403,
                                                  "msg": "Something went wrong"
                                              }


```
