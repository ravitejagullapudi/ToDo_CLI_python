import commands.lists
import commands.todos
from commands import commands_dict

def parse(command):
    '''
    Takes command as input and returns command_name and arguments
    '''
    cmd_list = command.split()
    cmd_type = cmd_list[0]

    if cmd_type == 'help' or cmd_type == 'quit':
        return cmd_type, []
    elif cmd_type == 'list':
        cmd_name = cmd_list[1]
        # If commands are list commands
        if cmd_name in commands_dict['list_cmds'].keys():
            return cmd_name, cmd_list[2:]
        else:
            return 'invalid_list_cmds', []
    elif cmd_type == 'todo':
        cmd_name = cmd_list[1]
        # If commands are todo commands
        if cmd_name in commands_dict['todo_cmds'].keys():
            return cmd_name, cmd_list[2:]
        else:
            return 'invalid_todo_cmds', []
    else:
        return 'invalid',[]


def main():
    print('Started the TODO application')
    current_list = ''
    while(True):
        command = input('$ ')
        # command type, command_name, command_args
        # split the string seperated by space
        command_name, command_args = parse(command)
        command_type = command.split()[0]+'_cmds'


        if command=='quit':
            break
        elif command=='help':
            with open('help.txt', 'r') as help_file:
                print(help_file.read())
            print('-'*100)
        elif command_name == 'invalid':
            print('Please enter a valid command, Check below')
            with open('help.txt', 'r') as help_file:
                print(help_file.read())
            print('-'*100)
        elif command_name == 'invalid_list_cmds':
            print('Please enter a valid list command, Check below')
            with open('help.txt', 'r') as help_file:
                print(help_file.read())
            print('-'*100)
            
        elif command_name == 'invalid_todo_cmds':
            print('Please enter a valid todo command, Check below')
            with open('help.txt', 'r') as help_file:
                print(help_file.read())
            print('-'*100)
        
        elif command_name == 'use':
            # todo
            file_name = commands_dict[command_type][command_name](command_args)
            if file_name == -1:
                print('This is not a valid list name or make sure entered list name!')
                current_list = ''
            else:
                current_list = file_name
                print('Successfully, Chosen the list,..',current_list)
            print('-'*100)

        elif command_type == 'todo_cmds':
            print(current_list)
            # We need to attach current list to which 
            # the todo item ned to be added
            command_args.insert(0, current_list)
            # print('Arguments passed are', command_args)
            commands_dict[command_type][command_name](command_args)
            print('-'*100)
        else:
            commands_dict[command_type][command_name](command_args)
            print('-'*100)

if __name__ == '__main__':
    main()