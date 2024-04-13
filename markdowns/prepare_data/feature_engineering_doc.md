# Feature engineering

An acronym to easily remember the steps in feature engineering: ARISES.

1. **[Add](https://www.mage.ai/blog/product-developers-guide-to-getting-started-with-ai-pt3-terraforming-dataframes) and [combine features](https://www.mage.ai/blog/product-developers-guide-to-customize-data-ai-pt2-join-merge-dataframes)** (aka feature extraction): enrich, enhance, etc.
2. **[Remove and repair features](https://www.mage.ai/blog/ditching-datetime)**: reformat, fix inconsistencies, etc.
3. **[Impute features](https://www.mage.ai/blog/estimating-lost-data)**: fill in missing values; mean imputation, median imputation, mode imputation, K-Nearest Neighbors (KNN), Multivariate Imputation by Chained Equations (MICE), etc.
4. **[Scale features](https://www.mage.ai/blog/scaling-numerical-data)**: change all the values to be similar in range; min-max scaling, standardization, robust scaling, log or power transformation, etc.
5. **[Encode features](https://www.mage.ai/blog/qualitative-data)**: convert non-numerical feature values into numbers; one-hot encoding, label encoding, mean encoding, binary encoding, hash encoding, embeddings, etc.
6. **Select features**: the features you choose to use and don’t use will affect the performance of the model; from training speed, to accuracy, precision, recall, and inference speed.