import random as rd
objects_sun_system = [
    {
        'x': 0,
        'y': 0,
        'vx': 0,
        'vy': 0,
        'm': 333333.3333,
        'r': 0.00464,
        'c': 0,
        't': 'star',
        'name': 'Sun'
    },
    {
        'x': 0.3871,
        'y': 0,
        'vx': 0,
        'vy': 10.0988,
        'm': 0.06,
        'r': 0.000016267,
        'c': 1,
        't': 'planet',
        'name': 'Mercury'
    },
    {
        'x': 0.7233,
        'y': 0,
        'vx': 0,
        'vy': 7.3875,
        'm': 0.81,
        'r': 0.000040333,
        'c': 2,
        't': 'planet',
        'name': 'Venus'
    },
    {
        'x': 1,
        'y': 0,
        'vx': 0,
        'vy': 6.2831,
        'm': 1,
        'r': 0.000042467,
        'c': 3,
        't': 'planet',
        'name': 'Earth'
    },
    {
        'x': 1.5237,
        'y': 0,
        'vx': 0,
        'vy': 5.0172,
        'm': 0.11,
        'r': 0.0000226,
        'c': 4,
        't': 'planet',
        'name': 'Mars'
    },
    {
        'x': 5.2028,
        'y': 0,
        'vx': 0,
        'vy': 2.7559,
        'm': 318,
        'r': 0.0004766,
        'c': 5,
        't': 'planet',
        'name': 'Jupiter'
    },
    {
        'x': 9.5388,
        'y': 0,
        'vx': 0,
        'vy': 2.0346,
        'm': 95,
        'r': 0.0004018,
        'c': 6,
        't': 'planet',
        'name': 'Saturn'
    },
    {
        'x': 19.1914,
        'y': 0,
        'vx': 0,
        'vy': 1.4353,
        'm': 14.5,
        'r': 0.0001704,
        'c': 7,
        't': 'planet',
        'name': 'Uranus'
    },
    {
        'x': 30.0611,
        'y': 0,
        'vx': 0,
        'vy': 1.1462,
        'm': 17,
        'r': 0.000165067,
        'c': 8,
        't': 'planet',
        'name': 'Neptune'
    }
]
objects_double_star = [
    {
        'x': -0.5,
        'y': 0,
        'vx': 0,
        'vy': 4.4429,
        'm': 333333.3333,
        'r': 0.00464,
        'c': 0,
        't': 'star',
        'name': 'sun'
    },
    {
        'x': 0.5,
        'y': 0,
        'vx': 0,
        'vy': -4.4428,
        'm': 333333.3333,
        'r': 0.005,
        'c': 1,
        't': 'star',
        'name': 'anti-sun'
    }
]
collision = []
for i in range(20):
    collision.append(
    {
        'x': 1*(2*rd.random()-1),
        'y': 1*(2*rd.random()-1),
        'vx': 0,
        'vy': 0,
        'm': 1,
        'r': 0.00004,
        'c': 0,
        't': 'planet',
        'name': 'planet'+str(i+1)
    })

objects = {
    'sun-system': objects_sun_system,
    'double-star': objects_double_star,
    'collision': collision
}
