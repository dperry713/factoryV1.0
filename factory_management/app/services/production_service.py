from app.models import Production
from app.extensions import db

def evaluate_production_efficiency(production_date):
    query = """
    SELECT 
        prod.name AS product_name,
        SUM(p.quantity) AS total_quantity_produced
    FROM 
        Production p
    JOIN 
        Product prod ON p.product_id = prod.id
    WHERE 
        p.date = :production_date
    GROUP BY 
        prod.name;
    """
    result = db.session.execute(query, {"production_date": production_date}).fetchall()
    return [{"product_name": row["product_name"], "total_quantity_produced": row["total_quantity_produced"]} for row in result]


def get_all_production_records():
    records = Production.query.all()
    return [{"id": r.id, "product_id": r.product_id, "date": r.date} for r in records]

def get_production_record_by_id(production_id):
    record = Production.query.get(production_id)
    if record:
        return {"id": record.id, "product_id": record.product_id, "date": str(record.date)}
    return None

def create_production_record(data):
    new_record = Production(product_id=data["product_id"], date=data["date"])
    db.session.add(new_record)
    db.session.commit()
    return {"id": new_record.id, "product_id": new_record.product_id, "date": str(new_record.date)}

def update_production_record(production_id, data):
    record = Production.query.get(production_id)
    if record:
        record.product_id = data["product_id"]
        record.date = data["date"]
        db.session.commit()
        return {"id": record.id, "product_id": record.product_id, "date": str(record.date)}
    return None

def delete_production_record(production_id):
    record = Production.query.get(production_id)
    if record:
        db.session.delete(record)
        db.session.commit()
        return True
    return False
