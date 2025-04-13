import click  # to creat cli
import json  # built in module in python  -- to save and load the task file
import os  # built in module in python   -- operating system -- use to check file exist or not

TODO_FILE = "todo.json"  # this variable hold our file


# function
def load_task():  # load task from todo.json
    if not os.path.exists(TODO_FILE):  # exists in os module
        return []  # tell system about the above condition
    with open(TODO_FILE, "r") as file:
        # r is used for read mode and extract data in read mode
        #  #with is used to manage resources -- data manage
        return json.load(file)  # load data from file


def save_task(tasks):  # user defined task
    with open(TODO_FILE, "w") as file:
        json.dump(
            tasks, file, indent=4
        )  # store data in todo json file # user defined taske # indentation for json file


@click.group()
def cli():  # all work done by cli
    """Simple todo list manager"""
    pass


@click.command()
@click.argument("task")  # argument provided by us
def add(task):
    """Add new task into list"""
    tasks = load_task()  # open file
    tasks.append(
        {"task": task, "done": False}  # this task is from argument
    )  # store a dictionary in a file this task variable
    save_task(tasks)
    click.echo(
        f"Task added successfully: {task}"
    )  # this task is coming from @click.argument ("task")


@click.command(name="list")
def tasklist():
    """List of task"""
    tasks = load_task()  # open file
    if not tasks:
        click.echo("No task found")
        return  # stop execution
    for index, task in enumerate(
        tasks, 1
    ):  # task in property here and tasks is variable , starting from 1
        status = "✅" if task["done"] else "❌"
        click.echo(f"{index}. {task['task']} , [{status}] ")


@click.command()
@click.argument("task_number", type=int)
def completed(task_number):
    """Mark Task completed"""
    tasks = load_task()
    if 0 < task_number <= len(tasks):
        tasks[task_number - 1]["done"] = True
        save_task(tasks)
        click.echo(f"Task {task_number} marked as completed")
    else:
        click.echo(f"Invalid task number : {task_number}")


@click.command()
@click.argument("task_number", type=int)
def deleted(task_number):
    """Delete task"""
    tasks = load_task()
    if 0 < task_number <= len(tasks):
        removed_task = tasks.pop(task_number - 1)
        # del tasks[task_number - 1]
        save_task(tasks)
        click.echo(f"Removed task successfully {removed_task['task']}")
    else:
        click.echo(f"Invalid task number : {task_number}")


cli.add_command(add)
cli.add_command(tasklist)
cli.add_command(completed)
cli.add_command(deleted)

# command to run uv run python filename command

if __name__ == "__main__":
    cli()  # if this file is run directly then this will run
