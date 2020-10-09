from . import lists
from . import todos


# Maps the command name to command function
commands_dict={
    'list_cmds': {
        'show': lists.show_lists,
        'use': lists.use_list,
        'create': lists.create_list
    },
    'todo_cmds': {
        'add': todos.add_item,
        'all': todos.show_items,
        'edit': todos.edit_item,
        'remove': todos.remove_item,
        'complete': todos.complete_item,
        'incomplete': todos.incomplete_item
    }
}