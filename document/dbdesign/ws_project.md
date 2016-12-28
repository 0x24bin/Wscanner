# ws_project

`ws_project`是存储扫描器所有项目信息的表。

 | 键名 | 类型 | 属性 | 解释
 |-----|-----|------|-----
 | id | int(11) | 非负,主键,自增 | 项目id
 | name | varchar(50) | 不可为空 | 项目名称
 | desc | text | 可为空 | 项目描述

建表语句：

```
CREATE TABLE `ws_project` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL DEFAULT '',
  `desc` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
```
