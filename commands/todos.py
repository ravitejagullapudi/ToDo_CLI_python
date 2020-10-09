import json
from . import lists
from datetime import datetime 
current_path = 'commands/'

def set_list(list_name):
    if list_name == '':
        print('Please select a given list before this action by running the ``list use list_name`` command')
        lists.show_lists([])
    return list_name

def get_data(list_name):
    """
        Get the deserialized data from the todo list json file
    """
    with open(current_path+ f'lists/{list_name}','r+') as json_file:
        data = json.load(json_file)
    return data
    
def update_data(list_file_name, new_data):
    """
        Update the content of the todo list json file
        with the serialized version of 'new_data'
    """
    with open(current_path+f'lists/{list_file_name}','w') as json_file:
        json.dump(new_data,json_file,sort_keys=True, indent=True)
    print('Changes successfully reflected.')


def add_item(args):
    # r+ means read+write
        
    """
        Adds a todo item to the todo list
    """

    list_name = set_list(args[0])
    if not list_name:
        return

    title = args[1]
    data  = get_data(list_name)
    
    new_todo = {
        'title': title,
        'created_at': datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
        'completed': False
    }
    data.append(new_todo)
    update_data(list_name,data)

def show_items(args):
    """
        Prints all the todo items in the currently chosen todo list
    """
    # r+ means read+write
    list_name = set_list(args[0])
    if (not list_name):
        return
    data = get_data(list_name)


    if len(data)==0:
        print('No todos in the list, Add one')
    else:
        complete=0
        for index, todo_item in enumerate(data):
            print(index+1, todo_item['title'])
            if todo_item['completed']:
                complete+=1
        print(f'{complete}/{len(data)} completed')

def edit_item(args):
    """
        Edit a particular todo item
    """
    list_name = set_list(args[0])
    if (not list_name):
        return
    item_id = int(args[1])
    new_title = args[2]
    data = get_data(list_name)
    update_todo = {
        'title': new_title,
        'created_at': datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
        'completed': False
    }
    data[item_id - 1] = update_todo
    update_data(list_name, data)

def remove_item(args):
  """
  Remove a todo item
  """
  list_name = set_list(args[0])
  if (not list_name):
    return
  item_id = int(args[1])
  data = get_data(list_name)
  data.pop(item_id - 1)
  update_data(list_name, data)

def complete_item(args):
  """
  Mark a todo item as completed
  """
  list_name = set_list(args[0])
  if (not list_name):
    return
  item_id = int(args[1])
  data = get_data(list_name)
  data[item_id - 1]['completed'] = True
  update_data(list_name, data)

def incomplete_item(args):
  """
  Mark a todo item as incomplete
  """
  list_name = set_list(args[0])
  if (not list_name):
    return
  item_id = int(args[1])
  data = get_data(list_name)
  data[item_id - 1]['completed'] = False
  update_data(list_name, data)


    