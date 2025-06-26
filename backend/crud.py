from sqlalchemy.orm import Session
import models, schemas

# ----------- Factory -----------
def create_factory(db: Session, factory: schemas.FactoryCreate):
    db_factory = models.Factory(**factory.dict())
    db.add(db_factory)
    db.commit()
    db.refresh(db_factory)
    return db_factory

def get_factories(db: Session):
    return db.query(models.Factory).all()

def get_factory(db: Session, factory_id: int):
    return db.query(models.Factory).filter(models.Factory.factory_id == factory_id).first()

def update_factory(db: Session, factory_id: int, factory: schemas.FactoryCreate):
    db_factory = get_factory(db, factory_id)
    if db_factory:
        for key, value in factory.dict().items():
            setattr(db_factory, key, value)
        db.commit()
        db.refresh(db_factory)
    return db_factory

def delete_factory(db: Session, factory_id: int):
    db_factory = get_factory(db, factory_id)
    if db_factory:
        db.delete(db_factory)
        db.commit()
    return db_factory

# ----------- Employee -----------
def create_employee(db: Session, employee: schemas.EmployeeCreate):
    db_employee = models.Employee(**employee.dict())
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return db_employee

def get_employees(db: Session):
    return db.query(models.Employee).all()

def get_employee(db: Session, employee_id: int):
    return db.query(models.Employee).filter(models.Employee.employee_id == employee_id).first()

def update_employee(db: Session, employee_id: int, employee: schemas.EmployeeCreate):
    db_employee = get_employee(db, employee_id)
    if db_employee:
        for key, value in employee.dict().items():
            setattr(db_employee, key, value)
        db.commit()
        db.refresh(db_employee)
    return db_employee

def delete_employee(db: Session, employee_id: int):
    db_employee = get_employee(db, employee_id)
    if db_employee:
        db.delete(db_employee)
        db.commit()
    return db_employee

# ----------- ProductionLine -----------
def create_line(db: Session, line: schemas.ProductionLineCreate):
    db_line = models.ProductionLine(**line.dict())
    db.add(db_line)
    db.commit()
    db.refresh(db_line)
    return db_line

def get_lines(db: Session):
    return db.query(models.ProductionLine).all()

def get_line(db: Session, line_id: int):
    return db.query(models.ProductionLine).filter(models.ProductionLine.line_id == line_id).first()

def update_line(db: Session, line_id: int, line: schemas.ProductionLineCreate):
    db_line = get_line(db, line_id)
    if db_line:
        for key, value in line.dict().items():
            setattr(db_line, key, value)
        db.commit()
        db.refresh(db_line)
    return db_line

def delete_line(db: Session, line_id: int):
    db_line = get_line(db, line_id)
    if db_line:
        db.delete(db_line)
        db.commit()
    return db_line

# ----------- Product -----------
def create_product(db: Session, product: schemas.ProductCreate):
    db_product = models.Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def get_products(db: Session):
    return db.query(models.Product).all()

def get_product(db: Session, product_id: int):
    return db.query(models.Product).filter(models.Product.product_id == product_id).first()

def update_product(db: Session, product_id: int, product: schemas.ProductCreate):
    db_product = get_product(db, product_id)
    if db_product:
        for key, value in product.dict().items():
            setattr(db_product, key, value)
        db.commit()
        db.refresh(db_product)
    return db_product

def delete_product(db: Session, product_id: int):
    db_product = get_product(db, product_id)
    if db_product:
        db.delete(db_product)
        db.commit()
    return db_product

# ----------- ProductionRecord -----------
def create_record(db: Session, record: schemas.ProductionRecordCreate):
    db_record = models.ProductionRecord(**record.dict())
    db.add(db_record)
    db.commit()
    db.refresh(db_record)
    return db_record

def get_records(db: Session):
    return db.query(models.ProductionRecord).all()

def get_record(db: Session, record_id: int):
    return db.query(models.ProductionRecord).filter(models.ProductionRecord.record_id == record_id).first()

def update_record(db: Session, record_id: int, record: schemas.ProductionRecordCreate):
    db_record = get_record(db, record_id)
    if db_record:
        for key, value in record.dict().items():
            setattr(db_record, key, value)
        db.commit()
        db.refresh(db_record)
    return db_record

def delete_record(db: Session, record_id: int):
    db_record = get_record(db, record_id)
    if db_record:
        db.delete(db_record)
        db.commit()
    return db_record
