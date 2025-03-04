### 1.多表建表-一对多

* 图解

  ![1717741065850](assets/1717741065850.png)

* 代码实现

  ```sql
  # -------------- 案例1: 多表建表之 1对多 --------------
  /*
  约束回顾:
      概述:
          就是用来保证数据的完整性 和 安全性的.
      分类:
          单表约束:
              主键约束: primary key, 一般结合自增(auto_increment) 使用.
              非空约束: not null
              唯一约束: unique
              默认约束: default
          多表约束:
              外键约束: foreign key

  多表约束详解:
      概述:
          它是用来描述多表关系的, 一般在 外表(从表)中 做限定.
      格式:
          场景1: 建表时创建, 和以前写字段的方式一样.
              [constraint 外键约束名] foreign key(外键列名) references 主表名(主键列名)
          场景2: 建表后创建.
              alter table 表名 add [constraint 外键约束名] foreign key(外键列名) references 主表名(主键列名);
          场景3: 删除外键约束.
              alter table 表名 drop foreign key 外键约束名;
      注意事项:
          1. 多表关系之 一对多建表原则: 在"多"的一方新建一列, 充当外键列, 去关联"一"的一方的主键列.
          2. 多表关系中 有外键的表称之为: 外表(从表), 有主键的表称之为: 主表.
          3. 外键约束特点(记忆): 外表的外键列 不能出现 主表的主键列 没有的数据.
  */
  -- 1. 建库, 切库, 查表.
  drop database if exists day03;
  create database if not exists day03;
  use day03;
  show tables;

  -- 2. 建表, 部门表.
  create table dept(
      id int primary key auto_increment,    # 部门id, 主键, 自增
      name varchar(10)                      # 部门名
  );
  -- 3. 建表, 员工表, 先不添加约束, 我们插入数据看看.
  create table employee(
      id int primary key auto_increment,  # 员工id
      name varchar(20),                   # 员工姓名
      salary int,                         # 工资
      dept_id int,                         # 部门id
      constraint fk_dept_em foreign key(dept_id) references dept(id)  # 设置员工表和部门表的 外键约束
  );

  -- 4. 给部门表添加数据.
  insert into dept values(null, '人事部'), (null, '财务部'), (null, '研发部');
  -- 5. 给员工表添加数据, 发现, 数据可以任意加入, 还可以出现: 员工所在的部门, 居然是部门表没有的部门 => 脏数据.
  insert into employee values(null, '刘备', 5000, 1);
  insert into employee values(null, '关羽', 50000, 3);
  insert into employee values(null, '小乔', 66666, 9);

  -- 6. 删表, 重新建表, 建表时: 添加外键约束.
  drop table dept;
  drop table employee;

  -- 7. 再次给 部门表 和 员工表添加数据, 发现: OK了, 员工所在的部门, 必须是 部门表已有的部门.
  insert into dept values(null, '人事部'), (null, '财务部'), (null, '研发部');
  insert into employee values(null, '刘备', 5000, 1);
  insert into employee values(null, '关羽', 50000, 3);
  insert into employee values(null, '小乔', 66666, 9);  -- 报错, 外表的外键列 不能出现 主表的主键列没有的数据.

  -- 8. 手动删除 外键约束, 观察: 表关系.
  alter table employee drop foreign key fk_dept_em;

  -- 9. 手动再次添加 外键约束, 即: 建表后, 添加外键约束.   掌握.
  alter table employee add foreign key(dept_id) references dept(id);

  -- 10.查看表数据.
  select * from dept;
  select * from employee;
  delete from employee where id = 4;
  ```



#### 2.多表查询

* 准备数据

  ```sql
  # -------------- 案例2: 多表查询之 交叉查询 和 连接查询 详解 --------------
  /*
  多表查询解释:
      记忆(精髓):
          多表查询的本质就是 根据关联条件 把多张表变成1张表, 然后进行 单表查询.
      分类:
          交叉查询:
          连接查询:
              内连接:
              外连接:
              扩展: 自关联(自连接)查询
          子查询:
  */
  -- 1. 建表.
  # 创建hero表
  CREATE TABLE hero(
      hid   INT PRIMARY KEY,  # 英雄id
      hname VARCHAR(255),     # 英雄名
      kongfu_id INT           # 功夫id
  );

  # 创建kongfu表
  CREATE TABLE kongfu (
      kid     INT PRIMARY KEY,    # 功夫id
      kname   VARCHAR(255)        # 功夫名
  );

  -- 2. 添加表数据.
  # 插入hero数据
  INSERT INTO hero VALUES(1, '鸠摩智', 9),(3, '乔峰', 1),(4, '虚竹', 4),(5, '段誉', 12);
  # 插入kongfu数据
  INSERT INTO kongfu VALUES(1, '降龙十八掌'),(2, '乾坤大挪移'),(3, '猴子偷桃'),(4, '天山折梅手');

  -- 3. 查看表数据.
  select * from hero;     -- 英雄表.
  select * from kongfu;   -- 功夫表
  ```

