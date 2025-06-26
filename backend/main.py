from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models, crud, schemas
from database import engine, SessionLocal, get_db
from fastapi.middleware.cors import CORSMiddleware

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# DB session dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ⭐ 新增 CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 或指定你的前端網址，例如 ["http://127.0.0.1:5500"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 🚀 Factory
@app.post("/factories", response_model=schemas.FactoryOut)
def create_factory(factory: schemas.FactoryCreate, db: Session = Depends(get_db)):
    return crud.create_factory(db, factory)

@app.get("/factories", response_model=list[schemas.FactoryOut])
def list_factories(db: Session = Depends(get_db)):
    return crud.get_factories(db)

@app.get("/factories/{factory_id}", response_model=schemas.FactoryOut)
def read_factory(factory_id: int, db: Session = Depends(get_db)):
    result = crud.get_factory(db, factory_id)
    if not result:
        raise HTTPException(status_code=404, detail="Factory not found")
    return result

@app.put("/factories/{factory_id}", response_model=schemas.FactoryOut)
def update_factory(factory_id: int, factory: schemas.FactoryCreate, db: Session = Depends(get_db)):
    result = crud.update_factory(db, factory_id, factory)
    if not result:
        raise HTTPException(status_code=404, detail="Factory not found")
    return result

@app.delete("/factories/{factory_id}")
def delete_factory(factory_id: int, db: Session = Depends(get_db)):
    result = crud.delete_factory(db, factory_id)
    if not result:
        raise HTTPException(status_code=404, detail="Factory not found")
    return {"msg": "Deleted"}

# 🚀 Employee
@app.post("/employees", response_model=schemas.EmployeeOut)
def create_employee(employee: schemas.EmployeeCreate, db: Session = Depends(get_db)):
    return crud.create_employee(db, employee)

@app.get("/employees", response_model=list[schemas.EmployeeOut])
def list_employees(db: Session = Depends(get_db)):
    return crud.get_employees(db)

@app.get("/employees/{employee_id}", response_model=schemas.EmployeeOut)
def read_employee(employee_id: int, db: Session = Depends(get_db)):
    result = crud.get_employee(db, employee_id)
    if not result:
        raise HTTPException(status_code=404, detail="Employee not found")
    return result

@app.put("/employees/{employee_id}", response_model=schemas.EmployeeOut)
def update_employee(employee_id: int, employee: schemas.EmployeeCreate, db: Session = Depends(get_db)):
    result = crud.update_employee(db, employee_id, employee)
    if not result:
        raise HTTPException(status_code=404, detail="Employee not found")
    return result

@app.delete("/employees/{employee_id}")
def delete_employee(employee_id: int, db: Session = Depends(get_db)):
    result = crud.delete_employee(db, employee_id)
    if not result:
        raise HTTPException(status_code=404, detail="Employee not found")
    return {"msg": "Deleted"}

# 🚀 ProductionLine
@app.post("/lines", response_model=schemas.ProductionLineOut)
def create_line(line: schemas.ProductionLineCreate, db: Session = Depends(get_db)):
    return crud.create_line(db, line)

@app.get("/lines", response_model=list[schemas.ProductionLineOut])
def list_lines(db: Session = Depends(get_db)):
    return crud.get_lines(db)

@app.get("/lines/{line_id}", response_model=schemas.ProductionLineOut)
def read_line(line_id: int, db: Session = Depends(get_db)):
    result = crud.get_line(db, line_id)
    if not result:
        raise HTTPException(status_code=404, detail="Line not found")
    return result

@app.put("/lines/{line_id}", response_model=schemas.ProductionLineOut)
def update_line(line_id: int, line: schemas.ProductionLineCreate, db: Session = Depends(get_db)):
    result = crud.update_line(db, line_id, line)
    if not result:
        raise HTTPException(status_code=404, detail="Line not found")
    return result

@app.delete("/lines/{line_id}")
def delete_line(line_id: int, db: Session = Depends(get_db)):
    result = crud.delete_line(db, line_id)
    if not result:
        raise HTTPException(status_code=404, detail="Line not found")
    return {"msg": "Deleted"}

# 🚀 Product
@app.post("/products", response_model=schemas.ProductOut)
def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    return crud.create_product(db, product)

@app.get("/products", response_model=list[schemas.ProductOut])
def list_products(db: Session = Depends(get_db)):
    return crud.get_products(db)

@app.get("/products/{product_id}", response_model=schemas.ProductOut)
def read_product(product_id: int, db: Session = Depends(get_db)):
    result = crud.get_product(db, product_id)
    if not result:
        raise HTTPException(status_code=404, detail="Product not found")
    return result

@app.put("/products/{product_id}", response_model=schemas.ProductOut)
def update_product(product_id: int, product: schemas.ProductCreate, db: Session = Depends(get_db)):
    result = crud.update_product(db, product_id, product)
    if not result:
        raise HTTPException(status_code=404, detail="Product not found")
    return result

@app.delete("/products/{product_id}")
def delete_product(product_id: int, db: Session = Depends(get_db)):
    result = crud.delete_product(db, product_id)
    if not result:
        raise HTTPException(status_code=404, detail="Product not found")
    return {"msg": "Deleted"}

# 🚀 ProductionRecord
@app.post("/records", response_model=schemas.ProductionRecordOut)
def create_record(record: schemas.ProductionRecordCreate, db: Session = Depends(get_db)):
    return crud.create_record(db, record)

@app.get("/records", response_model=list[schemas.ProductionRecordOut])
def list_records(db: Session = Depends(get_db)):
    return crud.get_records(db)

@app.get("/records/{record_id}", response_model=schemas.ProductionRecordOut)
def read_record(record_id: int, db: Session = Depends(get_db)):
    result = crud.get_record(db, record_id)
    if not result:
        raise HTTPException(status_code=404, detail="Record not found")
    return result

@app.put("/records/{record_id}", response_model=schemas.ProductionRecordOut)
def update_record(record_id: int, record: schemas.ProductionRecordCreate, db: Session = Depends(get_db)):
    result = crud.update_record(db, record_id, record)
    if not result:
        raise HTTPException(status_code=404, detail="Record not found")
    return result

@app.delete("/records/{record_id}")
def delete_record(record_id: int, db: Session = Depends(get_db)):
    result = crud.delete_record(db, record_id)
    if not result:
        raise HTTPException(status_code=404, detail="Record not found")
    return {"msg": "Deleted"}
