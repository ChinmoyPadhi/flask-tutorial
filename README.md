**Problem Statement**
1. Create a Flask application with an /api route. When this route is accessed, it should return a JSON list.
   The data should be stored in a backend file, read from it, and sent as a response.
2. Create a form on the frontend that, when submitted, inserts data into MongoDB Atlas.
   Upon successful submission, the user should be redirected to another page displaying the message "Data submitted successfully".
   If there's an error during submission, display the error on the same page without redirection.
   
**Command to execute the app.py file from Exercise01**

$ python app.py

**The output for Problem 1**

<img width="239" height="281" alt="image" src="https://github.com/user-attachments/assets/a3ed5338-f3d8-438a-92fb-c72a23d8e9ea" />

**Command to execute the app.py file from Exercise02**

$python app.py

Please enter Username and Password

<img width="288" height="181" alt="image" src="https://github.com/user-attachments/assets/1ee929c5-371f-4a4e-8099-cae0ff030fa6" />

Upon submit it will move to a new html page which says Data submitted Successfully
<img width="301" height="140" alt="image" src="https://github.com/user-attachments/assets/9c546ac3-f5c6-490c-b58e-4b4249734fd7" />

Go to your Atlas DB and check in the Data Explorer-->cluster0-->testdb-->credentials collection
<img width="895" height="311" alt="image" src="https://github.com/user-attachments/assets/889f3ae9-3463-452e-8239-c5f550f3bdb9" />

