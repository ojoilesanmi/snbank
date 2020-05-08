# snbank
This program is a basic banking system that stores data using the Python File System. 2 file texts are created initially.


The program accepts a staff to login into the app and perform some functions-create account, check account details and logout.


If the staff logs in successfully with already existing credentials in the the staff text file, the staff will be allowed to perform the functions stated above.


The program automatically generates a 10-digit account number after collecting other necessary details like account name, opening balance, account type and email. These information are stored in an empty text file named customer.txt.

If the staff decides to check account details, the account number will be requested. On validating this, the details inputed above will be displayed from the customer txt file.


A text file containing staff login credentials is created on successful login and deleted when the staff logs out. 


User can also decide to close the app (this stops the program from running).
