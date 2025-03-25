from tinytroupe import utils
import tinytroupe

def simple_task():
    print("TinyTroupe is working!")

troupe = tinytroupe.Troupe()
troupe.add(simple_task)
troupe.run()