* 交叉查询

  ```sql
  # 4. 交叉查询, 查询结果是: 两张表的笛卡尔积, 即: 表A的总条数 * 表B的总条数, 会有大量的脏数据, 实际开发, 一般不用.
  -- 格式: select * from 表A, 表B;
  select * from hero, kongfu;
  ```

* 连接查询

  ```sql
  # 5. 内连接, 查询结果是: 表的交集.
  -- 场景1: 显式内连接. 格式: select * from 表A inner join 表B on 关联条件 where...;
  select * from hero h inner join kongfu kf on h.kongfu_id = kf.kid;
  select * from hero h join kongfu kf on h.kongfu_id = kf.kid;  -- inner 可以省略不写.

  -- 场景2: 隐式内连接. 格式: select * from 表A, 表B  where 关联条件...;
  select * from hero h, kongfu kf where h.kongfu_id = kf.kid;

  # 6. 外连接.
  -- 场景1: 左外连接, 查询结果是: 左表全集 + 交集.
  -- 格式: select * from 表A left outer join 表B on 关联条件 where...;
  select * from hero h left outer join kongfu kf on h.kongfu_id = kf.kid;
  select * from hero h left join kongfu kf on h.kongfu_id = kf.kid;     -- outer可以省略不写.

  -- 场景2: 右外连接, 查询结果是: 右表全集 + 交集.
  -- 格式: select * from 表A right outer join 表B on 关联条件 where...;
  select * from hero h right outer join kongfu kf on h.kongfu_id = kf.kid;
  select * from hero h right join kongfu kf on h.kongfu_id = kf.kid;     -- outer可以省略不写.
  ```

  ![1717741199900](assets/1717741199900.png)

* 子查询

  ```sql
  # -------------- 案例3: 多表查询之 子查询 详解 --------------
  /*
  子查询介绍:
      概述:
          实际开发中, 如果1个查询语句的 查询条件需要依赖 另一个查询语句的查询结果, 这种写法就叫: 子查询.
          即: 1个SQL的查询条件, 依赖另1个SQL语句的查询结果.
          外边的查询叫: 主查询(父查询), 里边的查询叫: 子查询.
      格式:
          |--------- 主查询 ---------- |  |-------- 子查询 ----------|
          select * from 表A where 字段 > (select 列名 from 表B where ....);
  */

  -- 1. 建表.
  create table category (             # 分类表
    cid varchar(32) primary key ,     # 分类id
    cname varchar(50)                 # 分类名
  );
  create table products(              # 商品表
    pid varchar(32) primary key ,     # 商品id
    pname varchar(50),                # 商品名
    price int,                        # 商品价格
    flag varchar(2),                  # 是否上架标记为：1表示上架、0表示下架
    category_id varchar(32),
    constraint products_fk foreign key (category_id) references category (cid)
  );

  -- 2. 添加表数据.
  #分类
  INSERT INTO category(cid,cname) VALUES('c001','家电');
  INSERT INTO category(cid,cname) VALUES('c002','服饰');
  INSERT INTO category(cid,cname) VALUES('c003','化妆品');
  INSERT INTO category(cid,cname) VALUES('c004','奢侈品');

  #商品
  INSERT INTO products(pid, pname,price,flag,category_id) VALUES('p001','联想',5000,'1','c001');
  INSERT INTO products(pid, pname,price,flag,category_id) VALUES('p002','海尔',3000,'1','c001');
  INSERT INTO products(pid, pname,price,flag,category_id) VALUES('p003','雷神',5000,'1','c001');
  INSERT INTO products (pid, pname,price,flag,category_id) VALUES('p004','JACK JONES',800,'1','c002');
  INSERT INTO products (pid, pname,price,flag,category_id) VALUES('p005','真维斯',200,'1','c002');
  INSERT INTO products (pid, pname,price,flag,category_id) VALUES('p006','花花公子',440,'1','c002');
  INSERT INTO products (pid, pname,price,flag,category_id) VALUES('p007','劲霸',2000,'1','c002');
  INSERT INTO products (pid, pname,price,flag,category_id) VALUES('p008','香奈儿',800,'1','c003');
  INSERT INTO products (pid, pname,price,flag,category_id) VALUES('p009','相宜本草',200,'1','c003');

  -- 3. 查看表数据.
  select * from category;
  select * from products;


  -- 4. 子查询演示.
  # 需求1: 查询哪些分类的商品已经上架
  -- Step1: 查询上架的商品, 的 分类id
  select distinct category_id from products where flag = 1;

  -- Step2: 根据上一步查出的 分类id, 找其对应的 分类名.
  select * from category where cid in ('c001', 'c002', 'c003');

  -- Step3: 把上述的分解步骤, 合并到一起, 就是: 子查询.
  select * from category where cid in (
      select distinct category_id from products where flag = 1
  );

  # 需求2: 查询所有分类商品的个数
  select
      cname,
      count(category_id) total_cnt,        -- 基于业务, 这里写 category_id 更合适.
      count(pid) total_cnt2                -- 基于效率, 这里写 pid 更合适.
  from
      category c
  left join products p on c.cid = p.category_id   -- 外连接查询
  group by cname;
  ```



