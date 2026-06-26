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
    def __init__(self, mdp, discount=0.9, iterations=100):
        """
          Your value iteration agent should take an mdp on
          construction, run the indicated number of iterations
          and then act according to the resulting policy.
        """
        self.mdp = mdp
        self.discount = discount
        self.iterations = iterations
        self.values = util.Counter()  # A Counter is a dict with default 0

        # Laço para o número de iterações definido
        for _ in range(self.iterations):
            # Dicionário temporário para garantir a atualização em batch
            new_values = util.Counter()
            
            for state in self.mdp.getStates():
                if self.mdp.isTerminal(state):
                    new_values[state] = 0
                    continue
                
                max_q = float('-inf')
                possible_actions = self.mdp.getPossibleActions(state)
                
                # Se não houver ações possíveis, o valor continua 0
                if not possible_actions:
                    new_values[state] = 0
                    continue
                    
                # Acha o maior Q-value entre as ações possíveis
                for action in possible_actions:
                    q_val = self.computeQValueFromValues(state, action)
                    if q_val > max_q:
                        max_q = q_val
                        
                new_values[state] = max_q
            
            # Ao final da varredura de todos os estados, atualizamos self.values
            self.values = new_values

    def getValue(self, state):
        return self.values[state]

    def computeQValueFromValues(self, state, action):
        """
          Compute the Q-value of action in state from the
          value function stored in self.values.
        """
        q_value = 0
        # getTransitionStatesAndProbs retorna uma lista de tuplas (nextState, prob)
        for nextState, prob in self.mdp.getTransitionStatesAndProbs(state, action):
            reward = self.mdp.getReward(state, action, nextState)
            # Fórmula de Bellman: Q(s,a) = Soma( Prob * (Recompensa + Desconto * V(s')) )
            q_value += prob * (reward + self.discount * self.getValue(nextState))
        
        return q_value

    def computeActionFromValues(self, state):
        """
          The policy is the best action in the given state
          according to the values currently stored in self.values.
        """
        if self.mdp.isTerminal(state):
            return None
            
        possible_actions = self.mdp.getPossibleActions(state)
        if not possible_actions:
            return None
            
        best_action = None
        max_q = float('-inf')
        
        for action in possible_actions:
            q_val = self.computeQValueFromValues(state, action)
            if q_val > max_q:
                max_q = q_val
                best_action = action
                
        return best_action

    def getPolicy(self, state):
        return self.computeActionFromValues(state)

    def getAction(self, state):
        "Returns the policy at the state (no exploration)."
        return self.computeActionFromValues(state)

    def getQValue(self, state, action):
        return self.computeQValueFromValues(state, action)