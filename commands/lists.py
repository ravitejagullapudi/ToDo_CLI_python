import os
import json

from datetime import datetime

FILE_NAME = 'commands/lists.json'
current_path = 'commands/'

def show_lists(args):
    try:
        with open(FILE_NAME,'r') as lists_json:
            
                data = json.load(lists_json)
                print('Currently available lists are: ')
                for index, todo_list in enumerate(data.keys()):
                    print(index+1, data[todo_list]['title'])
    except FileNotFoundError as e:
        print('No lists are created, Please create a list to show')

    except Exception as e:
        print('Some error occured!'+str(e))

def create_list(args):
    list_name = args[0]
    new_list ={}
    with open(FILE_NAME,'r+') as lists_json:
        try:
            data = json.load(lists_json)
            # if file exists already
            if data.get(list_name):
                print('List already exists! Try a different name')
            else:
                # create a new list dict
                new_list = {
                    'title': list_name,
                    'created_at': datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                }
                data[list_name] = new_list
            
                # Add list name to the todo_lists json file
                # and create a list_name.json file in which we add todo items
                with open(current_path+f'lists/{list_name}.json','w') as new_list:
                    new_list.write('[\n]')
                    print(f'Successfully create new list named {list_name}. You can add todos into it by first selecting this list by using use cammand')
                # Add to the lists.json
                lists_json.seek(0)
                json.dump(data, lists_json, sort_keys=True, indent=True)
            
        except FutureWarning as e:
            print('Some error occured!'+str(e))
    

def use_list(args):
    list_name =args[0]
    try:
        with open(FILE_NAME,'r') as lists_json:
            try:
                data = json.load(lists_json)
                if data.get(list_name):
                    return f'{list_name}.json'
                else:
                    return -1
                
            except Exception as e:
                print('Some error occured!'+str(e))
    except FileNotFoundError as e:
        print('File name specified is not found')

