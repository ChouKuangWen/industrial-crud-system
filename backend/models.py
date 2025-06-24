from sqlalchemy import Column, Integer, String, Date, Enum, DECIMAL, ForeignKey
from sqlalchemy.orm import relationship
from database import Base  # 從 database.py 匯入 Base，作為 ORM 基底類別

class Factory(Base):
    __tablename__ = "factory"  # 對應資料表名稱
    factory_id = Column(Integer, primary_key=True, index=True)  # 主鍵，自動遞增工廠編號
    name = Column(String(100), nullable=False, comment="工廠名稱")  # 工廠名稱，必填
    location = Column(String(200), comment="地址")  # 工廠地址，可空值
    phone = Column(String(20), comment="聯絡電話")  # 聯絡電話，可空值
    employee_count = Column(Integer, default=0, comment="員工人數")  # 員工總數，預設 0
    established_date = Column(Date, comment="成立日期")  # 工廠成立日期，可空值

    # 與員工一對多關聯：一個工廠有多個員工
    employees = relationship("Employee", back_populates="factory", cascade="all, delete-orphan")
    # 與生產線一對多關聯：一個工廠有多條生產線
    production_lines = relationship("ProductionLine", back_populates="factory", cascade="all, delete-orphan")

class Employee(Base):
    __tablename__ = "employee"  # 員工資料表
    employee_id = Column(Integer, primary_key=True, index=True)  # 員工主鍵，自動遞增
    factory_id = Column(Integer, ForeignKey("factory.factory_id"), nullable=False, comment="所屬工廠")  # 外鍵，指向工廠
    name = Column(String(100), nullable=False, comment="員工姓名")  # 員工姓名，必填
    position = Column(String(100), comment="職位")  # 職位名稱，可空
    phone = Column(String(20), comment="聯絡電話")  # 員工電話，可空
    hire_date = Column(Date, comment="入職日期")  # 入職日期，可空

    # 對應工廠（多對一）
    factory = relationship("Factory", back_populates="employees")
    # 與生產紀錄中操作員一對多關聯
    operated_records = relationship("ProductionRecord", back_populates="operator")

class ProductionLine(Base):
    __tablename__ = "production_line"  # 生產線資料表

    line_id = Column(Integer, primary_key=True, index=True)  # 主鍵，自動遞增生產線編號
    factory_id = Column(Integer, ForeignKey("factory.factory_id"), nullable=False, comment="所屬工廠")  # 外鍵，所屬工廠
    name = Column(String(100), nullable=False, comment="生產線名稱")  # 生產線名稱，必填
    status = Column(Enum("運作中", "停工中", "維修中"), default="運作中", comment="狀態")  # 生產線狀態
    capacity_per_day = Column(Integer, default=0, comment="每日最大產能")  # 預設最大產能，單位不限制

    # 連回工廠，多對一
    factory = relationship("Factory", back_populates="production_lines")
    # 與生產紀錄一對多
    production_records = relationship("ProductionRecord", back_populates="production_line", cascade="all, delete-orphan")

class Product(Base):
    __tablename__ = "product"  # 產品資料表

    product_id = Column(Integer, primary_key=True, index=True)  # 主鍵，自動遞增產品編號
    name = Column(String(100), nullable=False, comment="產品名稱")  # 產品名稱，必填
    category = Column(String(100), comment="分類")  # 產品分類，可空
    price = Column(DECIMAL(10, 2), nullable=False, comment="單價")  # 單價，必填
    spec = Column(String(255), comment="產品規格")  # 規格說明，可空

    # 與生產紀錄一對多關聯
    production_records = relationship("ProductionRecord", back_populates="product", cascade="all, delete-orphan")

class ProductionRecord(Base):
    __tablename__ = "production_record"  # 生產紀錄資料表

    record_id = Column(Integer, primary_key=True, index=True)  # 主鍵，紀錄編號
    line_id = Column(Integer, ForeignKey("production_line.line_id"), nullable=False)  # 生產線外鍵，必填
    product_id = Column(Integer, ForeignKey("product.product_id"), nullable=False)  # 產品外鍵，必填
    produced_quantity = Column(Integer, nullable=False, comment="生產數量")  # 生產數量，必填
    produced_date = Column(Date, nullable=False, comment="生產日期")  # 生產日期，必填
    shift = Column(Enum("白班", "夜班"), default="白班", comment="班次")  # 班次，預設白班
    operator_id = Column(Integer, ForeignKey("employee.employee_id"), comment="操作員")  # 操作員外鍵，可空

    # 連回生產線，多對一
    production_line = relationship("ProductionLine", back_populates="production_records")
    # 連回產品，多對一
    product = relationship("Product", back_populates="production_records")
    # 連回操作員，多對一
    operator = relationship("Employee", back_populates="operated_records")
