# -*- coding:utf-8 -*-

states = ("接尾語","名詞:形式名詞","連体詞","助動詞","助詞:格助詞","動詞語幹:一段","助詞:格助詞","助詞:接続助詞")
observations = ("こ","こと","この","で","と","ひ","ひと","ひとこと")
start_prob = {"kousei":0.5,"husei":0.5}
transit_prob = {"kousei":{"kousei":0.95,"husei":0.05},
                "husei":{"kousei":0.4,"husei":0.6}}
emission_prob = {'kousei' : {'1': 1.0/6,'2':1.0/6,'3':1.0/6,'4':1.0/6,'5':1.0/6,'6':1.0/6},
                 'husei' : {'1': 1.0/10,'2':1.0/10,'3':1.0/10,'4':1.0/10,'5':1.0/10,'6':1.0/2}}

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