# mushroom-classifier

## Background
<i>Implementation of the [ID3 decision tree learning algorithm](https://en.wikipedia.org/wiki/ID3_algorithm) as applied to a data set of edible and poisonous mushrooms.</i>

    classes: edible=e, poisonous=p
Curious about those mushrooms in your backyard? Tempted to see how they taste, but skeptical of those purple dots? <i>Well fear no more.</i> Whether on the road, on a hike, or in the kitchen, it is important to be aware of the mushrooms you're eating, and with this useful tool, your salads will be safer than ever. :mushroom:

<i>Some mushroom features include...</i>

    cap-shape
    cap-surface
    cap-color
    bruises
    odor
    gill-attachment
    gill-spacing
    gill-size
    gill-color
    stalk-shape
    stalk-root
    stalk-surface-above-ring
    stalk-surface-below-ring
    stalk-color-above-ring
    stalk-color-below-ring
    veil-type
    veil-color
    ring-number
    ring-type
    spore-print-color
    population
    habitat

####<i>Method</i>
-Attributes are chosen based on their information gain (the highest being the most desired).

-The set (mushroom) in which they are contained is then split on that desired attribute.

-This process continues until the minimum information gain can no longer be acquired.

## Results

At minimum information gain = 0.1, the classifier achieved an accuracy of 99.45%

    >FeatureVal(feature=5, value='n')	[2602, 3398]	0.532198700055
    ->FeatureVal(feature=20, value='r')	[48, 2554]	0.100113206327
    --><class '__main__.FeatureVal'>	[0, 48]	0.0
    -->FeatureVal(feature=13, value='y')	[2523, 31]	0.0603303456366
    ->FeatureVal(feature=4, value='f')	[2397, 1001]	0.382235152098
    --><class '__main__.FeatureVal'>	[0, 2397]	0.0
    -->FeatureVal(feature=11, value='c')	[385, 616]	0.388369157208
    ---><class '__main__.FeatureVal'>	[385, 0]	0.0
    --->FeatureVal(feature=11, value='r')	[147, 469]	0.464857872498
    ----><class '__main__.FeatureVal'>	[147, 0]	0.0
    ---->FeatureVal(feature=22, value='d')	[67, 402]	0.5585404951
    -----><class '__main__.FeatureVal'>	[67, 0]	0.0
    -----><class '__main__.FeatureVal'>	[0, 402]	0.0
    0.994454713494

At minimum information gain = 0, the classifier achieved an accuracy of 99.94%

    >FeatureVal(feature=5, value='n')	[2602, 3398]	0.532198700055
    ->FeatureVal(feature=20, value='r')	[48, 2554]	0.100113206327
    --><class '__main__.FeatureVal'>	[0, 48]	0.0
    -->FeatureVal(feature=13, value='y')	[37, 2517]	0.0603303456366
    --->FeatureVal(feature=8, value='b')	[11, 26]	0.617975834875
    ----><class '__main__.FeatureVal'>	[11, 0]	0.0
    ----><class '__main__.FeatureVal'>	[0, 26]	0.0
    --->FeatureVal(feature=2, value='g')	[3, 2514]	0.0100432918009
    ----><class '__main__.FeatureVal'>	[0, 3]	0.0
    ---->FeatureVal(feature=1, value='c')	[1, 2513]	0.0036031073331
    -----><class '__main__.FeatureVal'>	[0, 1]	0.0
    -----><class '__main__.FeatureVal'>	[2512, 1]	0.0
    ->FeatureVal(feature=4, value='f')	[2397, 1001]	0.382235152098
    --><class '__main__.FeatureVal'>	[0, 2397]	0.0
    -->FeatureVal(feature=11, value='c')	[385, 616]	0.388369157208
    ---><class '__main__.FeatureVal'>	[385, 0]	0.0
    --->FeatureVal(feature=11, value='r')	[147, 469]	0.464857872498
    ----><class '__main__.FeatureVal'>	[147, 0]	0.0
    ---->FeatureVal(feature=22, value='d')	[67, 402]	0.5585404951
    -----><class '__main__.FeatureVal'>	[67, 0]	0.0
    -----><class '__main__.FeatureVal'>	[0, 402]	0.0
    0.999383857055

## Sources
<i>Project completed for [Dr. Alan Ritter's](http://aritter.github.io) CSE 5523: Machine Learning and Statistical Pattern Recognition course.</i>

<i>[Mushroom data](https://archive.ics.uci.edu/ml/datasets/Mushroom) borrowed from UC Irvine's Machine Learning Repository.</i>