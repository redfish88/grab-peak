create table blog_user(id INTEGER PRIMARY KEY autoincrement,name VARCHAR (100),description TEXT);

insert into blog_user(name,description) values(\'阮一峰的博客\',\'测试\');

create table blog_category(id INTEGER PRIMARY KEY autoincrement,href VARCHAR (100), tag_name VARCHAR (100))

