
class Mymeta(type):
    def __init__(self,class_name,class_bases,class_dic):
        if not class_name.istitle():
            raise TypeError('类名的首字母必须大写')

        if '__doc__' not in class_dic or not class_dic['__doc__'].strip():
            raise TypeError('必须有注释，且注释不能为空')

        super(Mymeta,self).__init__(class_name,class_bases,class_dic)

class Chinese(object,metaclass=Mymeta):
    '''
    中文人的类
    '''
    country='China'

    def __init__(self,namem,age):
        self.name=namem
        self.age=age

    def talk(self):
        print('%s is talking' %self.name)


# Chinese=Mymeta(class_name,class_bases,class_dic)



