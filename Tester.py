from CSP import CSP
from AC3 import AC3
from BacktrackingSearch import BacktrackingSearch

def main():
        #Tests our CSP algorthimns against a string representing board values.
        #In the string, 0's represent empty spaces on the board
        input = "000000000302540000050301070000000004409006005023054790000000050700810000080060009"
        csp = CSP(input)
        csp.print_board()
        print()
        print(f"The sudoku board:\n{csp.board}\nThe domain:\n{csp.domain}\nThe constraints:\n{csp.constraints}\n")
        ac3 = AC3
        ac3.AC3(ac3, csp)
        print(ac3.print_solved_domain(csp))
        bts = BacktrackingSearch
        print(f"\nSudoku Solution after Backtracking Search: \n{bts.BTS(bts, csp)}")
       
    
    
if __name__ == "__main__":
    main()