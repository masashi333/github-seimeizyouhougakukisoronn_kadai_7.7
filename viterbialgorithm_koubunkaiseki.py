# -*- coding:utf-8 -*-
#解析の対象とする単語
target = ("こ","の","ひ","と","こ","と","で")
#単語の品詞（状態）
states = ("接尾語","名詞:普通名詞","名詞:形式名詞","連体詞","動詞語幹:一段","助詞:格助詞","助詞:接続助詞")
#単語辞書
word_dictionary = ("こ","こと","この","で","と","ひ","ひと","ひとこと")
#最初のノード
start_prob = {"文頭":0}
#遷移コスト
transit_prob = {"文頭":{"この":10,"こ":10},
                "この":{"ひとこと":10,"ひと":10,"ひ":10},
                "こ":{"の":10,"と":10},
                "の":{"ひとこと":10,"ひと":10,"ひ":10},
                "ひとこと":{"で":40},
                "ひと":{"こと":10,"こ":10},
                "ひ":{"と":10},
                "と":{"こと":10,"で":10}}
#単語コスト
emission_prob = {'この' : {'連体詞':10},
                'こ':{'名詞:普通名詞':40},
                'の':{'助詞:接続助詞':15},
                'ひとこと' : {'名詞:普通名詞':40},
                'ひ' : {'名詞:普通名詞':40},
                'と' : {'助詞:格助詞':40,'助詞:接続助詞':15},
                'こと' : {'名詞:形式名詞':40},
                'こ' : {'接尾語':20},
                'で':{'動詞語幹:一段':30,'助詞:格助詞':10}}

keitaiso_result = [["" for x in range(20)]for y in range(20)]
keitaiso_result[0][0]= 'この'
keitaiso_result[0][1]= 'ひとこと'
keitaiso_result[0][2]= 'で'
keitaiso_result[1][0]= 'この'
keitaiso_result[1][1]= 'この'
keitaiso_result[1][2]= 'この'


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
"""
if __name__=="__main__":
    print observations
    a,b = viterbi(observations,states,
                  start_prob,transit_prob,emission_prob)
    print b
    print a
"""