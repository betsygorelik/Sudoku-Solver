from copy import copy
class BacktrackingSearch:
    
    # Selects the unassigned variable, using the minimum remaining value heuristic. 
    # MRV choose the variable with the fewest legal values in its domain. 
    def SelectUnassignVariable(self, assignments, csp):
        unassigned_variables = [var for var in csp.domain if var not in assignments]
        if not unassigned_variables:
            return None
        mrv_var = min(unassigned_variables, key=lambda var: len(csp.domain[var]))
        
        return mrv_var

    # Checks if given an assignment and a CSP object, we have successfully completed. the assignment of every empty value of the board
    def CheckAssignment(self, assignments, csp):
        for var in csp.domain:
            if var not in assignments:
                return False
        return True
            
    # Determines if an assignments is not violating any constriants
    def CheckConsistent(self, assignment, csp):
        for constraint in csp.constraints:
            assigned_values = set()
            for var in constraint:
                if var in assignment:
                    value = assignment[var]
                    if value in assigned_values:
                        return False
                    assigned_values.add(value)
        return True
    
    # helper function to convert assignment and csp board to final solved board.
    def board_to_string(assignment, csp):
        rows = "ABCDEFGHI"
        cols = "123456789"
        output = ""
        
        for r in rows:
            for c in cols:
                if r + c not in assignment:
                    output += str(csp.board[r + c])
                else:
                    output += str(assignment[r + c])
            
        return output
    
    # main caller function that returns the assignment of the board
    def BTS(self, csp):
        assignment = self.BackTrack({}, csp)
        return self.board_to_string(assignment, csp)

    #  BackTrack is the recursive algorithm that returns whether an assignmemnt is complete and the assignment.
    def BackTrack(self, assignments, csp):
        if self.CheckAssignment(assignments, csp):
            return assignments
        
        var = self.SelectUnassignVariable(assignments, csp)
        for value in csp.domain[var]:
            new_assignment = assignments.copy()
            new_assignment[var] = value
            if self.CheckConsistent(new_assignment, csp):
                result = self.BackTrack(new_assignment, csp)
                if result != 'failure':
                    return result
            new_assignment.pop(var, None)
        
        return 'failure'
