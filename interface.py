import json
from typing import NewType


# TODO: Interface conversion


class Interface:
    """
    An Interface object is a representation for an interface. It contains several methods (type: Interface.Specification.Method), which represent the methods of the interface; and several variables (type: Interface.Specification.Variable), which represent the variables of the interface.
    NOTE: An Interface object DOES NOT correspond to a specific class. Any class mappable can be mapped to a specific Interface object.
    NOTE: An Interface object is just a SPECIFICATION, NOT referring to any specific class or object!
    """

    # Definition for class "Interface.Specification"

    class Specification:

        # Definition for class "Interface.Specification.Method"

        class Method:
            """
            A Method object is a representation for a method in a class. Its "name" variable represents its method name in the class.
            """

            variableSignature = None
            name = None

            def __init__(self, name, variableSignature) -> None:
                """
                # variableSignature should be a reference to a Interface.Specification.Method.VariableSignature object
                # name should be a string, indicating the name of the Method in the INTERFACE object it belongs to, NOT that in the specific class to which the INTERFACE object is bound to! 
                """

                self.name = name
                self.variableSignature = variableSignature

            # Definition for class "Interface.Specification.Method.Signature"

            class VariableSignature:
                var = None
                ret = None

                def __init__(self, var, ret) -> None:
                    """
                    # var should be a dictionary of $variableName: $variableType, listing out the names and types of the parameters that the method takes in
                    # ret should be a dictionary of $variableName: $variableType, listing out the names and types of the variables that the method returns
                    """

                    self.var = var
                    self.ret = ret

        # Definition for class "Interface.Specification.Variable"

        class Variable:
            """
            A Variable object is a representation for a variable in a class. Its "name" variable represents its variable name in the class.
            """

            typeSignature = None
            name = None

            def __init__(self, name, typeSignature) -> None:
                """
                # typeSignature should be a string, indicating the type of obj
                # name should be a string, indicating the name of the variable in the Interface object it belongs to
                """

                self.name = name
                self.typeSignature = typeSignature

        # begin variable definitions

        methods = []
        variables = []

        def __init__(self, methods, variables) -> None:
            """
            # methods should be a list of Interface.Specification.Method objects
            # variables should be a list of Interface.Specification.Variable objects
            """

            self.methods = methods
            self.variables = variables

    class TagConfiguration:

        # definition of the Method specification

        # class Method:
        #     """
        #     # name should be a string, indicating the name of the method in the other interface
        #     # selfRef should be a string, indicating which method in the "self" interface is assigned to the method in the other interface
        #     """
        #     name = None
        #     selfRef = None

        #     def __init__(self, name, selfRef) -> None:
        #         self.name = name
        #         self.selfRef = selfRef

        # # definition of the variable specification

        # class Variable:
        #     """
        #     # name should be a string, indicating the name of the variable in the other interface
        #     # selfRef should be a string, indicating which variable in the "self" interface is assigned to the variable in the other interface
        #     """
        #     name = None
        #     selfRef = None

        #     def __init__(self, name, selfRef) -> None:
        #         self.name = name
        #         self.selfRef = selfRef

        # begin variables definition

        """
        # methods should be a dictionary of $nameInTheOtherInterface: $method (type: Interface.TagConfiguration.Method)
        # variables should be a dictionary of $nameInTheOtherInterface: $ $nameInThisInterface
        """
        class Method:
            """
            # name should be a string, indicating the name of the method in the interface to which the "self" is bound
            # var should be a dictionary of $nameInThisInterface: $nameInTheOtherInterface
            # ret should be a dictionary of $nameInThisInterface: $nameInTheOtherInterface
            """

            name = None
            var = {}
            ret = {}

            def __init__(self, name, var, ret) -> None:
                self.name = name
                self.var = var
                self.ret = ret

        methods = {}
        variables = {}

        def __init__(self, methods, variables) -> None:
            self.methods = methods
            self.variables = variables

    class Object:

        # Definition for Interface.Object.Configuration

        class Configuration:
            """
            # methods should be a dictionary of $nameInInterface: $configuration (type: Interface.Object.Configuration.Method)
            # variables should be a dictionary of $nameInInterface: $nameInClass
            """

            class Method:
                """
                var should be a dictionary of $nameInInterface: $nameInClass
                ret should be a dictionary of $nameInInterface: $nameInClass
                """

                name = None
                var = {}
                ret = {}
                retBackwards = {}

                def __init__(self, name, var, ret) -> None:
                    self.name = name
                    self.var = var
                    self.ret = ret

                    retBack = {}
                    for key in self.ret.keys():
                        retBack[ret[key]] = key

                    self.retBackwards = retBack

            interfaceName = None
            className = None
            methods = {}
            variables = {}

            def __init__(self) -> None:
                pass

            def LoadFromFile(self, file):

                # file should be a string, indicating the file holding the configuration

                f = open(file, 'r')
                dictionary = json.load(f)

                self.interfaceName = dictionary['interfaceName']
                self.className = dictionary['className']

                configuration = dictionary["configuration"]

                methods = {}
                for key in configuration['methods'].keys():
                    args = {}
                    for var in configuration['methods'][key]['variables'].keys():
                        args[var] = configuration['methods'][key]['variables'][var]

                    rets = {}
                    for ret in configuration['methods'][key]['returns'].keys():
                        rets[ret] = configuration['methods'][key]['returns'][ret]

                    methods[key] = Interface.Object.Configuration.Method(
                        configuration['methods'][key]['name'], args, rets)

                variables = {}
                for key in configuration['variables'].keys():
                    variables[key] = configuration['variables'][key]

                self.methods = methods
                self.variables = variables
                f.close()

        """
        # obj should be an object (of any class mappable to this interface)
        # interface should be a reference to an Interface object, indicating the interface to which the object is bound
        # configuration should be an Interface.Object.Configuration object
        NOTE: An Interface.Object object IS a specification BOUND TO A SPECIFIC OBJECT!
        """

        # begin variable definitions

        obj = None
        interface = None
        configuration = None

        def __init__(self, obj, interface, configuration) -> None:
            # TODO: CHECK configuration validity!
            self.obj = obj
            self.interface = interface
            self.configuration = configuration

        def Call(self, methodName, variables):
            """
            # methodName should be the name of the method in the INTERFACE.OBJECT object, NOT the class to which it is bound!
            # variables should be a dictionary with strings as keys
            """
            # TODO: CHECK VALIDITY!
            args = ""
            for key in variables.keys():
                args += f"{self.configuration.methods[methodName].var[key]}=variables['{key}'], "

            classRet = eval(
                f"self.obj.{self.configuration.methods[methodName].name}({args})")

            InterfaceRet = {}
            for key in classRet.keys():
                InterfaceRet[self.configuration.methods[methodName]
                             .retBackwards[key]] = classRet[key]

            return InterfaceRet

        def Get(self, variableName):
            # TODO: CHECK VALIDITY!
            return eval(f"self.obj.GET_{self.configuration.variables[variableName]}()")

        def Set(self, variableName, var):
            # TODO: CHECK VALIDITY!
            eval(
                f"self.obj.SET_{self.configuration.variables[variableName]}(var)")

        def As(self, interface):
            """
            # interface should be a reference to an Interface object, indicating the interface to which the "self" is going to be converted
            """

            # """
            # !!!
            # !!!
            # !!!
            # """
            # interface = Interface()
            # self.configuration = Interface.Object.Configuration()
            # self.interface = Interface
            # """
            # !!!
            # !!!
            # !!!
            # """

            newObject_obj = self.obj
            newObject_interface = interface
            newobject_configuration = Interface.Object.Configuration()
            newobject_configuration.className = self.configuration.className
            newobject_configuration.interfaceName = interface.name
            newobject_configuration.methods = {}
            newobject_configuration.variables = {}
            tagConfig = self.interface.TAGS_CONFIGURATIONS[newObject_interface.name]
            for method in tagConfig.methods.keys():
                vars = {}
                for var in tagConfig.methods[method].var.keys():
                    vars[var] = self.configuration.methods[tagConfig.methods[method]
                                                           .name].var[tagConfig.methods[method].var[var]]

                rets = {}
                for ret in tagConfig.methods[method].ret.keys():
                    rets[ret] = self.configuration.methods[tagConfig.methods[method]
                                                           .name].ret[tagConfig.methods[method].ret[ret]]

                newobject_configuration.methods[method] = Interface.Object.Configuration.Method(
                    self.configuration.methods[tagConfig.methods[method].name].name, vars, rets)

            for var in tagConfig.variables.keys():
                newobject_configuration.variables[var] = self.configuration.variables[tagConfig.variables[var]]

            newObject = Interface.Object(
                newObject_obj, newObject_interface, newobject_configuration)

            return newObject

    # begin variables definition

    """
    # specification should be an Interface.Specification object
    # name should be a string, representing the name of the class
    # TAGS_CONFIGURATION should be a dictionary consisting of keys of string type and values of Interface.TagConfiguration type, storing configurations for mapping the Interface object onto other Interface objects
    """

    name = None
    specification = None
    TAGS_CONFIGURATIONS = {}

    def __init__(self, file) -> None:
        """
        file should be a string, indicating the file name that holds the json configuration of the interface
        TODO: CHECK VALIDITY!
        """

        # Load the json configuration

        f = open(file, 'r')
        dictionary = json.load(f)

        # initiate specification

        spec = dictionary['interfaceSpecification']
        self.name = spec['name']

        # initiate methods

        selfMethods = []
        selfVariables = []
        for method in spec['methods']:
            args = {}
            for var in method['variables']:
                args[var['name']] = var['type']

            rets = {}
            for var in method['returns']:
                rets[var['name']] = var['type']
            varSig = Interface.Specification.Method.VariableSignature(
                args, rets)
            selfMethods.append(
                Interface.Specification.Method(method['name'], varSig))

        # initiate variables

        for variable in spec['variables']:
            selfVariables.append(Interface.Specification.Variable(
                variable['name'], variable['type']))

        self.specification = Interface.Specification(
            selfMethods, selfVariables)

        # initiate TAGS configurations

        configurations = dictionary['tagConfigurations']
        for conf in configurations:
            methods = {}
            for key in conf['configuration']['methods'].keys():
                vars = {}
                for var in conf['configuration']['methods'][key]["variables"].keys():
                    vars[var] = conf['configuration']['methods'][key]['variables'][var]

                rets = {}
                for ret in conf['configuration']['methods'][key]["returns"].keys():
                    rets[ret] = conf['configuration']['methods'][key]['returns'][ret]

                methods[key] = Interface.TagConfiguration.Method(
                    conf['configuration']['methods'][key]["name"], vars, rets)

            variables = {}
            for key in conf['configuration']['variables'].keys():
                variables[key] = conf['configuration']['variables'][key]
            self.TAGS_CONFIGURATIONS[conf['className']] = Interface.TagConfiguration(
                methods, variables)
        f.close()

    def Interfacialize(self, obj, configuration):
        """
        Create an Interface from obj

        """
        # TODO: CHECK VALIDITY!
        return self.Object(obj, self, configuration)