#### 3. 自关联查询

* 运行 areas.sql 脚本, 创建: 区域表, 并导入数据.

  ![1717743340981](assets/1717743340981.png)

  ![1717743423905](assets/1717743423905.png)

* 代码实现

  ```sql
  # -------------- 案例4: 多表查询之 自关联(自连接)查询 详解 --------------
  -- 概述: 表自己和自己做关联查询, 就称之为: 自连接(自关联)查询.  一般用于: 省市区三级联动.
  -- 1. 建表, 插入表数据, 直接运行 areas.sql 脚本文件即可.

  -- 2. 查看表数据.
  select * from areas;

  -- 3. 初始 区域表的数据.
  select * from areas where id = '410000';        -- 查看 河南省 的信息
  select * from areas where pid = '410000';       -- 查看 河南省 所有的市的信息
  select * from areas where pid = '410700';       -- 查看 河南省新乡市 所有的县区信息


  -- 4. 查看所有省的, 所有市的, 所有县区的信息.
  select
      province.id, province.title,        -- 省的id, 省的名字
      city.id, city.title,                -- 市的id, 省的名字
      county.id, county.title             -- 县区的id, 省的名字
  from
      areas as county                                 -- 县区表
  join areas as city on county.pid = city.id          -- 市表
  join areas as province on city.pid = province.id;   -- 省表

  -- 5. 在上述查询基础上, 查看: 河南省所有的信息
  select
      province.id, province.title,        -- 省的id, 省的名字
      city.id, city.title,                -- 市的id, 省的名字
      county.id, county.title             -- 县区的id, 省的名字
  from
      areas as county                                 -- 县区表
  join areas as city on county.pid = city.id          -- 市表
  join areas as province on city.pid = province.id   -- 省表
  where province.title='河南省';



  -- 6. 在上述查询基础上, 查看: 新乡市所有的信息
  select
      province.id, province.title,        -- 省的id, 省的名字
      city.id, city.title,                -- 市的id, 省的名字
      county.id, county.title             -- 县区的id, 省的名字
  from
      areas as county                                 -- 县区表
  join areas as city on county.pid = city.id          -- 市表
  join areas as province on city.pid = province.id   -- 省表
  where city.title='新乡市';
  ```



#### 4.多表建表-多对多

* 图解

  ![1717747739273](assets/1717747739273.png)

