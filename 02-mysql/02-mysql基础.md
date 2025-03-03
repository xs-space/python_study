### 约束

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

```mysql
-- 1. 建库, 切库, 查表.
drop database if exists day02; -- 如果存在, 就删除day02数据库.
create database day02;
use day02;
show tables;

-- 2. 创建学生表, 字段(id, name, gender, age)
drop table student;
create table student
(
    id     int primary key auto_increment, # 学生id, 主键(非空, 唯一), 自增
    name   varchar(20),                    # 学生姓名
    gender varchar(10),                    # 学生性别
    age    int                             # 学生年龄
);

-- 3. 给学生表添加数据.
insert into student
values (1, '萧炎', '男', 33);
insert into student
values (2, '林动', '男', 33);
insert into student
values (10, '牧尘', '男', 31);
insert into student
values (2, '萧薰儿', '女', 25); -- 报错, 主键2已经存在了.  主键: 唯一性.
insert into student
values (null, '萧薰儿', '女', 25);
-- 报错, 主键: 不能为空.

-- 4. 查看学生表结构 和 数据.
desc student; -- 查看表结构.
select *
from student; -- 查看表数据.
```