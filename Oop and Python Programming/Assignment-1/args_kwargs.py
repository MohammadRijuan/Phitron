****args****

1. *args allows to pass a variable number of positional arg to a function..
2. this parameter treated as like a tuple...all positional arguments can be passed to a function

Example:

def total(*args):
    ans=0
    for i in args:
        ans+=i
    return ans

ans=total(1,2,3,4)
print(ans)


****kwargs****

1. **kwargs also allows to pass a variable number of positional arg to a function..
2.this parameter considered as a dictiobnary..

Example:

def info(**kwargs):
    for key, val in kwargs.items():
        print(f'{key} : {val}')

info(Name="Rijuan",Address="CTG",Mobile=1833992529)