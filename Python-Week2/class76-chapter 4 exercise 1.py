class Phone():
    def __int__(self,brand,model_name,price):
        self.brand=brand
        self.model_name=model_name
        self.price=max(price,0)

    def full_name(self):
        return f"{self.brand}{self.model_name}"

    def make_a_call(self,number):
        return f"calling{number}"

class Smartphone(Phone):
    def _int_(self,brand,model_name,price,ram,internal_memory,rear_camera):
        Phone.__int__(self,brand,model_name,price)
        super().__int__(self,brand,model_name)
        self.ram=ram
        self.internal_memory=internal_memory
        self.rear_camera=rear_camera

    def full_name(self):
        return f"{self.brand}{self.model_name}"

    def make_a_call(self,number):
        return f"calling{number}"

Phone ="nokia","1100",1000
smartphone="Oneplus","5",30000,"6GB","64GB","20MP"

print(smartphone)
print(Phone)