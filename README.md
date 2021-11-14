# AirBnB - The Console

This is a command line interpreter that will help us to manage the objects in this project, such as:

- Create a new object (ex: a new User or a new Place)
- Retrieve an object from a file, a database etc…
- Do operations on objects (count, compute stats, etc…)
- Update attributes of an object
- Destroy an object

### How to install?

Installing this console is quite easy, just go to your terminal and write:
```sh
https://github.com/yazgiraldoa/AirBnB_clone.git
```
That's it!

### How to start it?

This console has two ways of working: 

You can start it in the interactive mode as

```sh
$ ./console.py
```

And you also pass commands to it in the non-interactive mode as

```sh
$ echo "help" | ./console.py
```

### How to use it?

This are the commands you can use in the console:

| Command | Y/N | Description |
| ------- | --- | ----------- |
|   quit  | ✅ | Command to exit the program |
|   EOF   | ✅ | Command to exit the program |
|   update  | ✅ | Updates an instance based on the class name and id by adding or updating attribute. (Only one attribute at the time). It saves the change into the JSON file. Usage:  update <class name> <id> <attribute name> "<attribute value>" |
|   all   | ✅ | Command that prints all string representation of all instances based or not on the class name Usage: - To show all instances of all classes: all - To show all instances of a specific class: all <class_name> |
|   destroy  | ✅ | Command that deletes an instance based on the class nameand id. It saves the change into the JSON file. Usage: destroy <class_name> <object_id> |
|   show   | ✅ | Command that prints the string representation of an instance based on the class name and id. Usage:  show <class_name> <object_id> |
|   create   | ✅ | Command that creates a new instance of a class, saves it to a JSON file and prints the id. Usage: create <class_name> |
|   help   | ✅ | It shows the docummented commands available in the console |


### Examples

#### To create an object

```sh
$ ./console.py
(hbnb) create User
b9030dc9-684b-4a46-b07b-80dbfdaa2520
(hbnb) 
```

#### To show an object

```sh
$ ./console.py
(hbnb) show User b9030dc9-684b-4a46-b07b-80dbfdaa2520
[User] (b9030dc9-684b-4a46-b07b-80dbfdaa2520) {'id': 'b9030dc9-684b-4a46-b07b-80dbfdaa2520', 'created_at': datetime.datetime(2021, 11, 14, 17, 0, 55, 901449), 'updated_at': datetime.datetime(2021, 11, 14, 17, 0, 55, 901503)}
(hbnb) 
```

#### To show all objects

```sh
$ ./console.py
(hbnb) all
["[User] (b9030dc9-684b-4a46-b07b-80dbfdaa2520) {'id': 'b9030dc9-684b-4a46-b07b-80dbfdaa2520', 'created_at': datetime.datetime(2021, 11, 14, 17, 0, 55, 901449), 'updated_at': datetime.datetime(2021, 11, 14, 17, 0, 55, 901503)}", "[BaseModel] (4cf77954-028f-4803-8f53-4af034b03f22) {'id': '4cf77954-028f-4803-8f53-4af034b03f22', 'created_at': datetime.datetime(2021, 11, 14, 17, 2, 54, 683749), 'updated_at': datetime.datetime(2021, 11, 14, 17, 2, 54, 683779)}", "[Place] (513cb484-c2dd-401d-a3a3-3383186b1ada) {'id': '513cb484-c2dd-401d-a3a3-3383186b1ada', 'created_at': datetime.datetime(2021, 11, 14, 17, 3, 10, 493671), 'updated_at': datetime.datetime(2021, 11, 14, 17, 3, 10, 493711)}"]
(hbnb) 
```

#### To show all objects in a specific class

```sh
$ ./console.py
(hbnb) all User
["[User] (b9030dc9-684b-4a46-b07b-80dbfdaa2520) {'id': 'b9030dc9-684b-4a46-b07b-80dbfdaa2520', 'created_at': datetime.datetime(2021, 11, 14, 17, 0, 55, 901449), 'updated_at': datetime.datetime(2021, 11, 14, 17, 0, 55, 901503)}"]
(hbnb)  
```

#### To update an object

```sh
$ ./console.py
(hbnb) update User b9030dc9-684b-4a46-b07b-80dbfdaa2520 name "Cuchufli Antonio"
```

#### To destroy an object

```sh
$ ./console.py
(hbnb) destroy User b9030dc9-684b-4a46-b07b-80dbfdaa2520
```

## Authors!
***
**Yazmin Giraldo** - @yazgiraldoa -
<a href = 'https://www.twitter.com/@yazgiraldoa'> <img width = '18px' align= 'center' src="https://raw.githubusercontent.com/rahulbanerjee26/githubAboutMeGenerator/main/icons/twitter.svg"/></a>
<a href = 'https://www.github.com/yazgiraldoa'> <img width = '18px' align= 'center' src="https://raw.githubusercontent.com/rahulbanerjee26/githubAboutMeGenerator/main/icons/github.svg"/></a>


**Ibethe Ramada** - @IbetheRamada -
<a href = 'https://www.twitter.com/@AkimashitaGa'> <img width = '18px' align= 'center' src="https://raw.githubusercontent.com/rahulbanerjee26/githubAboutMeGenerator/main/icons/twitter.svg"/></a>
<a href = 'https://github.com/IbetheRamada'> <img width = '18px' align= 'center' src="https://raw.githubusercontent.com/rahulbanerjee26/githubAboutMeGenerator/main/icons/github.svg"/></a>
***