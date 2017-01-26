from collections import namedtuple
import sys
import math
from Data import *

DtNode = namedtuple("DtNode", "fVal, nPosNeg, gain, left, right")

POS_CLASS = 'e'


def information_gain(data, f):

    # total of attribute
    neg_total = 0.0
    pos_total = 0.0

    # lists of relevant mushrooms
    neg_data = []
    pos_data = []

    for mushroom in data:
        if mushroom[f[0]] is f[0]:
            neg_data.append(mushroom)
            neg_total += 1
        else:
            pos_data.append(mushroom)
            pos_total += 1

    pos_prob = pos_total / len(data)
    neg_prob = neg_total / len(data)

    # information gain equation
    return entropy(data) - neg_prob * entropy(neg_data) - pos_prob * entropy(pos_data)


def entropy(data):

    # total of edible and positive mushroom
    pos_total = 0.0
    neg_total = 0.0

    for mushroom in data:
        if mushroom[0] is 'e':
            pos_total += 1
        else:
            neg_total += 1

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
    node = DtNode

    # TODO: implement decision tree learning
    node.fVal = namedtuple("FeatureVal", "feature, value")
    node.nPosNeg = [0, 0]

    # maximum information gain
    node.gain = 0.0

    # left and right DTNodes
    node.left = []
    node.right = []

    # find feature of the highest information gain
    for f in features:
        info_gain = information_gain(data, f)
        if node.gain < info_gain:
            node.gain = info_gain
            node.fVal = f

    # base case edible v poisonous
    # check if info gain is less than threshold
    # entropy should naturally handle all cases
    # no need to increase entropy after split if all edible or all poisonous
    # set min info gain to zero --> grow whole tree
    # entropy below threshold? return leaf node

    if node.gain < MIN_GAIN:
        return DtNode(node.fVal[1], node.nPosNeg, node.gain, None, None)
    else:
        for mushroom in data:
            if mushroom[node.fVal[0]] is node.fVal[1]:
                node.left.append(mushroom)
                node.nPosNeg[0] += 1
            else:
                node.right.append(mushroom)
                node.nPosNeg[1] += 1

    return DtNode(node.fVal[1], node.nPosNeg, node.gain, id3(node.left, features, MIN_GAIN),
                  id3(node.right, features, MIN_GAIN))


if __name__ == "__main__":
    train = MushroomData(sys.argv[1])
    dev = MushroomData(sys.argv[2])

    dTree = id3(train.data, train.features, MIN_GAIN=float(sys.argv[3]))
    
    print_tree(dTree)

    print accuracy(dTree, dev.data)
