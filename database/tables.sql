create table blog_user(id INTEGER PRIMARY KEY auto_increment,name VARCHAR (100),description TEXT);

insert into blog_user(name,description) values('阮一峰的博客','测试');

CREATE TABLE `blog_category` (
	`id` INT(11) NOT NULL AUTO_INCREMENT,
	`href` VARCHAR(100) NULL DEFAULT NULL,
	`tag_name` VARCHAR(100) NULL DEFAULT NULL,
	PRIMARY KEY (`id`)
)
COLLATE='utf8_general_ci'
ENGINE=InnoDB
;


CREATE TABLE `article` (
	`id` INT(11) NOT NULL AUTO_INCREMENT,
	`tag_id` INT(11) NOT NULL DEFAULT '0',
	`link` VARCHAR(500) NOT NULL DEFAULT '',
	`title` VARCHAR(500) NOT NULL DEFAULT '',
	`content` TEXT NOT NULL,
	`update_time` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
	PRIMARY KEY (`id`)
)
COLLATE='utf8_general_ci'
ENGINE=InnoDB
;


