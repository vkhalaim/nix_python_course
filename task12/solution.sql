ALTER TABLE Users
ADD COLUMN phone_number INT;

ALTER TABLE Users
ALTER COLUMN phone_number TYPE VARCHAR(25);