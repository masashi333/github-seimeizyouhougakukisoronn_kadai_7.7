# -*- coding:utf-8 -*-

states = ("rainy","sunny")
observations = ("walk","shop","clean","shop","walk")
start_prob = {"rainy":0.6,"sunny":0.4}
transit_prob = {"rainy":{"rainy":0.7,"sunny":0.3},
                "sunny":{"rainy":0.4,"sunny":0.6}}
emission_prob = {'rainy' : {'walk': 0.1, 'shop': 0.4, 'clean': 0.5},
                 'sunny' : {'walk': 0.6, 'shop': 0.3, 'clean': 0.1}}

def viterbi(observs,states,sp,tp,ep):
    """viterbi algorithm
    Output : labels estimated"""
    T = {} # present state
    for st in states:
        T[st] = (sp[st]*ep[st][observs[0]],[st])
    for ob in observs[1:]:
        T = next_state(ob,states,T,tp,ep)
    prob,labels = max([T[st] for st in T])
    return prob,labels


def next_state(ob,states,T,tp,ep):
    """calculate a next state's probability, and get a next path"""
    U = {} # next state
    for next_s in states:
        U[next_s] = (0,[])
        for now_s in states:
            p = T[now_s][0] * tp[now_s][next_s] * ep[next_s][ob]
            if p>U[next_s][0]:
                U[next_s] = [p,T[now_s][1]+[next_s]]
    return U

if __name__=="__main__":
    print observations
    a,b = viterbi(observations,states,
                  start_prob,transit_prob,emission_prob)
    print b
    print a