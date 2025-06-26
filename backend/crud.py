from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
import models, schemas
from sqlalchemy.exc import SQLAlchemyError
from fastapi import HTTPException

# ----------- Factory -----------
async def create_factory(db: AsyncSession, factory: schemas.FactoryCreate):
    db_factory = models.Factory(**factory.dict())
    db.add(db_factory)
    try:
        await db.commit()
        await db.refresh(db_factory)
        return db_factory
    except SQLAlchemyError:
        await db.rollback()
        raise HTTPException(status_code=500, detail="新增工廠時發生資料庫錯誤")

async def get_factories(db: AsyncSession):
    result = await db.execute(select(models.Factory))
    return result.scalars().all()

async def get_factory(db: AsyncSession, factory_id: int):
    result = await db.execute(select(models.Factory).where(models.Factory.factory_id == factory_id))
    return result.scalar_one_or_none()

async def update_factory(db: AsyncSession, factory_id: int, factory: schemas.FactoryCreate):
    db_factory = await get_factory(db, factory_id)
    if not db_factory:
        return None
    for key, value in factory.dict().items():
        setattr(db_factory, key, value)
    try:
        await db.commit()
        await db.refresh(db_factory)
        return db_factory
    except SQLAlchemyError:
        await db.rollback()
        raise HTTPException(status_code=500, detail="更新工廠時發生資料庫錯誤")

async def delete_factory(db: AsyncSession, factory_id: int):
    db_factory = await get_factory(db, factory_id)
    if not db_factory:
        return None
    await db.delete(db_factory)
    try:
        await db.commit()
        return db_factory
    except SQLAlchemyError:
        await db.rollback()
        raise HTTPException(status_code=500, detail="刪除工廠時發生資料庫錯誤")


# ----------- Employee -----------
async def create_employee(db: AsyncSession, employee: schemas.EmployeeCreate):
    db_employee = models.Employee(**employee.dict())
    db.add(db_employee)
    try:
        await db.commit()
        await db.refresh(db_employee)
        return db_employee
    except SQLAlchemyError:
        await db.rollback()
        raise HTTPException(status_code=500, detail="新增員工時發生資料庫錯誤")

async def get_employees(db: AsyncSession):
    result = await db.execute(select(models.Employee))
    return result.scalars().all()

async def get_employee(db: AsyncSession, employee_id: int):
    result = await db.execute(select(models.Employee).where(models.Employee.employee_id == employee_id))
    return result.scalar_one_or_none()

async def update_employee(db: AsyncSession, employee_id: int, employee: schemas.EmployeeCreate):
    db_employee = await get_employee(db, employee_id)
    if not db_employee:
        return None
    for key, value in employee.dict().items():
        setattr(db_employee, key, value)
    try:
        await db.commit()
        await db.refresh(db_employee)
        return db_employee
    except SQLAlchemyError:
        await db.rollback()
        raise HTTPException(status_code=500, detail="更新員工時發生資料庫錯誤")

async def delete_employee(db: AsyncSession, employee_id: int):
    db_employee = await get_employee(db, employee_id)
    if not db_employee:
        return None
    await db.delete(db_employee)
    try:
        await db.commit()
        return db_employee
    except SQLAlchemyError:
        await db.rollback()
        raise HTTPException(status_code=500, detail="刪除員工時發生資料庫錯誤")


# ----------- ProductionLine -----------
async def create_line(db: AsyncSession, line: schemas.ProductionLineCreate):
    db_line = models.ProductionLine(**line.dict())
    db.add(db_line)
    try:
        await db.commit()
        await db.refresh(db_line)
        return db_line
    except SQLAlchemyError:
        await db.rollback()
        raise HTTPException(status_code=500, detail="新增生產線時發生資料庫錯誤")

async def get_lines(db: AsyncSession):
    result = await db.execute(select(models.ProductionLine))
    return result.scalars().all()

async def get_line(db: AsyncSession, line_id: int):
    result = await db.execute(select(models.ProductionLine).where(models.ProductionLine.line_id == line_id))
    return result.scalar_one_or_none()

