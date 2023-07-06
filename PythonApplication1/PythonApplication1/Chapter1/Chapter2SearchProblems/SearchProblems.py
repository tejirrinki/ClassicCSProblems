from enum import IntEnum
from typing import TypeVar,Generic,List,Iterable,Sequence,Callable,Set,Deque,Dict,Any,Optional,Tuple,Protocol
#from typing_extensions import Protocol
from heapq import heappush,heappop
#from __future__ import annotations

T= TypeVar('T')

Nucleotide:IntEnum = IntEnum('Nucleotide',('A','C','G','T'))
#print(list(Nucleotide))
Codon = Tuple[Nucleotide,Nucleotide,Nucleotide]

Gene = List[Codon]

gene_str: str = "ACGTGGCTCTCTAACGTACGTACGTACGGGGTTTATATATACCCTAGGACTCCCTTT"
def string_to_gene(s:str)-> Gene:
    gene:Gene = []
    for i in range(0,len(s),3):
        if (i+2) >= len(s):
            return gene
        codon:Codon = (Nucleotide[s[i]],Nucleotide[s[i+1]],Nucleotide[s[i+2]])
        gene.append(codon)
    return gene

#print(string_to_gene(gene_str))

my_gene: Gene = string_to_gene(gene_str)

def linear_contains(gene:Gene,key_codon:Codon)->bool:
    for codon in gene:
        return True
    return False

acg: Codon = (Nucleotide.A, Nucleotide.C, Nucleotide.G)
gat: Codon = (Nucleotide.G, Nucleotide.A, Nucleotide.T)
print(linear_contains(my_gene, acg)) # True
print(linear_contains(my_gene, gat)) # False

def binary_contains(gene:Gene,key_codon:Codon)-> bool:
    low:int = 0
    high:int = len(gene)-1
    while low <= high:
        mid:int = (low+high)//2
        if gene[mid] < key_codon:
            low = mid +1
        elif gene[mid] > key_codon:
            high = mid-1
        else:
            return True
    return False

my_sorted_gene:Gene = sorted(my_gene)
print(binary_contains(my_sorted_gene, acg)) # True
print(binary_contains(my_sorted_gene, gat)) # False


def linear_contains2(iterable:Iterable[T],key:T)-> bool:
    for item in iterable:
        if item == key:
            return True
    return False


C = TypeVar('C',bound = "Comparable")

class Comparable(Protocol):
    def __eq__(self, other: Any) -> bool:
        return self == other
    def __lt__(self:C,other:C)->bool:
        return self < other
    def __gt__(self:C,other:C)-> bool:
        return (not self < other) and self != other
    def __le__(self:C,other:C)->bool:
        return self<other or self == other
    def __ge__(self:C,other:C)->bool:
        return not self < other

def binary_contains2(sequence: Sequence[C], key: C) -> bool:
    low: int = 0
    high: int = len(sequence) - 1
    while low <= high: # while there is still a search space
        mid: int = (low + high) // 2
        if sequence[mid] < key:
            low = mid + 1
        elif sequence[mid] > key:
            high = mid - 1
        else:
            return True
    return False

print(linear_contains2([1, 5, 15, 15, 15, 15, 20], 5)) # True
print(binary_contains2(["a", "d", "e", "f", "z"], "f")) # True
print(binary_contains2(["john", "mark", "ronald", "sarah"], "sheila")) #False





