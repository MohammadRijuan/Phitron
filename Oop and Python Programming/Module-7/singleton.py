# singleton = one single instance
# id u want a new instance, u will get the old one (created) instance

class singleton:
    __instance=None
    def __init__(self) -> None:
        if singleton.__instance is None:
            singleton.__instance=self
        
        else:
            raise Exception("this is singleton..this one has already an instance..use that one by calling get_instance method")
        
    @staticmethod
    def get_instance():
        if singleton.__instance is None:
            singleton()

        return singleton.__instance


first=singleton.get_instance()
second=singleton.get_instance()
third=singleton.get_instance()

print(first)
print(second)
print(third)

# last=singleton()



# we can know more about design pattern,factory pattern ,architectural pattern etc...
