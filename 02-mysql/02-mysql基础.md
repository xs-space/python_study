### 一、约束

- 概述：
    - 就是在数据类型的基础上对某列值进一步做限定。如：非空、唯一等...
- 目的：
    - 保证数据的完整性和安全性
- 分类：
    - 单表约束：
        - 主键约束：primary key，一般结合自增auto_increment一起使用。特点：非空、唯一。
        - 非空约束：not null
        - 唯一约束：unique
        - 默认约束：default。如果我们不给值则会用默认值填充
    - 多表约束：
        - 外键约束：foreign key

- 主键约束

```mysql
# 1.建库、切库、查表
drop database if exists day02; -- 如果存在就删除day02数据库
create database day02;
use day02;
show tables;

# 2. 创建学生表。字段（id、name、gender、age）
drop table student;
create table student
(
    id     int primary key auto_increment, # 学生id  主键（非空、唯一、自增）
    name   varchar(20),                    # 学生姓名
    gender varchar(10),                    # 学生性别
    age    int                             # 学生年龄
);

# 3.给学生表添加数据
insert into student
values (1, '萧炎', '男', 33);
insert into student
values (2, '林动', '男', 33);
insert into student
values (10, '牧尘', '男', 31);

# 4.查看学生表结构和数据
desc student; -- 查看表结构
select *
from student; -- 查看表数据
```

- 单表约束

```mysql
# 1.建库、切库、查表
drop database if exists day02; -- 如果存在就删除day02数据库
create database day02;
use day02;
show tables;

# 2.创建teacher表。字段（id 主键约束；name 非空；phone 唯一约束；address 默认：北京）
create table teacher
(
    id      int primary key auto_increment, # 老师id  主键约束（非空、唯一）
    name    varchar(10) not null,           # 姓名  非空约束，必须传值，不能是null
    phone   varchar(11) unique,             # 手机号  唯一约束，不能重复
    address varchar(50) default '北京'      # 住址  默认：北京
);

# 3.添加表数据
insert into teacher
values (null, '夯哥', '13112345678', '新乡');

# 4. 查看表结构和表数据
desc teacher;
select *
from teacher;
```

### 二、delete和truncate的区别

```mysql
/*
区别：
    1.delete from只删除表数据，不会重置主键id；truncate table相当于把表摧毁了，然后创建一张和该表一模一样的新表
    2.delete from 属于DML语句，可以结合事务一起使用；truncate table属于DDL语句.
 */
# 1.delete from方式删除表数据
delete
from student;

# 3. truncate table方式删除表数据
truncate table student;
truncate student; # 效果同上
```

### 三、备份表数据

```mysql
# 1.查看源表数据
select *
from teacher;

# 2.备份表数据。只会备份表数据、列名、数据类型，不会备份约束（主键约束、唯一约束，因为它们的底层其实是索引）
-- 场景1：备份表不存在
-- 格式：create table 备份表名 select * from 源表名 where 条件...;
create table teacher_tmp
select *
from teacher;

-- 场景2：备份表存在
-- 格式：insert into 备份表名 select * from 源表名 where 条件...;
insert into teacher_tmp
select *
from teacher;

# 3.查看备份表的数据
select *
from teacher_tmp;
-- 清空备份表的数据
truncate table teacher_tmp;

# 4.模拟紧急情况下的"数据恢复"
truncate table teacher;
insert into teacher
select *
from teacher_tmp;
```

### 四、单表查询

