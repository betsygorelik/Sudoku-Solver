from itertools import permutations
# Arc Consistency algorithm 
class AC3:
    def CreateArcs(self, constraints):
        arcs = []
        for constraint in constraints:
            permOfTwo = list(permutations(constraint, 2))
            arcs+=permOfTwo
        
        return arcs
        

    def Revise(self, csp, Xi, Xj):
        revised = False
        domainI = csp.domain[Xi][:]
        domainJ = csp.domain[Xj]
        
        for x in domainI:
            if not any(x != y for y in domainJ):
                csp.domain[Xi].remove(x)
                revised = True
        
        return revised

    def find_neighbors(self, neighbors, Xi, constraints):
        for constraint in constraints:
            if Xi in constraint:
                for var in constraint:
                    if var != Xi and var not in neighbors[Xi]:
                        neighbors[Xi].append(var)
        return neighbors
    
    # Returns true if arc consistent domains for each variable can be made
    def AC3(self, csp):
        arcs_queue = self.CreateArcs(csp.constraints)
        
        while arcs_queue:
            Xi, Xj = arcs_queue.pop(0)  
            if self.Revise(csp, Xi, Xj):
                if not csp.domain[Xi]:  
                    return False
        
                csp.neighbors = self.find_neighbors(csp.neighbors, Xi, csp.constraints)
                for Xk in csp.neighbors[Xi]:
                    if Xk != Xj:
                        arcs_queue.append((Xk, Xi))
        
        return True  
    
    def print_solved_domain(csp):
        #### Returns the printed solution if the domain of each variable has only one element
        #### Otherwise prints the AC3 domain.
        if max([len(val) for val in csp.domain.values()])==1:
            solution_string="".join([str(item) for sublist in list(csp.domain.values()) for item in sublist])
            print("Sudoku is Solved")
            print()
        else:
            print("Sudoku is Not Solved")
            print()
            print("Domain: ")
            return csp.domain          