import collections
class Mystring(collections.UserString):
    def reverse(self,string):
        reversed_string = ''.join(reversed(string))
        self.data = self.data.replace(string,reversed_string)

    def insert(self,index,character):
        self.data = self.data[:index] + character + self.data[index:]

#--------reverse---------------------------
str1=Mystring('ali')
str1.reverse('ali')
print(str1)

#---------insert---------------------------
str2=Mystring('hossein')
str2.insert(3,'M')
print(str2)