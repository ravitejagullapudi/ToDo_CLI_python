# To do CLI application

1. Use cases, running our application -> commands(figure out requirements and usage of our apps)

- Structuring our code, how we will implement it
    - where to store the data
    - how to manipulate the data
- Implemetation along with testing
- Run and use it :)


# Use cases

- Create a todo list
- Show all the todo lists
- Add, edit, delete, mark as complete, incomplete etc.. the todo items present in those lists
- Show all the todo items in a particular items

# Commands to use CLI app

- prefixes for the commands: list, todo
- list show -> show all the todo lists we have
- list create list_name -> create a list with list_name
- list use list_name -> select a particular todo list

- todo add todo_title -> add todo item in the lists
- todo all -> show all todos in selected list
- todo edit item_id new_title -> edit the item with id item_id
- todo remove item_id
- todo complete item_id -> mark item_id as complete
- todo incomplete item_id -> mark item_id as incomplete

- help -> print all the commands we can use in our app
- quit -> exit the application


### data is stored as json file

### lists.json store json 

[
    list1,
    list2
]

check whether a given list exists
-> using the above approach need to iterate over all list elements

- store it as dict of todo list
data = {
        'title':{
            'description':'description',
            'created_at':'time',
            'filename':'name'
        }
    }

### for every todo list we will create a file with some name.

### As we are using json we need to do serialisation and deserialisation of the data

## todo_list->no.of->to_items -> complete, incomplete,add edit delete
