def sayHello():
    return 'Hello World'


import helloWorld
helloWorld.__doc__ #'This is the module docstring.'
helloWorld.sayHello.__doc__ # 'This is the function docstring.'
