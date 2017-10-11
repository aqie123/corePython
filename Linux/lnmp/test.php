/*
create database test;
use test;
DROP TABLE IF EXISTS `auth_admin`;
CREATE TABLE `auth_admin` (
  `admin_id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `admin_name` varchar(255) NOT NULL,
  `password` char(32) NOT NULL default '',
  `avatar` varchar(200) DEFAULT NULL,
  `email` varchar(50) NOT NULL default '',
  `mobile` varchar(20) NOT NULL default '',
  `create_time` datetime NOT NULL default '1000-01-01 00:00:00',
  `update_time` datetime NOT NULL default '1000-01-01 00:00:00',
  `is_del` tinyint(1) NOT NULL DEFAULT '0',
  `salt` varchar(20) NOT NULL DEFAULT '',
  PRIMARY KEY (`admin_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COMMENT='测试表';

The supported range is ‘1000-01-01‘ to ‘9999-12-31‘.

INSERT INTO auth_admin (admin_id,admin_name) values(1,'aqie');

1.查看mysql 端口
	show global variables like 'port';
*/