async def update_line(db: AsyncSession, line_id: int, line: schemas.ProductionLineCreate):
    db_line = await get_line(db, line_id)
    if not db_line:
        return None
    for key, value in line.dict().items():
        setattr(db_line, key, value)
    try:
        await db.commit()
        await db.refresh(db_line)
        return db_line
    except SQLAlchemyError:
        await db.rollback()
        raise HTTPException(status_code=500, detail="更新生產線時發生資料庫錯誤")

async def delete_line(db: AsyncSession, line_id: int):
    db_line = await get_line(db, line_id)
    if not db_line:
        return None
    await db.delete(db_line)
    try:
        await db.commit()
        return db_line
    except SQLAlchemyError:
        await db.rollback()
        raise HTTPException(status_code=500, detail="刪除生產線時發生資料庫錯誤")


# ----------- Product -----------
async def create_product(db: AsyncSession, product: schemas.ProductCreate):
    db_product = models.Product(**product.dict())
    db.add(db_product)
    try:
        await db.commit()
        await db.refresh(db_product)
        return db_product
    except SQLAlchemyError:
        await db.rollback()
        raise HTTPException(status_code=500, detail="新增產品時發生資料庫錯誤")

async def get_products(db: AsyncSession):
    result = await db.execute(select(models.Product))
    return result.scalars().all()

async def get_product(db: AsyncSession, product_id: int):
    result = await db.execute(select(models.Product).where(models.Product.product_id == product_id))
    return result.scalar_one_or_none()

async def update_product(db: AsyncSession, product_id: int, product: schemas.ProductCreate):
    db_product = await get_product(db, product_id)
    if not db_product:
        return None
    for key, value in product.dict().items():
        setattr(db_product, key, value)
    try:
        await db.commit()
        await db.refresh(db_product)
        return db_product
    except SQLAlchemyError:
        await db.rollback()
        raise HTTPException(status_code=500, detail="更新產品時發生資料庫錯誤")

async def delete_product(db: AsyncSession, product_id: int):
    db_product = await get_product(db, product_id)
    if not db_product:
        return None
    await db.delete(db_product)
    try:
        await db.commit()
        return db_product
    except SQLAlchemyError:
        await db.rollback()
        raise HTTPException(status_code=500, detail="刪除產品時發生資料庫錯誤")


# ----------- ProductionRecord -----------
async def create_record(db: AsyncSession, record: schemas.ProductionRecordCreate):
    db_record = models.ProductionRecord(**record.dict())
    db.add(db_record)
    try:
        await db.commit()
        await db.refresh(db_record)
        return db_record
    except SQLAlchemyError:
        await db.rollback()
        raise HTTPException(status_code=500, detail="新增生產紀錄時發生資料庫錯誤")

async def get_records(db: AsyncSession):
    result = await db.execute(select(models.ProductionRecord))
    return result.scalars().all()

async def get_record(db: AsyncSession, record_id: int):
    result = await db.execute(select(models.ProductionRecord).where(models.ProductionRecord.record_id == record_id))
    return result.scalar_one_or_none()

async def update_record(db: AsyncSession, record_id: int, record: schemas.ProductionRecordCreate):
    db_record = await get_record(db, record_id)
    if not db_record:
        return None
    for key, value in record.dict().items():
        setattr(db_record, key, value)
    try:
        await db.commit()
        await db.refresh(db_record)
        return db_record
    except SQLAlchemyError:
        await db.rollback()
        raise HTTPException(status_code=500, detail="更新生產紀錄時發生資料庫錯誤")

async def delete_record(db: AsyncSession, record_id: int):
    db_record = await get_record(db, record_id)
    if not db_record:
        return None
    await db.delete(db_record)
    try:
        await db.commit()
        return db_record
    except SQLAlchemyError:
        await db.rollback()
        raise HTTPException(status_code=500, detail="刪除生產紀錄時發生資料庫錯誤")