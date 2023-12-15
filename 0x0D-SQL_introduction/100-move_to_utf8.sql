-- Convert database hbtn_0c_0 to UTF8 (utf8mb4, collate utf8mb4_unicode_ci)

ALTER DATABASE `hbtn_0c_0` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

ALTER TABLE `first_table` CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

ALTER TABLE `first_table` MODIFY COLUMN `name` VARCHAR(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
