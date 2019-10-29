import abc

class Templatemethod(abc.ABC):
    
    def template_method(self):
        self.do_first_thing()
        self.do_second_thing()
        self.do_last_thing()
    
    @abc.abstractmethod
    def do_first_thing(self):
        pass
        
    def do_second_thing(self):
        pass
    
    def do_last_thing(self):
        print("last_thing")
        
        
class Implementation(Templatemethod):
    
    def do_first_thing(self):
        print("first_thing")
        
if __name__ == "__main__":
    implementation = Implementation()
    implementation.template_method()
