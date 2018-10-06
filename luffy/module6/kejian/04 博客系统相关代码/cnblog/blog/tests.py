from django.test import TestCase

# Create your tests here.



print("hello"[0:150])


from bs4 import BeautifulSoup

s="<h1>hello</h1><span>123</span><script>alert(123)</script>"

soup=BeautifulSoup(s,"html.parser")

# print(soup.text)

print(soup.find_all())

for tag in soup.find_all():

    print(tag.name)
    if tag.name=="script":
        tag.decompose()

print(str(soup))




