flock = [20, 10, 25, 50, 300, 200 ,150, 100 ,90, 36]
print('Hello, my name is Tung and these are my sheep sizes')
print(flock)

highest = max(flock)
print('Now my biggest sheep has size',highest,'let sheer it')
highest_pos = flock.index(max(flock))
flock[highest_pos] = 8
print('After sheering, here is my flock')
print(flock)
for i in range(1,5):
    flock = [x+50 for x in flock]
    print('MONTH',i)
    print('One month has passed, now here is my flock')
    print(flock)
    highest = max(flock)
    print('Now my biggest sheep has size',highest,'let sheer it')
    highest_pos = flock.index(max(flock))
    flock[highest_pos] = 8
    print('After sheering, here is my flock')
    print(flock)
print('My flock has size in total:',sum(flock))
print('I would get',sum(flock),'* 2$ =',sum(flock)*2,'$')