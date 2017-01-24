from collections import namedtuple
import sys
import math
from Data import *

DtNode = namedtuple("DtNode", "fVal, nPosNeg, gain, left, right")

POS_CLASS = 'e'


def information_gain(data, f):
    # TODO: compute information gain of this dataset after splitting on feature F

    # information gain after splitting on feature f

    # entropy of class distribution (ed/pos), not feature
    # look at entropy of node, split, and observe how much entropy is reduced

    # edible v poisonous is target for entropy

    return


def entropy(data):
    pos_total = 0
    neg_total = 0

    for mushroom in data:
        if mushroom[0] is 'e':
            pos_total += 1
        else:
            neg_total += 1

    pos_prob = pos_total / len(data)
    neg_prob = neg_total / len(data)

    return -pos_prob*math.log(pos_prob, 2) - neg_prob*math.log(neg_prob, 2)


def classify(tree, instance):
    if tree.left is None and tree.right is None:
        return tree.nPosNeg[0] > tree.nPosNeg[1]
    elif instance[tree.fVal.feature] == tree.fVal.value:
        return classify(tree.left, instance)
    else:
       return classify(tree.right, instance)


def accuracy(tree, data):
    n_correct = 0
    for d in data:
        if classify(tree, d) == (d[0] == POS_CLASS):
            n_correct += 1
    return float(n_correct) / len(data)


def print_tree(node, prefix=''):
    print("%s>%s\t%s\t%s" % (prefix, node.fVal, node.nPosNeg, node.gain))
    if node.left is not None:
        print_tree(node.left, prefix + '-')
    if node.right is not None:
        print_tree(node.right, prefix + '-')


def id3(data, features, MIN_GAIN=0.1):
    # TODO: implement decision tree learning
    # maximum entropy
    max_h = 0.0

    # base case edible v poisonous
    # check if info gain is less than threshold
    # entropy should naturally handle all cases
    # no need to increase entropy after split if all edible or all poisonous
    # set min info gain to zero --> grow whole tree
    # entropy below threshold? return leaf node

    # find best attribute
    for attribute in features:
        f_h = information_gain(data, attribute)
        if f_h > max_h:
            max_h = f_h
            f_split = attribute

    return DtNode(FeatureVal(1,'x'), (100,0), 0, None, None)


if __name__ == "__main__":
    train = MushroomData(sys.argv[1])
    dev = MushroomData(sys.argv[2])

    dTree = id3(train.data, train.features, MIN_GAIN=float(sys.argv[3]))
    
    print_tree(dTree)

    print accuracy(dTree, dev.data)
