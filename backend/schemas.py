from pydantic import BaseModel
from typing import Optional
from datetime import date

# Factory
class FactoryBase(BaseModel):
    name: str
    location: Optional[str]
    phone: Optional[str]
    employee_count: Optional[int]
    established_date: Optional[date]

class FactoryCreate(FactoryBase):
    pass

class FactoryOut(FactoryBase):
    factory_id: int

    class Config:            # 告訴 Pydantic，模型不僅可以驗證 資料，還可從 ORM 讀取資料
        orm_mode = True

# Employee
class EmployeeBase(BaseModel):
    factory_id: int
    name: str
    position: Optional[str]
    phone: Optional[str]
    hire_date: Optional[date]

class EmployeeCreate(EmployeeBase):
    pass

class EmployeeOut(EmployeeBase):
    employee_id: int

    class Config:
        orm_mode = True

# ProductionLine
class ProductionLineBase(BaseModel):
    factory_id: int
    name: str
    status: Optional[str] = '運作中'
    capacity_per_day: Optional[int]

class ProductionLineCreate(ProductionLineBase):
    pass

class ProductionLineOut(ProductionLineBase):
    line_id: int

    class Config:
        orm_mode = True

# Product
class ProductBase(BaseModel):
    name: str
    category: Optional[str]
    price: float
    spec: Optional[str]

class ProductCreate(ProductBase):
    pass

class ProductOut(ProductBase):
    product_id: int

    class Config:
        orm_mode = True

# ProductionRecord
class ProductionRecordBase(BaseModel):
    line_id: int
    product_id: int
    produced_quantity: int
    produced_date: date
    shift: Optional[str] = '白班'
    operator_id: Optional[int]

class ProductionRecordCreate(ProductionRecordBase):
    pass

class ProductionRecordOut(ProductionRecordBase):
    record_id: int

    class Config:
        orm_mode = True
