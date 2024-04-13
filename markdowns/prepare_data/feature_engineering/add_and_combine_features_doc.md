## Add and combine features (aka feature extraction)

We need to join all the tables together
1. `user_profiles`.`id` == `user_emails`.`user_id`
1. `email_content`.`id` == `user_emails`.`email_id`
1. `user_profiles`.`id` == `email_content.user_emails.user_id`