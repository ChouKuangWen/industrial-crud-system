from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
import models, crud, schemas
from database import async_engine, AsyncSessionLocal, get_db
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with async_engine.begin() as conn:
        await conn.run_sync(models.Base.metadata.create_all)
    yield
    # 這裡可寫 shutdown 時的程式碼

app = FastAPI(lifespan=lifespan)


# 非同步 DB session dependency

async def get_db():
    async with AsyncSessionLocal() as session:
        yield session

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],     # 或指定你的前端網址，例如 ["http://127.0.0.1:5500"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Factory
@app.post("/factories", response_model=schemas.FactoryOut)
async def create_factory(factory: schemas.FactoryCreate, db: AsyncSession = Depends(get_db)):
    return await crud.create_factory(db, factory)

@app.get("/factories", response_model=list[schemas.FactoryOut])
async def list_factories(db: AsyncSession = Depends(get_db)):
    return await crud.get_factories(db)

@app.get("/factories/{factory_id}", response_model=schemas.FactoryOut)
async def read_factory(factory_id: int, db: AsyncSession = Depends(get_db)):
    result = await crud.get_factory(db, factory_id)
    if not result:
        raise HTTPException(status_code=404, detail="Factory not found")
    return result

@app.put("/factories/{factory_id}", response_model=schemas.FactoryOut)
async def update_factory(factory_id: int, factory: schemas.FactoryCreate, db: AsyncSession = Depends(get_db)):
    result = await crud.update_factory(db, factory_id, factory)
    if not result:
        raise HTTPException(status_code=404, detail="Factory not found")
    return result

@app.delete("/factories/{factory_id}")
async def delete_factory(factory_id: int, db: AsyncSession = Depends(get_db)):
    result = await crud.delete_factory(db, factory_id)
    if not result:
        raise HTTPException(status_code=404, detail="Factory not found")
    return {"msg": "Deleted"}

# Employee
@app.post("/employees", response_model=schemas.EmployeeOut)
async def create_employee(employee: schemas.EmployeeCreate, db: AsyncSession = Depends(get_db)):
    return await crud.create_employee(db, employee)

@app.get("/employees", response_model=list[schemas.EmployeeOut])
async def list_employees(db: AsyncSession = Depends(get_db)):
    return await crud.get_employees(db)

@app.get("/employees/{employee_id}", response_model=schemas.EmployeeOut)
async def read_employee(employee_id: int, db: AsyncSession = Depends(get_db)):
    result = await crud.get_employee(db, employee_id)
    if not result:
        raise HTTPException(status_code=404, detail="Employee not found")
    return result

@app.put("/employees/{employee_id}", response_model=schemas.EmployeeOut)
async def update_employee(employee_id: int, employee: schemas.EmployeeCreate, db: AsyncSession = Depends(get_db)):
    result = await crud.update_employee(db, employee_id, employee)
    if not result:
        raise HTTPException(status_code=404, detail="Employee not found")
    return result

@app.delete("/employees/{employee_id}")
async def delete_employee(employee_id: int, db: AsyncSession = Depends(get_db)):
    result = await crud.delete_employee(db, employee_id)
    if not result:
        raise HTTPException(status_code=404, detail="Employee not found")
    return {"msg": "Deleted"}

# ProductionLine
@app.post("/lines", response_model=schemas.ProductionLineOut)
async def create_line(line: schemas.ProductionLineCreate, db: AsyncSession = Depends(get_db)):
    return await crud.create_line(db, line)

@app.get("/lines", response_model=list[schemas.ProductionLineOut])
async def list_lines(db: AsyncSession = Depends(get_db)):
    return await crud.get_lines(db)

@app.get("/lines/{line_id}", response_model=schemas.ProductionLineOut)
async def read_line(line_id: int, db: AsyncSession = Depends(get_db)):
    result = await crud.get_line(db, line_id)
    if not result:
        raise HTTPException(status_code=404, detail="Line not found")
    return result

@app.put("/lines/{line_id}", response_model=schemas.ProductionLineOut)
async def update_line(line_id: int, line: schemas.ProductionLineCreate, db: AsyncSession = Depends(get_db)):
    result = await crud.update_line(db, line_id, line)
    if not result:
        raise HTTPException(status_code=404, detail="Line not found")
    return result

@app.delete("/lines/{line_id}")
async def delete_line(line_id: int, db: AsyncSession = Depends(get_db)):
    result = await crud.delete_line(db, line_id)
    if not result:
        raise HTTPException(status_code=404, detail="Line not found")
    return {"msg": "Deleted"}

# Product
@app.post("/products", response_model=schemas.ProductOut)
async def create_product(product: schemas.ProductCreate, db: AsyncSession = Depends(get_db)):
    return await crud.create_product(db, product)

@app.get("/products", response_model=list[schemas.ProductOut])
async def list_products(db: AsyncSession = Depends(get_db)):
    return await crud.get_products(db)

@app.get("/products/{product_id}", response_model=schemas.ProductOut)
async def read_product(product_id: int, db: AsyncSession = Depends(get_db)):
    result = await crud.get_product(db, product_id)
    if not result:
        raise HTTPException(status_code=404, detail="Product not found")
    return result

@app.put("/products/{product_id}", response_model=schemas.ProductOut)
async def update_product(product_id: int, product: schemas.ProductCreate, db: AsyncSession = Depends(get_db)):
    result = await crud.update_product(db, product_id, product)
    if not result:
        raise HTTPException(status_code=404, detail="Product not found")
    return result

@app.delete("/products/{product_id}")
async def delete_product(product_id: int, db: AsyncSession = Depends(get_db)):
    result = await crud.delete_product(db, product_id)
    if not result:
        raise HTTPException(status_code=404, detail="Product not found")
    return {"msg": "Deleted"}

# ProductionRecord
@app.post("/records", response_model=schemas.ProductionRecordOut)
async def create_record(record: schemas.ProductionRecordCreate, db: AsyncSession = Depends(get_db)):
    return await crud.create_record(db, record)

@app.get("/records", response_model=list[schemas.ProductionRecordOut])
async def list_records(db: AsyncSession = Depends(get_db)):
    return await crud.get_records(db)

@app.get("/records/{record_id}", response_model=schemas.ProductionRecordOut)
async def read_record(record_id: int, db: AsyncSession = Depends(get_db)):
    result = await crud.get_record(db, record_id)
    if not result:
        raise HTTPException(status_code=404, detail="Record not found")
    return result

@app.put("/records/{record_id}", response_model=schemas.ProductionRecordOut)
async def update_record(record_id: int, record: schemas.ProductionRecordCreate, db: AsyncSession = Depends(get_db)):
    result = await crud.update_record(db, record_id, record)
    if not result:
        raise HTTPException(status_code=404, detail="Record not found")
    return result

@app.delete("/records/{record_id}")
async def delete_record(record_id: int, db: AsyncSession = Depends(get_db)):
    result = await crud.delete_record(db, record_id)
    if not result:
        raise HTTPException(status_code=404, detail="Record not found")
    return {"msg": "Deleted"}
