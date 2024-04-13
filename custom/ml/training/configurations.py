if 'custom' not in globals():
    from mage_ai.data_preparation.decorators import custom
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@custom
def transform_custom(*args, **kwargs):
    return dict(
        hyperparameters=dict(
            objective='binary:logistic',
            subsample=1.0,
            tree_method='auto',
            use_label_encoder=False,
            verbosity=3,
        ),
        label_feature_name='unsubscribed',
        n_splits=10,
        random_state=3,
        test_size=0.2,
    )