from sklearn.model_selection import StratifiedKFold


if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data(data, configurations, *args, **kwargs):
    label_classes, X, y = data

    kf = StratifiedKFold(
        n_splits=configurations.get('n_splits', 10),
        random_state=configurations.get('random_state', 3),
        shuffle=True,
    )

    splits = list(kf.split(X, y))

    return [
        splits,
        [dict(split_index=i) for i in range(len(splits))],
    ]