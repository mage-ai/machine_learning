# Build or fetch existing training set

There are 2 other pipelines that build the training set:

1. `core_data.users_v0`: fetches data from 3 tables and joins them together
2. `training_set_v0`: prepares the data

We’re using the [Global Data Products](https://docs.mage.ai/orchestration/global-data-products/overview) 
so that they can be shared and not have to recalculate on each run unless the underlying data is stale.