class engine:
    def __init__(self,name,capacity) -> None:
        self.name=name
        self.capacity=capacity


    def start(self):
        return 'engine has started'
    
class driver:
    def __init__(self) -> None:
        pass

#car 'has a' engine 
class car:
    def __init__(self,engine,driver) -> None:
        self.engine=engine()
        self.driver=driver()

    def start(self):
        self.engine.start()
        