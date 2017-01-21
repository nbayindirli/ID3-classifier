from collections import namedtuple
import sys
import math
from Data import *

DtNode = namedtuple("DtNode", "fVal, nPosNeg, gain, left, right")

POS_CLASS = 'e'


def information_gain(data, f):
    # TODO: compute information gain of this dataset after splitting on feature F
    return 0


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
    return DtNode(FeatureVal(1,'x'), (100,0), 0, None, None)

if __name__ == "__main__":
    train = MushroomData(sys.argv[1])
    dev = MushroomData(sys.argv[2])

    dTree = id3(train.data, train.features, MIN_GAIN=float(sys.argv[3]))
    
    print_tree(dTree)

    print accuracy(dTree, dev.data)
