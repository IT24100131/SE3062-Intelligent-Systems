# =======================================================================
# Member 1 (IT24100131) - Question 2: Breadth First Search (BFS)
# Target file in project: Group_Project/search/search.py
# =======================================================================

import sys
import os

# Import util and SearchProblem from search package (removes undefined warnings in IDE)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../Group_Project/search')))
try:
    import util
    from search import SearchProblem
except ImportError:
    pass


def breadthFirstSearch(problem: 'SearchProblem'):
    """
    Search the shallowest nodes in the search tree first.
    """
    "*** YOUR CODE HERE ***"
    # Q2 (Member 1 - IT24100131): Graph-search BFS using util.Queue (FIFO).
    # Nodes are expanded level-by-level, guaranteeing optimal path for unit step costs.
    fringe = util.Queue()
    fringe.push((problem.getStartState(), []))
    expanded = set()

    while not fringe.isEmpty():
        state, path = fringe.pop()

        if problem.isGoalState(state):
            return path

        if state not in expanded:
            expanded.add(state)
            for successor, action, _ in problem.getSuccessors(state):
                if successor not in expanded:
                    fringe.push((successor, path + [action]))

    return []