* 代码实现

  ```sql
  # -------------- 案例5: 多表建表之 多对多 详解 --------------
  -- 建表原则: 新建中间表, 该表至少有2列, 充当外键列, 分别去关联"多"的两方的主键列.
  -- 1. 建表.
  # 学生表
  create table student(
      sid int primary key auto_increment,   # 学生id, 主键, 自增
      name varchar(10)                      # 学生姓名
  );
  # 选修课表
  create table course(
      cid int primary key auto_increment,   # 选修课id
      name varchar(10)                      # 选修课名
  );
  # 中间表
  create table stu_cur(
      id int not null unique auto_increment,    # 中间表, 自身id, 伪主键(唯一, 非空, 自增)
      sid int,                                  # 学生id
      cid int                                   # 选修课id
      # primary key(sid, cid)                     # 联合主键, 建表时添加.
  );

  -- 2. 添加外键约束.
  -- 中间表 和 学生表
  alter table stu_cur add constraint fk_stu_middle foreign key (sid) references student(sid);
  -- 中间表 和 选修课表
  alter table stu_cur add constraint fk_cur_middle foreign key (cid) references course(cid);

  -- 3. 设置中间表的 sid, cid列为: 联合主键.
  alter table stu_cur add primary key(sid, cid);

  -- 4. 添加表数据.
  # 学生表
  insert into student values(null, '曹操'), (null, '夏侯惇'), (null, '吕布');
  # 选修课表
  insert into course values(null, 'AI'), (null, 'Python大数据'), (null, '鸿蒙');
  # 中间表
  insert into stu_cur values(null, 1, 1);     -- 曹操 学 AI
  insert into stu_cur values(null, 1, 2);     -- 曹操 学 Py大数据
  insert into stu_cur values(null, 2, 1);     -- 夏侯惇 学 AI
  insert into stu_cur values(null, 2, 1);     -- 夏侯惇 学 AI, 报错. 联合主键

  -- 5. 查询结果.
  select * from student;
  select * from course;
  select * from stu_cur;

  -- 6. 扩展, 查看每个学生的选课情况.
  select
      s.sid, s.name,      -- 学生id, 学生名
      c.cid, c.name       -- 选修课id, 课程名
  from
      student s
  left join stu_cur sc on s.sid = sc.sid
  left join course c on sc.cid = c.cid;

  -- 7. 统计每个学生学了几门课.
  select
      s.name, count(c.cid) as total_cnt
  from
      student s
  left join stu_cur sc on s.sid = sc.sid
  left join course c on sc.cid = c.cid
  group by s.name;

  -- 8. 统计选修了2门课及其以上的学生姓名.
  select
      s.name, count(c.cid) as total_cnt
  from
      student s
  left join stu_cur sc on s.sid = sc.sid
  left join course c on sc.cid = c.cid
  group by s.name         -- 根据 学生名 分组
  having total_cnt >= 2;  -- 组后筛选, 选修课数 大于等于 2


  ```


#### 5.多表建表-一对一(了解)

![1717751031833](assets/1717751031833.png)



#### 6.练习题-34题导入数据

* 建库, 切库.

  ```sql
  -- ******************** 准备动作 ********************
  -- 1. 创建数据库.
  drop database if exists north_wind;
  create database north_wind; -- 我们一会儿要做的34个题用的数据源是从Git上下载的, 微软的北风项目的源数据.

  -- 2. 切换数据库.
  use north_wind;

  -- 3. 查询所有表.
  show tables;

  -- 4. 导入北风项目的数据源.
  ```

* 执行我给的脚本, 导入数据即可.

  ![1717751470434](assets/1717751470434.png)

  ![1717751505760](assets/1717751505760.png)

* 查看表结构, 表数据.

  ![1717751534320](assets/1717751534320.png)

  ![1717751859941](assets/1717751859941.png)

