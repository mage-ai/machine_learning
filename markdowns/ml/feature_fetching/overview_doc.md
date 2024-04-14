# Feature fetching

1. Get raw data from `core_data.users_v0`.
1. Prepare the data using the `prepare_data` pipeline.
1. Group the prepared data by `user_id`, select 1 row for each user that is most recent based on `delivered_at`.
1. Store each user’s feature vector as an output of a dynamic child block with a custom `block_uuid` corresponding to the user’s `user_id`.