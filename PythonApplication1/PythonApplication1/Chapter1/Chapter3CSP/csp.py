from typing import Generic,TypeVar,Dict,List,Optional
from abc import ABC,abstractmethod

V = TypeVar('V') #Variable Type

D = TypeVar('D') # domain type

#Base class for all constraints

class Constraint(Generic[V,D],ABC):
    def __init__(self,variables:List[V]) -> None:
        self.variables = variables

    #Must be overridden by subclasses
    @abstractmethod
    def satisfied(sef,assignment:Dict[V,D])->bool:
        ...


class CSP(Generic[V,D]):
    def __init__(self,variables:List[V],domains:Dict[V,List[D]]) -> None:
        self.variables:List[V] = variables
        self.domains:Dict[V,List[D]]  = domains
        self.constraints:Dict[V,List[Constraint[V,D]]] = {}
        for variables in self.variables:
            self.constraints[variables] = []
            if variables not in self.domains:
                raise LookupError("Every variable should have a domain to it")

    def add_constraint(self,constraint:Constraint[V,D])->None:
        for variable in constraint.variables:
            if variable not in self.variables:
                raise LookupError("Variable in constraint not in CSP")
            else:
                self.constraints[variable].append(constraint)

    def consistent(self,variable:V,assignment:Dict[V,D])->bool:
        for constraint in self.constraints[variable]:
            if not constraint.satisfied(assignment):
                return False
        return True
    
    def backtracking_search(self,assignment:Dict[V,D] = {})-> Optional[Dict[V,D]]:
        #assignment is complete if every variable is assigned (our base case)
        if len(assignment) == len(self.variables):
            return assignment
        #get all variables in the CSP but not in the assignment
        unassigned:List[V] = [v for v in self.variables if v not in assignment]
        #get every possible domain value of the first unassigned variable
        first:V = unassigned[0]
        for value in self.domains[first]:
            local_assignment = assignment.copy()
            local_assignment[first] = value
            #if we're still consistent, we recurse(continue)
            if self.consistent(first,local_assignment):
                result:Optional[Dict[V,D]] = self.backtracking_search(local_assignment)
                # if we didnt find the result, we will end up backtracking
                if result is not None:
                    return result
        return None


    
    

