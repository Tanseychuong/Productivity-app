CREATE TABLE IF NOT EXISTS user(
    varchar(50) primary key,
    varchar(30) first_name not null,
    varchar(30) middle_name, 
    varchar(30) last_name not null,
    image profile_picture,
    text(500) bio_description
);