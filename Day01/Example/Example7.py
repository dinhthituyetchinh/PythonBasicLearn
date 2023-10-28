#defaultdict
state_capitals = {
 'Arkansas': 'Little Rock',
 'Colorado': 'Denver',
 'California': 'Sacramento',
 'Georgia': 'Atlanta'
}

from collections import defaultdict
state_capitals = defaultdict(lambda: 'Boston')

state_capitals['Arkansas'] = 'Little Rock'
state_capitals['California'] = 'Sacramento'
state_capitals['Colorado'] = 'Denver'
state_capitals['Georgia'] = 'Atlanta'

state_capitals['Arkansas']

print(state_capitals['Arkansas'])


import math
print(math.sqrt(16)) # 4.0
print(math.pow(2, 3))

math.__doc__