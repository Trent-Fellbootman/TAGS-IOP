# TAGS

 Experimental IOP Framework for Python

 WARNING: Currently, this project has NO EXCEPTION HANDLING. USE AT YOUR OWN RISK!

 <br/>

 ## I. Introduction to Interface Oriented Programming

I believe that each piece of code shall be reused as much as possible, so I came up with this paradigm called "Interface Oriented Programming" IOP), as well as its experimental implementation in Python.

The fundamental idea of "Interface Oriented Programming" (IOP) is that one class should be able to be reused as multiple interfaces without making changes to the class itself as long as configuration for such operation is presented, even if there were no intentions to make that possible in the designing of the class.

Here, a "class" is considered as definition of a functional entity, containing declarations and implementations for its methods and variables; whereas an "interface" is considered just a specification, containing only declarations but no implementations.

An interface instance is an instance of a class mapped to an interface with certain configuration, specifying how certain methods and variables in the class correspond to that in the interface. An interface instance can be easily converted to an instance of another interface, as long as configuration for such conversion is presented.

One of the most powerful features of IOP is that new classes, as well as functions can be defined on interface types, and new interfaces can be defined on existing interfaces as well. This allows the types of function arguments, as well as class or interface variables to vary. For example, if the variables of a class are of interface types, the the class may be instantiated using any class / interface instances as long as those instances offer configurations using which they may be used as instances of the interfaces required for the class instantiation.

<br/>

## II. Usages

### 1. Requirements for class definitions

TAGS does not require you to change the way you code very much, but you should include a "GET_variableName (self): return self.variableName" method and a "SET_variableName (self, obj): self.variableName = obj" method for each variable in your class if you wish that class to be used as an interface (of course, you can write code to generate those functions automatically). Otherwise, you will not be able to get and set variables through interface normally.

<br/>

### 2. Importing TAGS

To import TAGS, simply import "interface.py"

<br/>

### 3. Writing Interface Configurations

Interface configurations are written in JSON format. Basically, a JSON configuration of an interface consists of two parts: a specification that specifies what methods and varables the interface should have ("interfaceSpecification" in json files) and an array of configurations that specifies how the interface may be converted into other interfaces (tagConfigurations in json files).

To learn more about how to write interface configurations, take a look at "Koala_INTERFACE.json", the example file for configurating interfaces.

<br/>

### Writing Class Configurations

To use a class as a specific interface, you do not need to change the definition of the class (after you have written/generated the GET and SET methods). However, you do need to specify how the class can be mapped to the interface by writing a configuration in JSON format.

To learn more about how to write class configurations, take a look at "Koala_Binder.json". It should be noticed that the name of the methods and variables in the json file must correspond to those in the class definition.

<br/>

### Using the "interface" module

The interface module contains only the "Interface" class, which contains several sub-classes. Among all these classes, what you should use are the "Interface" class and the "Interface.Object" class.

To load an interface, as well as its configurations that specifies how it can be converted into other interfaces from your JSON configuration, simply initiate the interface using its "__init__" method, with the file name of your json file as the argument.

To load the configuration for mapping a class to an instance, first create a configuration object using "Interface.Object.Configuration()", then call the "LoadFromFile" method of that object, with the file name of your json file as the argument.

To initiate an interface instance using a class instance and an interface, simply use the "Interfacialize" method of that interface, with your class instance as the first argument and the configuration object containing the configuration for mapping the class to the interface as the second.

Interface instances correspond to instances of the "Interface.Object" class in the module.To convert an interface instance to instance of another interface, use the "As" method of the instance, with the interface to which you wish the instance to be converted as the argument. This method will return an instance of the interface to which you wish the interface to be converted, and will retain the original instance. However, the newly created interface instance and the originial one will have the same class instance attached. This means changing the properties of the class instance of one interface instance will result in changes to that of the other interface instance.

To call a method of an interface instance, use the "Call" method of that instance, with the method name you wish to call as the first argument and a dictionary of the arguments that method takes in as the second.

To Get a variable of an interface instance, use the "Get" method of that instance, with the variable name you wish to get as the argument.

To Set a variable of an interface instance, use the "Set" method of that instance, with the variable name you wish to set as the first argument, and the value you wish to set as the second.

For more information, check out "example.py".

<br/>

## III. Friendly Reminders

### 1. About Reliability

This project, named "TAGS", is an EXPERIMENTAL IOP framework for Python. The word "EXPERIMENTAL" means there is currently NO EXCEPTION HANDLING and that anything might go wrong in anyway if you use it incorrectly, but if you write your code, as well as your json configurations unerringly, it should work as expected.

Of course, as the idea and the implementations of IOP develops, new features such as exception handling will be added.

### 2. Performance

The performance of this framework depends on how you use it. Type conversions of the framework are done using the "eval" function, so if you use the framework to call simple functions in a high frequency, the performance may drop dramatically. However, if you have complicated functions and classes that naturally take a lot of time to be called or instantiated (for example, game development), cost of performance for using TAGS should be insignificant.
