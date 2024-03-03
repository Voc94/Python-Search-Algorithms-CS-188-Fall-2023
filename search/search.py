# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""
import util
from util import Stack as stack
from util import Queue as queue
from util import PriorityQueue as priorityqueue

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem: SearchProblem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    # print("Start:", problem.getStartState())
    # print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    # print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    start = problem.getStartState()
    visited = set()
    path = []

    def dfs(pos, visited, path):
        if problem.isGoalState(pos):
            return path

        visited.add(pos)
        successors = problem.getSuccessors(pos)

        for successor_pos, successor_dir, _ in successors:
            if successor_pos not in visited:
                new_path = path + [successor_dir]
                result = dfs(successor_pos, visited, new_path)
                if result:
                    return result

        return None
    return dfs(start,visited,path)


def breadthFirstSearch(problem: SearchProblem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    start = problem.getStartState()
    visited = set()
    path = []
    queue = util.Queue()

    queue.push((start, path))

    while not queue.isEmpty():
        pos, path = queue.pop()

        if problem.isGoalState(pos):
            return path

        visited.add(pos)
        successors = problem.getSuccessors(pos)

        for successor_pos, successor_dir, _ in successors:
            if successor_pos not in visited:
                visited.add(successor_pos)
                queue.push((successor_pos, path + [successor_dir]))

    return []

def uniformCostSearch(problem: SearchProblem):
    """Search the node of least total cost first."""
    start = problem.getStartState()
    visited = set()
    priority_queue = util.PriorityQueue()
    priority_queue.push((start, [], 0), 0)  # (position, path, cost), priority

    while not priority_queue.isEmpty():
        pos, path, cost = priority_queue.pop()

        if problem.isGoalState(pos):
            return path

        if pos not in visited:
            visited.add(pos)
            successors = problem.getSuccessors(pos)

            for successor_pos, successor_dir, successor_cost in successors:
                new_path = path + [successor_dir]
                new_cost = cost + successor_cost
                priority_queue.push((successor_pos, new_path, new_cost), new_cost)

    return []




def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    start = problem.getStartState()
    visited = set()
    priority_queue = util.PriorityQueue()
    priority_queue.push((start, [], 0), 0)  # ((pos, action, cost), priority)

    while not priority_queue.isEmpty():
        pos, path, cost = priority_queue.pop()

        if problem.isGoalState(pos):
            return path

        if pos not in visited:
            visited.add(pos)
            successors = problem.getSuccessors(pos)

            for successor_pos, successor_dir, successor_cost in successors:
                new_path = path + [successor_dir]
                new_cost = cost + successor_cost
                priority_queue.push((successor_pos, new_path, new_cost), new_cost + heuristic(successor_pos, problem))

    return []



# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
