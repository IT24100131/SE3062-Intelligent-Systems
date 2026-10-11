# =======================================================================
# Member 1 (IT24100131) - Question 1: Depth First Search (DFS)
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


def depthFirstSearch(problem: 'SearchProblem'):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.
    """
    "*** YOUR CODE HERE ***"
    # Q1 (Member 1 - IT24100131): Graph-search DFS using util.Stack (LIFO).
    # Nodes are expanded deepest-first to find a path to the food goal.
    fringe = util.Stack()
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
