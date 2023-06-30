from operator import itemgetter
from typing import Dict
from functools import lru_cache
from typing import TypeVar,Generic,List
T= TypeVar('T')

def fib(n:int):
    if n<2: #Base case
        return n
    else:
        return fib(n-1)+fib(n-2) #recursive case


memo: Dict[int,int] = {0:0,1:1}
def fib3(n:int):
    if n not in memo:
        memo[n] = fib3[n-1]+fib[n-2]
    else:
        memo[n]


@lru_cache
def fib4(n:int):
    if n < 2:
        return n
    else:
        return fib4(n-1)+fib4(n-2)


#tuple unpacking
def fib5(n:int):
    if n==0: return n
    last : int = 0
    next1 : int = 0
    for _ in range (1,n):
        last,next1 = next1,last+next1
    return next1

def calculate_pi(n_terms:int):
    numnerator:float = 4.0
    denominator:float = 1.0
    operation:float = 1.0
    pi:float = 0.0

    for _ in range(n_terms):
        pi += operator * (numerator/denominator)
        denominator += 2.0
        operator *= -1.0
    return pi




class Stack(Generic[T]):
    def __init__(self) -> None:
        self._container:List[T] = []

    def push(self,item:T):
        self._container.append(item)

    def pop(self) -> T:
        return self._container.pop()
    
    def __repr__(self) -> str:
        return repr(self._container)


num_discs:int = 3
tower_a:Stack[int] = Stack()
tower_b:Stack[int] = Stack()
tower_c:Stack[int] = Stack()

for i in range(1,num_discs+1):
    tower_a.push(i)


def hanoi(begin:Stack[int],end:Stack[int],temp:Stack[int],n:int)->None:
    if n==1:
        end.push(begin.pop()) #Base Case
    else:
        hanoi(begin,temp,end,n-1)
        hanoi(begin,end,temp,1)
        hanoi(temp,end,begin,n-1)

if __name__ == "__main__":
    hanoi(tower_a,tower_b,tower_c)

     

    












