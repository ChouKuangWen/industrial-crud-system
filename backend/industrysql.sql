CREATE DATABASE IF NOT EXISTS industry
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

USE industry;

-- 工廠資料表
CREATE TABLE factory (
  factory_id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(100) NOT NULL COMMENT '工廠名稱',
  location VARCHAR(200) COMMENT '地址',
  phone VARCHAR(20) COMMENT '聯絡電話',
  employee_count INT DEFAULT 0 COMMENT '員工人數',
  established_date DATE COMMENT '成立日期'
);

-- 員工資料表
CREATE TABLE employee (
  employee_id INT AUTO_INCREMENT PRIMARY KEY,
  factory_id INT NOT NULL COMMENT '所屬工廠',
  name VARCHAR(100) NOT NULL COMMENT '員工姓名',
  position VARCHAR(100) COMMENT '職位',
  phone VARCHAR(20) COMMENT '聯絡電話',
  hire_date DATE COMMENT '入職日期',
  FOREIGN KEY (factory_id) REFERENCES factory(factory_id)
);

-- 生產線資料表
CREATE TABLE production_line (
  line_id INT AUTO_INCREMENT PRIMARY KEY,
  factory_id INT NOT NULL COMMENT '所屬工廠',
  name VARCHAR(100) NOT NULL COMMENT '生產線名稱',
  status ENUM('運作中', '停工中', '維修中') DEFAULT '運作中' COMMENT '狀態',
  capacity_per_day INT DEFAULT 0 COMMENT '每日最大產能',
  FOREIGN KEY (factory_id) REFERENCES factory(factory_id)
);

-- 產品資料表
CREATE TABLE product (
  product_id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(100) NOT NULL COMMENT '產品名稱',
  category VARCHAR(100) COMMENT '分類',
  price DECIMAL(10,2) NOT NULL COMMENT '單價',
  spec VARCHAR(255) COMMENT '產品規格'
);

-- 生產紀錄資料表
CREATE TABLE production_record (
  record_id INT AUTO_INCREMENT PRIMARY KEY,
  line_id INT NOT NULL,
  product_id INT NOT NULL,
  produced_quantity INT NOT NULL COMMENT '生產數量',
  produced_date DATE NOT NULL COMMENT '生產日期',
  shift ENUM('白班', '夜班') DEFAULT '白班' COMMENT '班次',
  operator_id INT COMMENT '操作員',
  FOREIGN KEY (line_id) REFERENCES production_line(line_id),
  FOREIGN KEY (product_id) REFERENCES product(product_id),
  FOREIGN KEY (operator_id) REFERENCES employee(employee_id)
);

-- 工廠資料
INSERT INTO factory (name, location, phone, employee_count, established_date) VALUES
('台北工廠', '台北市南港區工業一路1號', '02-12345678', 200, '2001-05-10'),
('台中工廠', '台中市西屯區工業二路2號', '04-23456789', 150, '2005-08-20'),
('高雄工廠', '高雄市前鎮區工業三路3號', '07-34567890', 300, '2010-03-15'),
('新竹工廠', '新竹市工業四路4號', '03-45678901', 100, '2015-09-12');

-- 員工資料
INSERT INTO employee (factory_id, name, position, phone, hire_date) VALUES
(1, '王小明', '生產主管', '0912000111', '2018-05-01'),
(1, '李小華', '操作員', '0912000222', '2019-06-15'),
(1, '張建國', '維修員', '0912000333', '2020-07-10'),
(2, '陳大志', '操作員', '0922000444', '2020-01-20'),
(2, '趙雲', '生產主管', '0922000555', '2017-03-10'),
(3, '林美麗', '維修員', '0933000666', '2017-03-10'),
(3, '李志豪', '操作員', '0933000777', '2018-11-05'),
(3, '洪小英', '品管員', '0933000888', '2019-12-01'),
(4, '周大為', '操作員', '0944000999', '2021-02-14'),
(4, '蔡佩珊', '生產主管', '0944000101', '2016-08-22');

-- 生產線資料
INSERT INTO production_line (factory_id, name, status, capacity_per_day) VALUES
(1, '台北A線', '運作中', 1000),
(1, '台北B線', '維修中', 800),
(2, '台中A線', '運作中', 1200),
(2, '台中B線', '運作中', 900),
(3, '高雄A線', '運作中', 1500),
(3, '高雄B線', '停工中', 1100),
(4, '新竹A線', '運作中', 700);

-- 產品資料
INSERT INTO product (name, category, price, spec) VALUES
('電子零件A', '電子', 50.00, '型號A100'),
('電子零件B', '電子', 80.00, '型號B200'),
('機械組件C', '機械', 120.00, '型號C300'),
('塑膠外殼D', '塑膠', 30.00, '型號D400'),
('電池E', '電源', 150.00, '型號E500'),
('電線F', '電子', 20.00, '型號F600');

-- 生產紀錄資料
INSERT INTO production_record (line_id, product_id, produced_quantity, produced_date, shift, operator_id) VALUES
(1, 1, 500, '2025-06-01', '白班', 2),
(1, 2, 300, '2025-06-01', '夜班', 2),
(2, 3, 400, '2025-06-02', '白班', 3),
(3, 4, 600, '2025-06-03', '夜班', 4),
(3, 5, 700, '2025-06-04', '白班', 7),
(4, 6, 200, '2025-06-05', '白班', 5),
(5, 1, 1000, '2025-06-06', '夜班', 8),
(5, 2, 500, '2025-06-06', '白班', 8),
(7, 3, 300, '2025-06-07', '白班', 9),
(7, 6, 400, '2025-06-07', '夜班', 10);