* 根据需求, 完成34个题目的代码实现即可.

  ```sql
  -- ******************** 以下是 34个练习题 ********************
  -- 需求1: 选中employees 表的所有数据


  -- 需求2: 查询每个客户的 ID, company name, contact name, contact title, city, 和 country.并按照国家名字排序


  -- 替换快捷键: ctrl + 字母R
  -- 需求3: 查询每一个商品的product_name, category_name, quantity_per_unit, unit_price, units_in_stock 并且通过 unit_price 字段排序
  -- 方式1: 显示内连接


  -- 方式2: 隐式内连接.


  -- 需求4: 列出所有提供了4种以上不同商品的供应商列表所需字段：supplier_id, company_name, and products_count (提供的商品种类数量).

  -- 需求5: 提取订单编号为10250的订单详情, 显示如下信息：
  -- product_name, quantity, unit_price （ order_items 表), discount , order_date 按商品名字排序


  -- 需求6: 收集运输到法国的订单的相关信息，包括订单涉及的顾客和员工信息，下单和发货日期等.


  -- 需求7: 提供订单编号为10248的相关信息，包括product name, unit price (在 order_items 表中), quantity（数量）,company_name（供应商公司名字 ，起别名 supplier_name).


  -- 需求8:  提取每件商品的详细信息，包括 商品名称（product_name）, 供应商的公司名称 (company_name，在 suppliers 表中),
  -- 类别名称 category_name, 商品单价unit_price, 和每单位商品数量quantity per unit

  -- 需求9: 另一种常见的报表需求是查询某段时间内的业务指标, 我们统计2016年7月的订单数量，

  -- 需求11: 统计每个供应商供应的商品种类数量, 结果返回供应商IDsupplier_id
  -- ，公司名字company_name ，商品种类数量（起别名products_count )使用 products 和 suppliers 表.

  -- 需求12: 我们要查找ID为10250的订单的总价（折扣前），SUM(unit_price * quantity)

  -- 需求13:  统计每个员工处理的订单总数, 结果包含员工IDemployee_id，姓名first_name 和 last_name，处理的订单总数(别名 orders_count)

  -- 需求14: 统计每个类别中的库存产品值多少钱？显示三列：category_id, category_name, 和 category_total_value, 如何计算库存商品总价：SUM(unit_price * units_in_stock)。

  -- 需求15: 计算每个员工的订单数量


  -- 需求16: 计算每个客户的下订单数 结果包含：用户id、用户公司名称、订单数量（customer_id, company_name, orders_count ）


  -- 需求17: 统计2016年6月到2016年7月用户的总下单金额并按金额从高到低排序
  -- 结果包含：顾客公司名称company_name 和总下单金额（折后实付金额）total_paid
  -- 提示：
  -- 计算实际总付款金额： SUM(unit_price quantity (1 - discount))
  -- 日期过滤 WHERE order_date >= '2016-06-01' AND order_date < '2016-08-01'


  -- 需求18: 统计客户总数和带有传真号码的客户数量
  -- 需要字段：all_customers_count 和 customers_with_fax_count


  -- 需求19: 我们要在报表中显示每种产品的库存量，但我们不想简单地将“ units_in_stock”列放在报表中。报表中只需要一个总体级别，例如低，高：
  -- 库存大于100 的可用性为高(high)
  -- 50到100的可用性为中等(moderate)
  -- 小于50的为低(low)
  -- 零库存 为 (none)


  -- 需求20: 创建一个报表，统计员工的经验水平
  -- 显示字段：first_name, last_name, hire_date, 和 experience
  -- 经验字段（experience ）：
  -- 'junior' 2014年1月1日以后雇用的员工
  -- 'middle' 在2013年1月1日之后至2014年1月1日之前雇用的员工
  -- 'senior' 2013年1月1日或之前雇用的员工

  -- 需求21: 我们的商店要针对北美地区的用户做促销活动：任何运送到北美地区（美国，加拿大) 的包裹免运费。 创建报表，查询订单编号为10720~10730 活动后的运费价格


  -- 需求22: 需求：创建客户基本信息报表, 包含字段：客户id customer_id, 公司名字 company_name
  -- 所在国家 country, 使用语言language, 使用语言language 的取值按如下规则
  -- Germany, Switzerland, and Austria 语言为德语 'German', 	UK, Canada, the USA, and Ireland -- 语言为英语 'English', 其他所有国家 'Other'


  -- 需求23: 需求：创建报表将所有产品划分为素食和非素食两类
  -- 报表中包含如下字段：产品名字 product_name, 类别名称 category_name
  -- 膳食类型 diet_type:
  -- 	非素食 'Non-vegetarian' 商品类别字段的值为 'Meat/Poultry' 和 'Seafood'.
  -- 	素食

  -- 需求24: 在引入北美地区免运费的促销策略时，我们也想知道运送到北美地区和其它国家地区的订单数量
  -- 促销策略, 参见需求21的代码.


  -- 需求25: 创建报表统计供应商来自那个大洲, 报表中包含两个字段：供应商来自哪个大洲（supplier_continent ）和 供应产品种类数量（product_count）
  -- 供应商来自哪个大洲（supplier_continent ）包含如下取值：
  -- 'North America' （供应商来自 'USA' 和 'Canada'.）
  -- 'Asia' （供应商来自 'Japan' 和 'Singapore')
  -- 'Other' (其它国家)


  -- 需求26: 需求：创建一个简单的报表来统计员工的年龄情况
  -- 报表中包含如下字段
  -- 年龄（ age ）：生日大于1980年1月1日 'young' ，其余'old'
  --  员工数量 （ employee_count）


  -- 需求27: 统计客户的contact_title 字段值为 ’Owner' 的客户数量
  -- 查询结果有两个字段：represented_by_owner 和 not_represented_by_owner



  -- 需求28: Washington (WA) 是 Northwind的主要运营地区，统计有多少订单是由华盛顿地区的员工处理的，
  -- 多少订单是有其它地区的员工处理的
  -- 结果字段： orders_wa_employees 和 orders_not_wa_employees



  -- 需求29: 创建报表，统计不同类别产品的库存量，将库存量分成两类 >30 和 <=30 两档分别统计数量
  -- 报表包含三个字段, 类别名称 category_name, 库存充足 high_availability, 库存紧张 low_availability
  -- 简化需求: 统计不同类别产品的库存量


  -- 需求30: 创建报表统计运输到法国的的订单中，打折和未打折订单的总数量
  -- 结果包含两个字段：full_price （原价）和 discounted_price（打折）
  -- select ship_country, discount from orders o, order_items oi where ship_country='France' and o.order_id = oi.order_id;  -- 184


  -- 需求31: 输出报表，统计不同供应商供应商品的总库存量，以及高价值商品的库存量（单价超过40定义为高价值）
  -- 结果显示四列：
  -- 供应商ID supplier_id
  -- 供应商公司名 company_name
  -- 由该供应商提供的总库存 all_units
  -- 由该供应商提供的高价值商品库存 expensive_units

  -- 需求32: 创建报表来为每种商品添加价格标签，贵、中等、便宜
  -- 结果包含如下字段：product_id, product_name, unit_price, 和 price_level
  -- 价格等级price_level的取值说明：
  -- 'expensive' 单价高于100的产品
  -- 'average' 单价高于40但不超过100的产品
  -- 'cheap' 其他产品



  -- 需求33: 制作报表统计所有订单的总价（不计任何折扣）对它们进行分类。
  -- 包含以下字段：
  -- 	order_id
  -- 	total_price（折扣前）
  -- 	price_group
  -- 字段 price_group 取值说明：
  -- 	'high' 总价超过2000美元
  -- 	'average'，总价在$ 600到$ 2,000之间，包括两端
  -- 	'low' 总价低于$ 600


  -- 需求34: 统计所有订单的运费，将运费高低分为三档
  -- 报表中包含三个字段
  -- low_freight freight值小于“ 40.0”的订单数
  -- avg_freight freight值大于或等于“ 40.0”但小于“ 80.0”的订单数
  -- high_freight freight值大于或等于“ 80.0”的订单数
  ```


