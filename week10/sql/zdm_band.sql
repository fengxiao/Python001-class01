/*
 Navicat Premium Data Transfer

 Source Server         : mylocal
 Source Server Type    : MySQL
 Source Server Version : 50713
 Source Host           : localhost:3306
 Source Schema         : test

 Target Server Type    : MySQL
 Target Server Version : 50713
 File Encoding         : 65001

 Date: 06/09/2020 21:14:22
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for zdm_band
-- ----------------------------
DROP TABLE IF EXISTS `zdm_band`;
CREATE TABLE `zdm_band`  (
  `id` varchar(128) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  `band` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NULL DEFAULT NULL,
  `bandenglish` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NULL DEFAULT NULL,
  `bandchinese` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_bin ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of zdm_band
-- ----------------------------
INSERT INTO `zdm_band` VALUES ('0033d834-eaf7-11ea-858a-38002586c62f', '悦动力', NULL, '悦动力');
INSERT INTO `zdm_band` VALUES ('003a6368-eaf7-11ea-3ded-38002586c62f', '中沃', NULL, '中沃');
INSERT INTO `zdm_band` VALUES ('075a8416-eaf7-11ea-a5f1-38002586c62f', '秋林', NULL, '秋林');
INSERT INTO `zdm_band` VALUES ('0780025c-eb09-11ea-86c9-38002586c62f', 'CHANG/泰象', NULL, '象');
INSERT INTO `zdm_band` VALUES ('0be0cc1e-eaf7-11ea-8d72-38002586c62f', '潘德拉', NULL, '潘德拉');
INSERT INTO `zdm_band` VALUES ('0bf6b739-eaf7-11ea-993b-38002586c62f', 'SINGHA/胜狮', 'SINGHA', '胜狮');
INSERT INTO `zdm_band` VALUES ('1c3bb885-eb2d-11ea-8ca5-38002586c62f', 'NONGFU SPRING/农夫山泉', 'NONGFU SPRING', '农夫山泉');
INSERT INTO `zdm_band` VALUES ('1c3bb886-eb2d-11ea-877e-38002586c62f', 'Watsons/屈臣氏', 'Watsons', '屈臣氏');
INSERT INTO `zdm_band` VALUES ('1c3bb887-eb2d-11ea-afe2-38002586c62f', 'SUNTORY/三得利', 'SUNTORY', '三得利');
INSERT INTO `zdm_band` VALUES ('1c3bb888-eb2d-11ea-a3af-38002586c62f', '天地精华', '', '天地精华');
INSERT INTO `zdm_band` VALUES ('1c3bb889-eb2d-11ea-9ce5-38002586c62f', 'perrier/巴黎水', 'perrier', '黎水');
INSERT INTO `zdm_band` VALUES ('1c3bb88a-eb2d-11ea-9a43-38002586c62f', 'yineng/依能', 'yineng', '依能');
INSERT INTO `zdm_band` VALUES ('1c3bb88b-eb2d-11ea-8de3-38002586c62f', 'laoshan/崂山', 'laoshan', '崂山');
INSERT INTO `zdm_band` VALUES ('1c3bb88c-eb2d-11ea-928a-38002586c62f', 'Alpenliebe/阿尔卑斯', 'Alpenliebe', '阿尔卑斯');
INSERT INTO `zdm_band` VALUES ('1c3bb88d-eb2d-11ea-b873-38002586c62f', 'WAHAHA/娃哈哈', 'WAHAHA', '娃哈哈');
INSERT INTO `zdm_band` VALUES ('1c3bb88e-eb2d-11ea-a9d0-38002586c62f', 'Schweppes/怡泉', 'Schweppes', '怡泉');
INSERT INTO `zdm_band` VALUES ('1c3bb88f-eb2d-11ea-9250-38002586c62f', 'Genki Forest/元気森林', 'Genki Forest', '元気森林');
INSERT INTO `zdm_band` VALUES ('1c3bb890-eb2d-11ea-96b0-38002586c62f', 'mingren/名仁', 'mingren', '名仁');
INSERT INTO `zdm_band` VALUES ('1c3bb891-eb2d-11ea-9367-38002586c62f', 'Ganten/百岁山', 'Ganten', '百岁山');
INSERT INTO `zdm_band` VALUES ('1c3bb892-eb2d-11ea-a5eb-38002586c62f', 'S.PELLEGRINO/圣培露', 'S.PELLEGRINO', '圣培露');
INSERT INTO `zdm_band` VALUES ('1c3bb893-eb2d-11ea-87b6-38002586c62f', 'Liz/丽兹', 'Liz', '丽兹');
INSERT INTO `zdm_band` VALUES ('1c3bb894-eb2d-11ea-821d-38002586c62f', '优珍', '', '优珍');
INSERT INTO `zdm_band` VALUES ('1c3bb895-eb2d-11ea-8acb-38002586c62f', 'YANZHONG/延中', 'YANZHONG', '延中');
INSERT INTO `zdm_band` VALUES ('1c3bb896-eb2d-11ea-a47a-38002586c62f', 'HORIEN5°C/5°C活力恩', 'HORIEN5°C', '活力恩');
INSERT INTO `zdm_band` VALUES ('1c3bb897-eb2d-11ea-8df0-38002586c62f', 'VOSS/芙丝', 'VOSS', '芙丝');
INSERT INTO `zdm_band` VALUES ('1c3bb898-eb2d-11ea-9e4a-38002586c62f', 'SOURCY', '', 'SOURCY');
INSERT INTO `zdm_band` VALUES ('1c3bb899-eb2d-11ea-80b7-38002586c62f', 'SAN BENEDETTO/圣碧涛', '', '圣碧涛');
INSERT INTO `zdm_band` VALUES ('1c3bb89a-eb2d-11ea-a453-38002586c62f', 'Yocharm/云臣', 'Yocharm', '云臣');
INSERT INTO `zdm_band` VALUES ('1c3bb89b-eb2d-11ea-9a9e-38002586c62f', '火山鸣泉', '', '火山鸣泉');
INSERT INTO `zdm_band` VALUES ('1c3bb89c-eb2d-11ea-b1ef-38002586c62f', '倍特', '', '倍特');
INSERT INTO `zdm_band` VALUES ('1c3bb89d-eb2d-11ea-8eac-38002586c62f', '五大连池', '', '五大连池');
INSERT INTO `zdm_band` VALUES ('1c3bb89e-eb2d-11ea-945f-38002586c62f', 'NORNIR/诺伦', 'NORNIR', '诺伦');
INSERT INTO `zdm_band` VALUES ('1c3bb89f-eb2d-11ea-854b-38002586c62f', '优典', '', '优典');
INSERT INTO `zdm_band` VALUES ('1c3bb8a0-eb2d-11ea-a90b-38002586c62f', '碱法', '', '碱法');
INSERT INTO `zdm_band` VALUES ('1c3bb8a1-eb2d-11ea-a55f-38002586c62f', '栗子园', '', '栗子园');
INSERT INTO `zdm_band` VALUES ('1c3bb8a2-eb2d-11ea-8237-38002586c62f', 'SPRITZER/事必胜', 'SPRITZER', '事必胜');
INSERT INTO `zdm_band` VALUES ('1e1530a0-eaf7-11ea-8c65-38002586c62f', 'Nestle/雀巢', 'Nestle', '雀巢');
INSERT INTO `zdm_band` VALUES ('29bf8b1f-eaf7-11ea-9c66-38002586c62f', '亲亲元气', NULL, '亲亲');
INSERT INTO `zdm_band` VALUES ('39046d59-eae5-51ea-ac7e-38002586c62f', '五连发', NULL, '五连发');
INSERT INTO `zdm_band` VALUES ('3907c68e-eae5-11ea-5bbd-38002586c62f', 'Ostromecko/圣波岚', 'Ostromecko', '圣波岚');
INSERT INTO `zdm_band` VALUES ('3909bfa2-eae5-11ea-93b8-38002586c62f', 'LEO/力欧', 'LEO', '力欧');
INSERT INTO `zdm_band` VALUES ('39159e68-eae5-11ea-b5f9-38002586c62f', '健龙', NULL, '健龙');
INSERT INTO `zdm_band` VALUES ('3f8854b9-eae5-19ea-9b7b-38002586c62f', '依维世', NULL, '依维世');
INSERT INTO `zdm_band` VALUES ('3f91271e-eae5-11ea-b9b1-38002586c62f', '青可儿', NULL, '青可儿');
INSERT INTO `zdm_band` VALUES ('41c4147b-eae5-71ea-abec-38002586c62f', 'POPSS/帕泊斯', 'POPSS', '帕泊斯');
INSERT INTO `zdm_band` VALUES ('43b9ff58-eae5-11ea-9929-38002586c62f', 'Sexton/赛克斯盾', 'Sexton', '赛克斯盾');
INSERT INTO `zdm_band` VALUES ('45b552b6-eae5-11ea-9896-38002586c62f', '农心白山水', NULL, '农心白山水');
INSERT INTO `zdm_band` VALUES ('45c1ba41-eae5-12ea-aae1-38002586c62f', 'badoit/波多', 'badoit', '波多');
INSERT INTO `zdm_band` VALUES ('4936142c-eae5-61ea-b01e-38002586c62f', 'Robust/乐百氏', 'Robust', '乐百氏');
INSERT INTO `zdm_band` VALUES ('4bed4a7b-eae5-11ea-b326-38002586c62f', '晶田', NULL, '晶田');
INSERT INTO `zdm_band` VALUES ('4d855179-eae5-14ea-9e4a-38002586c62f', '宏宝莱', NULL, '宏宝莱');
INSERT INTO `zdm_band` VALUES ('4fd0e59d-eae5-11ea-9fcc-38002586c62f', '伊然', NULL, '伊然');
INSERT INTO `zdm_band` VALUES ('5104ae19-eae5-11ea-9e60-38002586c62f', '宜简', NULL, '宜简');
INSERT INTO `zdm_band` VALUES ('53a75ad0-eae5-11ea-58d8-38002586c62f', '舒小达', NULL, '舒小达');
INSERT INTO `zdm_band` VALUES ('53a86b8f-eae7-11ea-9f25-38002586c62f', 'TSINGTAO/青岛啤酒', 'TSINGTAO', '青岛啤酒');
INSERT INTO `zdm_band` VALUES ('58b13b4a-eaf7-11ea-a952-38002586c62f', '恒大', NULL, '恒大');
INSERT INTO `zdm_band` VALUES ('bd6f189b-eb08-12ea-ab5b-38002586c62f', 'AGUASSIMA/阿古西马', 'AGUASSIMA', '阿古西马');
INSERT INTO `zdm_band` VALUES ('c923d0a9-eb08-11ea-9282-38002586c62f', 'BIZOE/佰倬壹品', 'BIZOE', '佰倬');
INSERT INTO `zdm_band` VALUES ('cfe41ef0-eb08-11ea-a532-38002586c62f', '天下水坊', NULL, '天下水坊');
INSERT INTO `zdm_band` VALUES ('effaa6cb-eaf6-11ea-b498-38002586c62f', 'Coca-Cola/可口可乐', 'Coca-Cola', '可口可乐');
INSERT INTO `zdm_band` VALUES ('f713cc2a-eaf6-11ea-9039-38002586c62f', '100PLUS', NULL, '100PLUS');
INSERT INTO `zdm_band` VALUES ('fccad146-eaf6-15ea-973e-38002586c62f', '元气森林', NULL, '元气森林');

SET FOREIGN_KEY_CHECKS = 1;
