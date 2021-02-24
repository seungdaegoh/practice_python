import fsm

import inspect


def test_basic_connection():
    state = fsm.START()
    script = ['connect',  'accept',  'read',
            'write', 'close',  'connect' ]

    for event in script:
        #print(event, '>>>', state)
        print(event, '>>>', str(inspect.getmembers(state, __name__)))
#print(event, '>>>', inspect.getmembers(state, __module__))
#print(event, '>>>', inspect.getmembers(state))
#print(event, '>>>', inspect.isfunction(state))
        #print("source___", inspect.getsource(state))
        
        state = state(event)