#### 7.扩展-SQL语法

* 代码演示

  ```sql
  -- 扩展: case when
  /*
  格式:
      case
          when 条件1 then 值1
          when 条件2 then 值2
          when 条件3 then 值3
          ......
          else 值n
      end as 别名

  执行流程:
      1. case.when值选择语句, 首先会先判断条件1是否成立, 如果成立则执行对应的 值1, 整个case when语句结束.
      2. 如果条件1不成立, 则会立即执行条件2, 看其是否成立, 成立走对应的值2, 然后整个语句结束.
      3. 如果条件2不成立, 则会立即执行条件3...依次类推.
      4. 如果所有的条件都不成立, 则执行 else语句, 然后整个case.when结束.
  */
  select
      order_id, customer_id, shipped_date, ship_country,
      case
          when ship_country='France' then '法国'
          when ship_country='Germany' then '德国'
          when ship_country='Brazil' then '巴西'
          else '其它国家'
      end as new_ship_country
  from orders limit 10;

  -- 扩展: if() 函数.
  -- 格式: if(关系表达式, 值1, 值2)
  -- 执行流程: 先执行关系表达式, 看其结果是否成立, 成立则返回值1, 否则返回值2.
  select if(5 > 3, '张三', '李四');   -- 张三
  select if(5 < 3, '张三', '李四');   -- 李四

  -- 需求: 统计运输到法国的订单的数量.
  select count(*) from orders where ship_country='France';        -- 77
  select count(    if(ship_country='France', 1, null)    ) from orders;   -- 77

  select ship_country from orders;
  ```