# AirBnB Clone - The Console

## Description
This is the first step of the AirBnB clone project. It implements a command-line interpreter to manage AirBnB objects (Users, Places, States, Cities, Amenities, Reviews) with JSON file-based persistence.

## Command Interpreter

### How to start
```bash
./console.py
```

### How to use
The console supports the following commands:

| Command | Description |
|---------|-------------|
| `create <class>` | Creates a new instance, saves it, and prints the id |
| `show <class> <id>` | Prints the string representation of an instance |
| `destroy <class> <id>` | Deletes an instance |
| `all [class]` | Prints all instances, optionally filtered by class |
| `update <class> <id> <attr> <value>` | Updates an attribute of an instance |
| `quit` / `EOF` | Exit the program |
| `help` | Display help information |

### Examples

**Interactive mode:**
```
$ ./console.py
(hbnb) create BaseModel
49faff9a-6318-451f-87b6-910505c55907
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'id': '49faff9a-...'}
(hbnb) all BaseModel
["[BaseModel] (49faff9a-...) {...}"]
(hbnb) update BaseModel 49faff9a-6318-451f-87b6-910505c55907 name "My model"
(hbnb) destroy BaseModel 49faff9a-6318-451f-87b6-910505c55907
(hbnb) quit
$
```

**Non-interactive mode:**
```
$ echo "help" | ./console.py
(hbnb)
Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update
(hbnb)
$
```
