# -*- coding:utf-8 -*-
#ランダムな値を生成するためにインポート
import random
#S1,S2,S3の3つの状態があるとする
states = ("S1","S2","S3")
#初期確率はどれも等しいとする
start_prob = {"S1":0.33,"S2":0.33,"S3":0.33}
#遷移確率
transit_prob = {"S1":{"S1":0.3,"S2":0.5,"S3":0.2},
                "S2":{"S1":0.5,"S2":0.1,"S3":0.4},
                "S3":{"S1":0.1,"S2":0.3,"S3":0.6}}
#ある状態（S1,S2,S3)のときにある文字(a,b)を出力する確率
emission_prob = {'S1' : {'a': 0.8,'b':0.2},
                 'S2' : {'a': 0.3,'b':0.7},
                 'S3' : {'a': 0.5,'b':0.5}}
#観測された文字列
observations = []
#乱数を用いて作製した正解ラベル
labels_seikai = []

#乱数を用いて観測データを作製する
def produce_observations():
    now_state = ''
    #初期確率1/3でS1,S2,S3のいずれかに遷移
    random_state = random.randint(1,99)
    if random_state <= 33:
      emission_observation('S1')
      now_state = "S1"
    elif random_state <= 66:
      emission_observation('S2')
      now_state = "S2"
    else:
      emission_observation('S3')
      now_state = "S3"
    #100個の観測データを作る
    for i in range (0,99):
      next_state = translate(now_state)
      emission_observation(next_state)
      now_state = next_state
    print "観測された文字:%s" %observations
    print "正解ラベル:%s" %labels_seikai

#ある状態の時にemission_probに従って文字を出力する
def emission_observation(state):
    random_observation = random.random()
    if state == 'S1':
      if random_observation <= 0.8:
        observations.append('a')
        labels_seikai.append('S1')
      else:
        observations.append('b')
        labels_seikai.append('S1')
    elif state == 'S2':
      if random_observation <= 0.3:
        observations.append('a')
        labels_seikai.append('S2')
      else:
        observations.append('b')
        labels_seikai.append('S2')
    else:
      if random_observation <= 0.5:
        observations.append('a')
        labels_seikai.append('S3')
      else:
        observations.append('b')
        labels_seikai.append('S3')
#状態がtransit_probに従って遷移する
def translate(now):
    random_translate = random.random()
    if now == 'S1':
      if random_translate <= 0.3:
        return 'S1'
      elif random_translate <= 0.8:
        return 'S2'
      elif random_translate <= 1.0:
        return 'S3'
    if now == 'S2':
      if random_translate <= 0.5:
        return 'S1'
      elif random_translate <= 0.6:
        return 'S2'
      elif random_translate <= 1.0:
        return 'S3'
    if now == 'S3':
      if random_translate <= 0.1:
        return 'S1'
      elif random_translate <= 0.4:
        return 'S2'
      elif random_translate <= 1.0:
        return 'S3'
#推定されたラベルの正答率を計算
def seitouritu(labels_estimate):
  zentai = 0
  seikai = 0
  for x in range(0,100):
    zentai += 1
    if labels_seikai[x] == labels_estimate[x]:
      seikai += 1
  accuracy = (seikai * 1.0 / zentai)*100
  accuracy = round(accuracy,3)
  print "正答率:%3r" %accuracy

#ビタビアルゴリズムを用いてもっとも確率の高い状態列を出力
def viterbi(observs,states,start_prob,transit_prob,emission_prob):
    T = {} # 現在の状態をキーとして値にその状態に至るまでの確率と現在の状態を持っている
    #初期確率のデータをTに入れる
    for st in states:
        T[st] = (start_prob[st]*emission_prob[st][observs[0]],[st])
    #観測された文字列をはじめから終わりまでループさせてその状態に至るまでの最大確率を持っている
    for ob in observs[1:]:
        T = next_state(ob,states,T,transit_prob,emission_prob)
    #最後3つの状態に至るまでの最大の確率をとる
    prob,labels_estimate = max([T[st] for st in T])
    return prob,labels_estimate

#次の状態に行ったときの最大確率とパスを計算
def next_state(ob,states,T,transit_prob,emission_prob):
    U = {} # 次の状態をキーとして値にその状態に至るまでの確率とパスを持っている
    for next_s in states:
        U[next_s] = (0,[])
        for now_s in states:
            p = T[now_s][0] * transit_prob[now_s][next_s] * emission_prob[next_s][ob]
            if p>U[next_s][0]:
                U[next_s] = [p,T[now_s][1]+[next_s]]
    return U

if __name__=="__main__":
    produce_observations()
    probability,labels_estimate = viterbi(observations,states,
                  start_prob,transit_prob,emission_prob)
    print "推定ラベル:%s" %labels_estimate
    print probability
    seitouritu(labels_estimate)