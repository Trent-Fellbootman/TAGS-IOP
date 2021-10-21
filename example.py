from os import name
import interface

class Koala:
    signature = None

    def BeAdorable(self, target):
        greetings = target + ", I'm so adorable!"
        print(greetings)
        return {"greetings": greetings}
    
    def GET_signature(self):
        return self.signature
    
    def SET_signature(self, signature):
        self.signature = signature

    def __init__(self, signature):
        self.signature = signature

Koala_ITF = interface.Interface("Koala_INTERFACE.json")
Animal_ITF = interface.Interface("Animal_INTERFACE.json")
config_Koala_Koala = interface.Interface.Object.Configuration()
config_Koala_Koala.LoadFromFile("Koala_Binder.json")
Koala_obj = Koala_ITF.Interfacialize(Koala("Koala01"), config_Koala_Koala)
Animal_obj = Koala_obj.As(Animal_ITF)
print("Return: " + Animal_obj.Call("SignatureMove", {"string": "XXX"})["string"])
print(Koala_obj.Get("name"))
Animal_obj.Set("animalSignature", "TheCutestKoalaInTheWholeWideWorld")
print(Koala_obj.Get("name"))