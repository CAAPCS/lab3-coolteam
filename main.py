import sys

from bank import Bank


def read_input_file(filename):
    with open(filename) as fin:
        lines = list(map(lambda x: x.strip(), fin.readlines()))
    return lines


def process_input_file(commands, bank):
    for command in commands:
        command = command.split(" ")
        if command[0] == 'DEPOSIT':
            account_id = int(command[1])
            delta = float(command[2])
            bank.processDeposit(account_id, delta)
        elif command[0] == 'WITHDRAW':
            account_id = int(command[1])
            delta = float(command[2])
            bank.processWithdraw(account_id, delta)

        elif command[0] == 'NEWCUST':
            first_name = command[1]
            last_name = command[2]
            address = command[3:]
            bank.createCustomer(first_name,last_name, address)
        elif command[0] == 'NEWACCOUNT':
            account_id = int(command[1])
            balance = float(command[2])
            bank.createAccount(account_id)
            bank.processDeposit(account_id, balance)
        elif command[0] == 'DISPACCOUNT':
            accounterid = int(command[1])
            bank.displayAccount(accounterid)
        elif command[0] == 'DISPCUST':
            customerid = int(command[1])
            bank.displayCustomerAccount(customerid)
        else:
            print("Command {command[0]} is not valid.")


def main():
    bank = Bank()

    input_commands = read_input_file(sys.argv[1])
    process_input_file(input_commands, bank)
    bank.displayAllAccounts()


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Need to provide an input file! Exiting...")
        exit()
    main()

