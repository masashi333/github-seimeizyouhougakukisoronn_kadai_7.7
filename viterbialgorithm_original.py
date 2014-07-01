# -*- coding:utf-8 -*-

states = ("kousei","husei")
observations = ("6","4","2","6","3","6","1","3","6","5","6","6","4","4")
start_prob = {"kousei":0.7,"husei":0.3}
transit_prob = {"kousei":{"kousei":0.95,"husei":0.05},
                "husei":{"kousei":0.4,"husei":0.6}}
emission_prob = {'1' : {'kousei': 1/6,'husei':1/10},
                 '2' : {'kousei': 1/6,'husei':1/10
                 '3' : {'kousei': 1/6,'husei':1/10
                 '4' : {'kousei': 1/6,'husei':1/10
                 '5' : {'kousei': 1/6,'husei':1/10
                 '6' : {'kousei': 1/6,'husei':1/2}

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