# TAGS

 Experimental IOP implementation for Python

 WARNING: Currently, this project has NO EXCEPTION HANDLING. USE AT YOUR OWN RISK!

 ## Introduction to Interface Oriented Programming

I believe that each piece of code shall be reused as much as possible, so I came up with this paradigm called "Interface Oriented Programming", as well as its experimental implementation in Python.

The fundamental idea of "Interface Oriented Programming" is that one class should be able to be reused as multiple interfaces without making changes to the class itself as long as configuration for such operation is presented, even if there were no intentions to make that possible in the designing of the class. Here, a "class" is considered definition of a functional entity, containing declarations and implementations for its methods and variables; whereas an "interface" is considered just a specification, containing only declarations but no implementations. An interface instance is . An interface instance can be easily converted to another instance of another, as long as configuration for such conversion is presented (as json files, as in this project specifically).
