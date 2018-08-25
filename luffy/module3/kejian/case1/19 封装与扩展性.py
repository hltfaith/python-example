class Room:
    def __init__(self,name,owner,weight,length,height):
        self.name=name
        self.owner=owner

        self.__weight=weight
        self.__length=length
        self.__height=height

    def tell_area(self):
        return self.__weight * self.__length * self.__height

r=Room('卫生间','alex',10,10,10)

# print(r.tell_area())

print(r.tell_area())


