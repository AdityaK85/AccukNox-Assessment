**AccukNox Assessment Test Completed : **
> [!NOTE]
>
> ```
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


```

**API's Endpoints **

**BASE URL : http://127.0.0.1:8000**

**User Login**  :   
                End point : /user_login
                Content-Type : Json
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
