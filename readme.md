
### Assignment
In this lab you will complete the code which runs a
a banking system. The input to your program will
be a list of commands such as creating new customers, accounts, and 
handling transactions. 

Things to do:
1. Complete `Customer` and `Account` classes by adding 
appropriate data fields and needed functions
   
2. Complete `Bank` class by filling in the functionality of the classes

3. Test the code by creating your own example_input.txt file.


#### Data

Customers have `CUSTOMER_ID` and accounts have `ACCOUNT_ID` The
`Bank` class keeps track of customers and accounts. 

The following commands will be in a text file for your 
program to read in. 

You can run the `main.py` program with `python main.py example_input.txt`.

```
DEPOSIT ACCOUNT_ID AMOUNT
WITHDRAW ACCOUNT_ID AMOUNT
NEWCUST FIRSTNAME LASTNAME ADDRESS
NEWACCOUNT CUSTOMER_ID STARTING_BALANCE
DISPACCOUNT ACCOUNT_ID
DISPCUST CUSTOMER_ID
 ```

Customers and account ids are increasing, starting at `0`.
In the `example_input.txt` file, the CUSTOMER_ID of Austin's account 
should be 0, and the id of Alice should be 1.

The display format for `DISPACCOUNT` should be 
```shell
ACCOUNT_ID: <> CUSTOMER_ID: <> BALANCE: <>
```

The display format for `DISPCUST` should be 
```shell
CUSTOMER_ID: <> ACCOUNT_IDS: [<>,<>] 
```

The format for the function `displayAllAccounts` in the `Bank` class is to print 
`DISCUST` for all customers followed by `DISPACCOUNT` for all accounts.

#### TIP
For PyCharm, go to the main.py file, right click and click run. You will then see
```shell
Need to provide an input file! Exiting...
```

Then go up to the top right, next to the play button, click the drop-down menu, and
click edit configurations. In the parameters box, type `example_input.txt`