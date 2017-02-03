from collections import namedtuple
import sys
import math
from Data import *

DtNode = namedtuple("DtNode", "fVal, nPosNeg, gain, left, right")
FeatureVal = namedtuple("FeatureVal", "feature, value")
POS_CLASS = 'e'


def information_gain(data, f):

    # total of attribute
    l_data = 0.0
    r_data = 0.0

    # lists of relevant items
    left = []
    right = []

    # assess items for feature
    for item in data:
        if item[f[0]] is f[1]:
            left.append(item)
            l_data += 1
        else:
            right.append(item)
            r_data += 1

    # calculate probability
    l_prob = l_data / len(data)
    r_prob = r_data / len(data)

    # information gain equation
    return entropy(data) - r_prob * entropy(right) - l_prob * entropy(left)


def entropy(data):

    # total of positive and negative items
    pos_total = 0.0
    neg_total = 0.0

    # tally item types (pos/neg)
    for item in data:
        if item[0] is POS_CLASS:
            pos_total += 1
        else:
            neg_total += 1

    # calculate probability (w/ smoothing)
    pos_prob = (pos_total + 1) / (len(data) + 2)
    neg_prob = (neg_total + 1) / (len(data) + 2)

    # entropy equation
    return -pos_prob * math.log(pos_prob, 2) - neg_prob * math.log(neg_prob, 2)


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
    f_val = FeatureVal

    nPosNeg = [0, 0]
    item_base = [0, 0]

    # maximum information gain
    gain = 0.0

    # left and right DTNodes
    left = []
    right = []

    # find feature of the highest information gain
    for f in features:
        info_gain = information_gain(data, f)
        if gain < info_gain:
            gain = info_gain
            f_val = f

    # base case for when information gain reaches minimum threshold
    if gain <= MIN_GAIN:
        for item in data:
            if item[0] is POS_CLASS:
                item_base[0] += 1
            else:
                item_base[1] += 1
        return DtNode(f_val, item_base, gain, None, None)

    for item in data:
        if item[f_val[0]] is f_val[1]:
            left.append(item)
            nPosNeg[0] += 1
        else:
            right.append(item)
            nPosNeg[1] += 1

    return DtNode(f_val, nPosNeg, gain, id3(left, features, MIN_GAIN),
                  id3(right, features, MIN_GAIN))


if __name__ == "__main__":
    train = MushroomData(sys.argv[1])
    dev = MushroomData(sys.argv[2])
    dTree = id3(train.data, train.features, MIN_GAIN=float(sys.argv[3]))
    
    print_tree(dTree)

    print accuracy(dTree, dev.data)
