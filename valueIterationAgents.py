# valueIterationAgents.py
# -----------------------
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


import mdp, util

from learningAgents import ValueEstimationAgent

class ValueIterationAgent(ValueEstimationAgent):
    """
        * Please read learningAgents.py before reading this.*

        A ValueIterationAgent takes a Markov decision process
        (see mdp.py) on initialization and runs value iteration
        for a given number of iterations using the supplied
        discount factor.
    """
    def __init__(self, mdp, discount = 0.9, iterations = 100):
        """
          Your value iteration agent should take an mdp on
          construction, run the indicated number of iterations
          and then act according to the resulting policy.

          Some useful mdp methods you will use:
              mdp.getStates()
              mdp.getPossibleActions(state)
              mdp.getTransitionStatesAndProbs(state, action)
              mdp.getReward(state, action, nextState)
              mdp.isTerminal(state)
        """
        self.mdp = mdp
        self.discount = discount
        self.iterations = iterations
        self.values = util.Counter() # A Counter is a dict with default 0
        self.new_values = util.Counter() # A Counter is a dict with default 0
	self.my_states = mdp.getStates()
	#for s in mdp.getStates():
	#  print(s)
	for i in range(0, iterations):
	    self.do_one_iteration(mdp)
	    self.values = self.new_values
        print("Finished my iterations ")

    def do_one_iteration(self, mdp):
        # Write value iteration code here
        "*** YOUR CODE HERE ***"
	print("States",mdp.getStates())
	for s in mdp.getStates():
	  if (s != 'TERMINAL_STATE'):
	    self.new_values[s] = self.computeActionFromValues(s)
	print(self.values)


    def getValue(self, state):
        """
          Return the value of the state (computed in __init__).
        """
        return self.values[state]


    def computeQValueFromValues(self, state, action):
        """
          Compute the Q-value of action in state from the
          value function stored in self.values.
        """
        "*** YOUR CODE HERE ***"
        s = state
        a = action 
        print("Transitions probabilities ", self.mdp.getTransitionStatesAndProbs(s, a))
        val = 0
        print("This is the value now ", val, "Transition prob", self.mdp.getTransitionStatesAndProbs(s, a)[0][1], "Transition state", self.mdp.getTransitionStatesAndProbs(s, a)[0][0], "Reward", self.mdp.getReward(s, a, self.mdp.getTransitionStatesAndProbs(s, a)[0][0]))
        for tp in self.mdp.getTransitionStatesAndProbs(s, a):
	  if (tp[0] != 'TERMINAL_STATE'):
            val_i = tp[1]*(self.mdp.getReward(s, a, tp[0]) + 0.9*self.values[tp[0]])
            print("This is the value now ", val, "Transition prob", tp[1], "Transition state", tp[0], "Reward", self.mdp.getReward(s, a, tp[0]))
	    print("Transitiong ", tp, " got value ", val_i)
	  else:
	    val_i = self.mdp.getReward(s, a, tp[0])
	    print("Terminal ", tp, " got value ", val_i)
          val = val + val_i
        print("Updating values ofr val", val)
        return val
        #self.values[s] = val
	
        #util.raiseNotDefined()

    def computeActionFromValues(self, state):
        """
          The policy is the best action in the given state
          according to the values currently stored in self.values.

          You may break ties any way you see fit.  Note that if
          there are no legal actions, which is the case at the
          terminal state, you should return None.
        """
        "*** YOUR CODE HERE ***"
	s = state
        print("States possible actions", self.mdp.getPossibleActions(s))
        val = -100
        for a in self.mdp.getPossibleActions(s):
          val_i = self.computeQValueFromValues(s, a)
          if (val_i > val):
            val = val_i
	print("Updating values")
        return val
        #util.raiseNotDefined()

    def getPolicy(self, state):
        return self.computeActionFromValues(state)

    def getAction(self, state):
        "Returns the policy at the state (no exploration)."
        return self.computeActionFromValues(state)

    def getQValue(self, state, action):
        return self.computeQValueFromValues(state, action)
