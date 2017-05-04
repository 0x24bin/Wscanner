/*
 Navicat Premium Data Transfer

 Source Server         : localhost
 Source Server Type    : MySQL
 Source Server Version : 50542
 Source Host           : localhost
 Source Database       : Wscanner

 Target Server Type    : MySQL
 Target Server Version : 50542
 File Encoding         : utf-8

 Date: 05/05/2017 03:55:29 AM
*/

SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
--  Table structure for `ws_project`
-- ----------------------------
DROP TABLE IF EXISTS `ws_project`;
CREATE TABLE `ws_project` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL DEFAULT '',
  `desc` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
--  Table structure for `ws_url`
-- ----------------------------
DROP TABLE IF EXISTS `ws_url`;
CREATE TABLE `ws_url` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `pid` int(11) DEFAULT NULL,
  `method` varchar(10) DEFAULT 'GET',
  `url` text NOT NULL,
  `data` text,
  `headers` text NOT NULL,
  `sqli` int(11) DEFAULT '0',
  `create_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2240 DEFAULT CHARSET=utf8;

SET FOREIGN_KEY_CHECKS = 1;
