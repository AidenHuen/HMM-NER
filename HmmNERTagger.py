# coding=utf-8
__author__ = 'gu'
import math
from helper import Helper

class HMMNERTTagger:
    helper = Helper()
    states = helper.get_states()
    start_probability = helper.load_start_pro()
    emission_probability = helper.load_emission_pro()
    transition_probability = helper.load_transition_pro()

    def print_dptable(self, V):
        """
        打印路径概率表
        :param V:
        :return:
        """
        print "    ",
        for i in range(len(V)): print "%7d" % i,
        print

        for y in V[0].keys():
            print "%.5s:  " % y,
            for t in range(len(V)):
                print "%.7s " % ("%f" % V[t][y]),
            print


    def viterbi(self,  obs, states, start_p, trans_p, emit_p):
        """
        :param obs:观测序列
        :param states:隐状态
        :param start_p:初始概率（隐状态）
        :param trans_p:转移概率（隐状态）
        :param emit_p: 发射概率 （隐状态表现为显状态的概率）
        :return:
        """
        # 路径概率表 V[时间][隐状态] = 概率
        V = [{}]
        # 一个中间变量，代表当前状态是哪个隐状态
        path = {}

        # 初始化初始状态 (t == 0)
        for y in states:
            V[0][y] = start_p[y] * emit_p[y][obs[0]]
            path[y] = [y]

        # 对 t > 0 跑一遍维特比算法
        for t in range(1, len(obs)):
            V.append({})
            newpath = {}
            # for y0 in states:
            #     print V[t - 1][y0]
            for y in states:
                # 概率 隐状态 =    前状态是y0的概率 * y0转移到y的概率 * y表现为当前状态的概率
                (prob, state) = max([((V[t - 1][y0]*10000) * (trans_p[y0][y]*10000) * (emit_p[y][obs[t]]*10000), y0) for y0 in states])
                # 记录最大概率
                V[t][y] = prob
                # 记录路径
                newpath[y] = path[state] + [y]

            # 不需要保留旧路径
            path = newpath

        # self.print_dptable(V)
        (prob, state) = max([(V[len(obs) - 1][y], y) for y in states])
        return (prob, path[state])




    def print_tagger(self,  pathlist,sentence):
        """
        打印标签
        :param pathlist:
        :param sentence:
        :return:
        """
        tagger = []
        word_index = []
        for i in xrange(len(pathlist)):
            if pathlist[i] != '0':
                word_index.append(i)
            else:
                if len(word_index):
                    tagger.append(word_index)
                    word_index=[]
        for indexs in tagger:
            print sentence[indexs[0]:indexs[len(indexs)-1]+1],

    def split_sentence(self,sentences):
        """
        拆分句子
        :param sentences:
        :return:
        """
        sentences = sentences.replace(u" ",u"").replace(u"\n",u"").replace(u"\r",u"")
        sentences = sentences.replace(u"!",u"。").replace(u"！",u"。").replace(u"?",u"。")\
            .replace(u"？",u"。")\
            # .replace(u",",u"。").replace(u"，",u"。").replace(u"：",u"。")\
        #     .replace(u":",u"。").replace(u"的",u"。").replace(u"—",u"。").replace(u"、",u"").replace(u"●",u"")
        sentences = sentences.split(u"。")
        return sentences

    def tag(self, sentences):
        """
        实体标注
        :param sentences:
        :return:
        """
        if sentences.__len__() <= 1:
            return []
        else:
            sentences = self.split_sentence(sentences)
            tag_list = []
            for sentence in sentences:
                if sentence.__len__() <= 0:
                    tag_list.append("0")
                    continue
                observations = self.helper.get_observationsunicode(sentence)
                pro, tags = self.viterbi(observations,
                               self.states,
                               self.start_probability,
                               self.transition_probability,
                               self.emission_probability)
                # print "pro"+str(pro)
                # self.print_tagger(pathlist,sentence.decode("utf-8"))
                for tag in tags:
                    tag_list.append(tag)
                tag_list.append("0")
            tag_list.pop()
            return tag_list
            # observations = self.helper.get_observationsunicode(sentences)
            # pro, tags = self.viterbi(observations,
            #                    self.states,
            #                    self.start_probability,
            #                    self.transition_probability,
            #                    self.emission_probability)
            #     # print "pro"+str(pro)
            #     # self.print_tagger(pathlist,sentence.decode("utf-8"))
            #
            #
            # return tags

if __name__ == '__main__':
    """
    nr人名456
    ns地名789
    nt机构团体123
    nz其他专名101112
    """
    sentence = u'G7烽烟未散 李克强给欧盟吃“定心丸”'
    hmm = HMMNERTTagger()
    print hmm.tag(sentence)


    # while True:
    #     sentence = raw_input("请输入句子：")
    #     hmm_nerf_tagger(sentence)



