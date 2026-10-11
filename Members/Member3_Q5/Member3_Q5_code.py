# Q5 CornersProblem (goes into searchAgents.py)
# Excerpt of the final integrated code in Group_Project/search/. Not runnable on its own.
# Member 3: Gajanayake H.K.D.W.R (IT24510235) - Q5 Finding All the Corners (Problem Representation)

import search
import pacman
from game import Directions, Actions
from typing import Any, Tuple, List

class CornersProblem(search.SearchProblem):
    """
    This search problem finds paths through all four corners of a layout.

    You must select a suitable state space and successor function.
    """

    def __init__(self, startingGameState: pacman.GameState):
        """
        Stores the walls, pacman's starting position and corners.
        """
        self.walls = startingGameState.getWalls()
        self.startingPosition = startingGameState.getPacmanPosition()
        top, right = self.walls.height - 2, self.walls.width - 2
        self.corners = ((1, 1), (1, top), (right, 1), (right, top))
        for corner in self.corners:
            if not startingGameState.hasFood(*corner):
                print('Warning: no food in corner ' + str(corner))
        self._expanded = 0 # DO NOT CHANGE; Number of search nodes expanded

    def getStartState(self):
        """
        Returns the start state (in your state space, not the full Pacman state space)
        """
        "*** YOUR CODE HERE ***"
        # Q5 (Member 3): State representation is (position, visitedCorners).
        # visitedCorners is a 4-tuple of booleans aligned with self.corners.
        # This keeps the state minimal, immutable, and hashable so graph search
        # expanded-set checks work in O(1) time without storing walls or GameState.
        visited = tuple(self.startingPosition == c for c in self.corners)
        return (self.startingPosition, visited)

    def isGoalState(self, state: Any):
        """
        Returns whether this search state is a goal state of the problem.
        The goal is reached when all four corners have been visited.
        """
        "*** YOUR CODE HERE ***"
        # state is ((x, y), (c1_visited, c2_visited, c3_visited, c4_visited))
        return all(state[1])

    def getSuccessors(self, state: Any):
        """
        Returns successor states, the actions they require, and a cost of 1.

         As noted in search.py:
            For a given state, this should return a list of triples, (successor,
            action, stepCost), where 'successor' is a successor to the current
            state, 'action' is the action required to get there, and 'stepCost'
            is the incremental cost of expanding to that successor
        """
        successors = []
        for action in [Directions.NORTH, Directions.SOUTH, Directions.EAST, Directions.WEST]:
            # Add a successor state to the successor list if the action is legal
            # Here's a code snippet for figuring out whether a new position hits a wall:
            #   x,y = currentPosition
            #   dx, dy = Actions.directionToVector(action)
            #   nextx, nexty = int(x + dx), int(y + dy)
            #   hitsWall = self.walls[nextx][nexty]

            "*** YOUR CODE HERE ***"
            (x, y), visited = state
            dx, dy = Actions.directionToVector(action)
            nextx, nexty = int(x + dx), int(y + dy)
            if not self.walls[nextx][nexty]:
                nextPos = (nextx, nexty)
                # If next position matches any corner, mark it as visited (True)
                newVisited = tuple(v or nextPos == c
                                   for v, c in zip(visited, self.corners))
                successors.append(((nextPos, newVisited), action, 1))

        self._expanded += 1 # DO NOT CHANGE
        return successors

    def getCostOfActions(self, actions):
        """
        Returns the cost of a particular sequence of actions.  If those actions
        include an illegal move, return 999999.  This is implemented for you.
        """
        if actions == None: return 999999
        x, y = self.startingPosition
        for action in actions:
            dx, dy = Actions.directionToVector(action)
            x, y = int(x + dx), int(y + dy)
            if self.walls[x][y]: return 999999
        return len(actions)
