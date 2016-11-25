#This module provides the infrastructure for defining abstract base classes
from abc import ABC, abstractmethod

class Abstract(ABC):
    @abstractmethod
    def foo(self):
        print("foo not implemented yet!")
        pass

class Derived(Abstract):
    def foo(self):
        #TODO: foo not implemented yet
        super().foo()


a  = Derived()
a.foo()

################
def upgrade_players():
    #TODO: update all players in the list l
    pass

def update_enemies():
    # TODO: update all enemies in the list l
    pass
################
#Option1 creating an empty function
class Foo:
    # TODO:
    pass

f = Foo()
print(f)

#Option2
class Bar:
    def get_enemies(self):
        #TODO:
        return False

    def get_players(self):
        #TODO
        return 10

b = Bar()
print(b.get_players())