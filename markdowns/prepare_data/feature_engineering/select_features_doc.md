## Select features

1. Remove all the categorical features that were encoded but keep:
    1. `unsubscribed`: this is the label we’re going to predict
    1. `subject`: we used label encoder and reused the same feature name
1. Remove all the original numerical columns since we scaled them using every scaling technique