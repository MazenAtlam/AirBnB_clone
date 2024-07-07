<center><h1>The Console</center></h1>
This Project is a command-line interpreter designed as the initial stage of a comprehensive project to manage AirBnB Objects.The Interpreter provides essential functionalities such as adding, updating, destroying, and managing the storage of the objects. It utilizes a system of JSON deserialization ensuring data being persistent between sessions, allowing for seamless user experience.

---

<center><h3>Table Of Content</center></h3>

1. [Installation](#installation)
2. [Usage](#usage)
3. [Features](#features)
4. [Authors](https://github.com/MazenAtlam/AirBnB_clone/blob/main/AUTHORS)


## Installation
In order to install and use the command interpreter follow these steps

## Usage
Here are some Basic examples :

## Features
- **create**

Creates New Instance

***Syntax***
```python
create <class_name>
```

***Example***
```shell
(hbnb) create BaseModel
84a2b477-e2e5-479c-8b05-6513cd15fc12
(hbnb)
```
- **update**

Updates an instance based on class name and id

***Syntax***
```python
update <class_name> <id> <new_attr_name> <attr_value>
```

***Example***
```shell
(hbnb) update BaseModel 84a2b477-e2e5-479c-8b05-6513cd15fc12 name "Mazen Atlam"
(hbnb) show BaseModel 84a2b477-e2e5-479c-8b05-6513cd15fc12
[BaseModel] (84a2b477-e2e5-479c-8b05-6513cd15fc12) {'created_at': datetime.datetime(2024, 7, 7, 12, 12, 31, 918139), 'id': '84a2b477-e2e5-479c-8b05-6513cd15fc12', 'updated_at': datetime.datetime(2024, 7, 7, 12, 13, 33, 926706), 'name': 'Mazen_Atlam'}
(hbnb)
```
- **destroy**

Deletes an instance based on class name and id

***Syntax***
```python
destroy <class_name> <id>
```

***Example***
```shell
(hbnb) destroy BaseModel 84a2b477-e2e5-479c-8b05-6513cd15fc12
(hbnb) show BaseModel 84a2b477-e2e5-479c-8b05-6513cd15fc12
** no instance found **
(hbnb)
```
- **show**

Prints the string representation of an instance based on class name and id

***Syntax***
```python
show <class_name> <id>
```

***Example***
```shell
(hbnb) show BaseModel a0ef0a07-ee74-4b6b-831c-141c44de6fb3
[BaseModel] (a0ef0a07-ee74-4b6b-831c-141c44de6fb3) {'created_at': datetime.datetime(2024, 7, 7, 9, 17, 2, 11787), 'id': 'a0ef0a07-ee74-4b6b-831c-141c44de6fb3', 'updated_at': datetime.datetime(2024, 7, 7, 12, 4, 15, 496660), 'name': 'ahmed', 'email': 'AhmedSHehab@gmail.com'}
(hbnb)
```
- **all**

Prints all String Representation of all instances based or not on class name

***Syntax***
```shell
all <class_name>
# OR
all # To Print all instances of all classes
```

***Example***
```python
(hbnb) all
["[BaseModel] (a0ef0a07-ee74-4b6b-831c-141c44de6fb3) {'created_at': datetime.datetime(2024, 7, 7, 9, 17, 2, 11787), 'id': 'a0ef0a07-ee74-4b6b-831c-141c44de6fb3', 'updated_at': datetime.datetime(2024, 7, 7, 12, 4, 15, 496660), 'name': 'ahmed', 'email': 'AhmedSHehab@gmail.com'}", "[State] (4562340f-1870-4de3-84a8-f8669dc54dc6) {'created_at': datetime.datetime(2024, 7, 7, 9, 17, 18, 118064), 'id': '4562340f-1870-4de3-84a8-f8669dc54dc6', 'updated_at': datetime.datetime(2024, 7, 7, 9, 17, 18, 118223)}", "[State] (8568bba3-528f-47c0-8a16-72f85ca34883) {'created_at': datetime.datetime(2024, 7, 7, 9, 41, 59, 210279), 'id': '8568bba3-528f-47c0-8a16-72f85ca34883', 'updated_at': datetime.datetime(2024, 7, 7, 9, 41, 59, 210765)}"]
(hbnb)


# To Select models of specific Class
(hbnb) all BaseModel
["[BaseModel] (a0ef0a07-ee74-4b6b-831c-141c44de6fb3) {'created_at': datetime.datetime(2024, 7, 7, 9, 17, 2, 11787), 'id': 'a0ef0a07-ee74-4b6b-831c-141c44de6fb3', 'updated_at': datetime.datetime(2024, 7, 7, 12, 4, 15, 496660), 'name': 'ahmed', 'email': 'AhmedSHehab@gmail.com'}"]
(hbnb)
```
