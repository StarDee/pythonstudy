def consumer():
    r=2
    while True:
        n =yield r
        if not n:
            return
        print('[CONSUMER]Consumer %s...'% n)
        r='200 ok'
def produce(c):
    c.send(None)
    n=0
    while n<5:
        n=n+1
        print('[PRODUCER]Producing %s...'%n)
        r=c.send(n)
        print(r)
    c.close()

c=consumer()
produce(c)
