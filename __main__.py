
import volume

def a():
    print("inside ")
    print(__name__)
    
def b():
    print("insdide ")
    print(__name__)
    

if __name__ == "__main__":
    print("inside ")
    print(__name__)
    a()
    b()
    volume.audio(5)
    volume.amplify(10)
    
       
# __name__ is a special variable that is set to the name of the module that is being run.
# Also __name__ acts as a gaurd to prevent running uninteded script from imported module. 