```mysql
# 1.创建商品表
create table product
(
    pid         int primary key auto_increment, # 商品id
    pname       varchar(20),                    # 商品名
    price       double,                         # 商品单价
    category_id varchar(32)                     # 商品所属的 分类id
);

# 2.添加表数据
INSERT INTO product(pid, pname, price, category_id)
VALUES (1, '联想', 5000, 'c001');
INSERT INTO product(pid, pname, price, category_id)
VALUES (2, '海尔', 3000, 'c001');
INSERT INTO product(pid, pname, price, category_id)
VALUES (3, '雷神', 5000, null);
INSERT INTO product(pid, pname, price, category_id)
VALUES (4, '杰克琼斯', 800, 'c002');
INSERT INTO product(pid, pname, price, category_id)
VALUES (5, '真维斯', 200, 'c002');
INSERT INTO product(pid, pname, price, category_id)
VALUES (6, '花花公子', 440, null);
INSERT INTO product(pid, pname, price, category_id)
VALUES (7, '劲霸', 2000, 'c002');
INSERT INTO product(pid, pname, price, category_id)
VALUES (8, '香奈儿', 800, 'c003');
INSERT INTO product(pid, pname, price, category_id)
VALUES (9, '相宜本草', 200, 'c003');
INSERT INTO product(pid, pname, price, category_id)
VALUES (10, '面霸', 5, 'c003');
INSERT INTO product(pid, pname, price, category_id)
VALUES (11, '好想你枣', 56, 'c004');
INSERT INTO product(pid, pname, price, category_id)
VALUES (12, '香飘飘奶茶', 1, 'c005');
INSERT INTO product(pid, pname, price, category_id)
VALUES (13, '海澜之家', 1, 'c002');

-- ------------------------------- 简单查询 -------------------------------
/*
 一个单表查询的完整语法如下
    select
        distinct 列1, 列2...
    from
        数据表名
    where
        组前筛选
    group by
        分组字段
    having
        组后筛选
    order by
        排序字段 [asc | desc]
    limit
        起始索引, 数据条数;
 */
# 1.查询所有的商品
select pid, pname, price, category_id
from product;
select *
from product;

# 2.查询商品名和商品价格
select pname, price
from product;

# 3.查询结果是表达式（运算查询）：将所有商品的价格+10元进行显示
select pname, price + 10
from product;

# 4. 起别名。as 别名即可，as可以省略不写
select pname, price + 10 as 价格
from product;
select pname, price + 10 价格
from product;

-- ------------------------------- 条件查询 -------------------------------
/*
格式:
    select * from 表名 where 条件;
条件可以是:
    比较运算符:
        >, >=, <, <=, =, !=, <>
    范围判断:
        between 起始值 and 结束值     包左包右.
        in (值1, 值2, 值3);          满足任意1个条件即可.
    模糊查询:
        like '张%'       %代表任意个占位符, _代表1个占位符.
    逻辑运算符:
        and     并且的意思, 叫: 逻辑与, 要求所有的条件都要满足.
        or      或者的意思, 叫: 逻辑或, 要求满足任意1个条件即可.
        not     取反的意思, 叫: 逻辑非, 取相反的条件即可.
*/
# 1.查询商品名称为“花花公子”的商品所有信息
select *
from product
where pname = '花花公子';
select *
from product
where pname in ('花花公子');
# 2.查询价格为800商品
select *
from product
where price = 800;
select *
from product
where price in (800);
# 3.查询价格不是800的所有商品
select *
from product
where price != 800;
select *
from product
where price <> 800;
select *
from product
where price not in (800);
# 4.查询商品价格大于60元的所有商品信息
select *
from product
where price > 60;
select *
from product
where not price <= 60;
# 5.查询商品价格小于等于800元的所有商品信息
select *
from product
where price <= 800;
# 6.查询商品价格在200到1000之间所有商品
select *
from product
where price between 200 and 800; -- 包左包右
select *
from product
where price >= 200
  and price <= 800;
# 7.查询商品价格是200或800的所有商品
select *
from product
where price = 200
   or price = 800;
select *
from product
where price in (200, 800);
# 8.查询价格不是800的所有商品
select *
from product
where price != 800;
select *
from product
where price <> 800;
select *
from product
where price not in (800);
# 9.查询以'香'开头的所有商品
select *
from product
where pname like '香%';
select *
from product
where pname like '香_'; # 两个字：第1个字是香，第2个字无所谓
select *
from product
where pname like '香__';
# 三个字：第1个字是香，剩下2个字无所谓
# 10.查询第二个字为'想'的所有商品
select *
from product
where pname like '_想%';
# 11.查询没有分类的商品
select *
from product
where category_id is null;
# 12.查询有分类的商品
select *
from product
where category_id is not null;

-- ------------------------------- 案例4: 排序查询 -------------------------------
# 格式: select * from 表名 order by 排序的列1 [asc | desc], 排序的列2 [asc | desc]....;
# 单词: ascending  升序
# 1.使用价格排序(降序)

# 2.在价格排序(降序)的基础上，以分类排序(降序)


-- ------------------------------- 案例5: 聚合查询 -------------------------------
/*
概述/作用:
    聚合函数是用来操作 某列数据 的.
分类:
    count() 功能是: 统计表的总行数(总条数)
    max()   功能是: 最大值, 只针对于 数字列 有效.
    min()   功能是: 最小值, 只针对于 数字列 有效.
    sum()   功能是: 求总和, 只针对于 数字列 有效.
    avg()   功能是: 平均值, 只针对于 数字列 有效.

面试题: count(*), count(列), count(1)的区别是什么?
答案:
    1. 是否统计null值.
        count(列): 只统计该列的非null值.
        count(*), count(1): 都会统计null值.
    2. 效率问题.
        从高到低, 分别是: count(主键列) > count(1) > count(*) > count(普通列)
*/

-- 1. 求 product 表的总数据条数.

-- 2. 求商品价格的 最大值.
-- 3. 求商品价格的 最小值.
-- 4. 求商品价格的 求总和.
-- 5. 求商品价格的 平均值.

-- 扩展: 因为SQL中的 整数相除, 结果可能是小数, 所以我们可以保留指定的小数位, 让结果更好看.

-- 扩展: 四舍五入, 保留两位小数.


-- ------------------------------- 案例6: 分组查询 -------------------------------
/*
解释:
    相当于把表 按照 分组字段 分成 n个组(n份), 然后就可以对每组的数据做筛选统计了.
    逻辑分组, 数据(物理存储上)还在一起.
大白话解释:
    咱们有40个人, 分成了4组(逻辑分组), 但是上课大家还都坐到1个教室(物理上)
格式:
    select
        分组字段, 聚合函数...
    from
        表名
    where
        组前筛选
    group by
        分组字段
    having
        组后筛选;

细节:
    1. 分组查询的 查询列, 只能出现: 分组字段 或者 聚合函数.
    2. where是组前筛选, having是组后筛选.
    3. 分组查询一般要结合聚合函数一起使用, 否则没有意义.

面试题: where 和 having的区别是什么?
答案:
    where:  组前筛选, 后边不能跟聚合函数.
    having: 组后筛选, 后边可以跟聚合函数.
*/
# 1.统计各个分类商品的个数

# 2.统计各个分类商品的个数, 且只显示个数大于1的信息

# 3.统计各个分类商品的个数, 且只显示个数大于1的信息, 按照 商品总数, 降序排列.

# 4. 综合版, 统计每类商品的总价格, 只统计单价在500以上的商品信息, 且只显示总价在 2000 以上的分组信息, 然后按照总价升序排列, 求出价格最低的那个分类信息.


-- ------------------------------- 案例7: 分页查询 -------------------------------
/*
概述:
    相当于一次性从表中获取n条数据, 例如: 总条数为100条, 每页10条, 则一共有10页.
好处:
    1. 一方面可以降低服务器, 数据库的压力.
    2. 另一方面, 可以提高用户体验, 阅读性更强.
语法格式:
    limit 起始索引, 数据条数;
格式解释:
    起始索引: 表示 从索引为几的数据行, 开始获取数据. 数据表中每条数据都有自己的索引, 索引是从0开始的.
    数据条数: 表示 获取几条数据.

扩展提高: 和分页相关的4个名词如下.
    数据总条数:      select count(1) from 表名;        假设: 23条
    每页的数据总数:   产品经理, 项目经理.                 假设: 5条
    每页的起始索引:   (当前页数 - 1) * 每页的数据条数      假设: 第3页, 则: (3 - 1) * 5 = 10, 起始索引为10, 即: 从第11条数据开始获取.
    总页数:         (总条数 + 每页的数据条数 - 1) / 每页的数据条数.  注意: 这里是整除, 只要整数部分, 等价于: 求地板数.
                   例如: 总23条, 每页5条, 则:  (23 + 5 - 1) / 5 = 27 / 5 =  5
                   例如: 总25条, 每页5条, 则:  (25 + 5 - 1) / 5 = 29 / 5 =  5
*/

# 语法糖, 如果起始索引为0, 则可以省略不写.


# floor(), 求地板数, 即: 比这个数字小的所有数字中, 最大的那个整数.


# 扩展: distinct, 去重查询, 即: 去除重复的数据.

# 思考, 如何去重呢?
# 方式1: distinct

# 方式2: 分组方式.
```