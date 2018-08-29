


def  run():
    count = 0
    while True:
        n =   yield count
        print("-->",n,count)
        count +=1

g = run()

g.__next__()
g.send('alex')
g.send('jack')
g.send('raom')
g.send('alex')
