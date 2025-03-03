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