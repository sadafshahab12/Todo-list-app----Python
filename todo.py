import click  # to creat cli
import json  # built in module in python  -- to save and load the task file
import os  # built in module in python   -- operating system -- use to check file exist or not

TODO_FILE = "todo.json"  # this variable hold our file
 

# function
def load_task():  # load task from todo.json
    if os.path.exists(TODO_FILE):  # exists in os module
        return []  # tell system about the above condition
    with open(TODO_FILE, "r") as file:
        # r is used for read mode and extract data in read mode
        #  #with is used to manage resources -- data manage
        return json.load(file) # load data from file


def save_task(tasks):  # user defined task
    with open(TODO_FILE, "w") as file:
        json.dump(
            tasks, file, indent=4
        )  # store data in todo json file # user defined taske # indentation for json file

@click.group()
def cli():
    """Simple todo list manager"""
    pass

@click.command()
@click.argument("task") # argument provided by us
def add (task):
    """Add new task into list"""
    tasks = load_task()  # open file
    tasks.append({ "task" : task ,  "done" : False}) # store a dictionary in a file this task variable
    save_task(tasks)
    click.echo(f"Task added successfully: {task}") # this task is coming from @click.argument ("task")