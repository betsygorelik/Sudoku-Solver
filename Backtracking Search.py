#  BackTrack is the recursive algorithm that returns whether an assignmemnt is complete and the assignment. 

class BacktrackingSearch:
    
    # Selects the unassigned variable, using the minimum remaining value heuristic. 
    # MRV choose the variable with the fewest legal values in its domain. 
    def SelectUnassignVariable(assignments, csp):
        unassigned_variables = [var for var in csp.domain if var not in assignments]
        if not unassigned_variables:
            return None
        mrv_var = min(unassigned_variables, key=lambda var: len(csp.domain[var]))
        
        return mrv_var

    # Checks if given an assignment and a CSP object, we have successfully completed. the assignment of every empty value of the board
    def CheckAssignment(assignments, csp):
        for var in csp.domain:
            if var not in assignments:
                return False
        return True
            
    # Determines if an assignments is not violating any constriants
    def CheckConsistent(assignment, csp):
        for constraint in csp.constraints:
            assigned_values = set()
            for var in constraint:
                if var in assignment:
                    value = assignment[var]
                    if value in assigned_values:
                        return False
                    assigned_values.add(value)
        return True
