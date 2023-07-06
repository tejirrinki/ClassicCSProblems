from typing import TypeVar

#from pydantic import BaseModel

V = TypeVar('V')
BoundFloat = TypeVar('BoundFloat', bound = float)
IntStr = TypeVar('IntStr', int, str)


class Model():
    def __init__(self,a: V,b: BoundFloat,c: IntStr ) -> None:
        self._a = a
        self._b = b
        self._c = c

    def __repr__(self) -> str:
        return '{} {} {}'.format(self._a,self._b,self._c)
      # equivalent of ": Any"
      # equivalent of ": float"
     # equivalent of ": Union[int, str]"


print(Model(a=[1], b=4.2, c='x'))
#> a=[1] b=4.2 c='x'

# a may be None
print(Model(a='str', b=1, c=1))
#> a=Non e b=1.0 c=1