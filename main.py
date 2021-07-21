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
            pass #TODO
        elif command[0] == 'WITHDRAW':
            pass  # TODO
        elif command[0] == 'NEWCUST':
            pass  # TODO
        elif command[0] == 'NEWACCOUNT':
            pass  # TODO
        elif command[0] == 'DISPACCOUNT':
            pass  # TODO
        elif command[0] == 'DISPCUST':
            pass  # TODO
        else:
            print(f"Command {command[0]} is not valid.")


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
