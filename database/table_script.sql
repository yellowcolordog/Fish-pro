create database project charset utf8
collate utf8_general_ci;



create table user01(
    user_id int primary key auto_increment,
    user_account varchar(16) not null,
    user_password varchar(16) not null,
    user_name varchar(32) not null,  -- 加索引
    user_phone varchar(16) not null,
    user_email varchar(32),    
    user_sex int not null,
);
create table note01(
    note_id int primary key auto_increment,
    note_create_date datetime default now(), 
    note_creater_id int not null,
    note_creater_name varchar(32) not null,
    note_title varchar(32) not null,
    note_raise int,  --点赞
    note_drop int  --差评
)

create table note_content(
    note_content_id int primary key auto_increment,
    note_id int not null,
    note_content_word varchar(600),
    note_content_file1 

)