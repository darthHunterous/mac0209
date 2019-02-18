t = 0.0
tf = 2.0
dt = 0.1

y = 10.0
v = 0.0
g = 9.8

while (t < tf):
    y = y + v*dt
    v = v - g*dt
    t += dt
    print('y == {}'.format(y))
    print('v == {}'.format(v))
    print('t == {}'.format(t))
