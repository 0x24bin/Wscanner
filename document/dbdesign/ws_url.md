# ws_url

`ws_url`是存储扫描器需要扫描的所有`url`的表。

 键名  | 类型        | 属性          | 解释
------|-------------|--------------|----
id    | int(11)     | 非负,主键,自增 | url的唯一id
pid   | int(11)     | 可为空        | project_id代表该url归属的项目
method| int(1)		| 可为空,默认为0 | url的请求方式,0代表`GET`,1代表`POST`
url	  | text 		| 不可为空		| 完整的url
raw   | text        | 不可为空		| HTTP原始请求包
sqli  | int(11)		| 可为空,默认为0 | 是否存在SQL注入,0代表`没有扫描`,1代表`正在扫描`,2代表`存在漏洞`
create_time | timestamp | 可为空,默认为当前时间 | Mysql会自动插入当前时间

建表语句：

```
CREATE TABLE `ws_url` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `pid` int(11) DEFAULT NULL,
  `method` int(1) DEFAULT '0',
  `url` text NOT NULL,
  `raw` text NOT NULL,
  `sqli` int(11) DEFAULT '0',
  `create_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
```
