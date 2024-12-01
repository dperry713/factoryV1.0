from app.models import Employee
from app.extensions import db

def analyze_employee_performance():
    query = """
    SELECT 
        e.name AS employee_name,
        SUM(p.quantity) AS total_quantity_produced
    FROM 
        Production p
    JOIN 
        Employee e ON p.employee_id = e.id
    GROUP BY 
        e.name;
    """
    result = db.session.execute(query).fetchall()
    return [{"employee_name": row["employee_name"], "total_quantity_produced": row["total_quantity_produced"]} for row in result]

def get_all_employees():
    employees = Employee.query.all()
    return [{"id": e.id, "name": e.name, "position": e.position} for e in employees]

def get_employee_by_id(employee_id):
    employee = Employee.query.get(employee_id)
    if employee:
        return {"id": employee.id, "name": employee.name, "position": employee.position}
    return None

def create_employee(data):
    new_employee = Employee(name=data["name"], position=data["position"])
    db.session.add(new_employee)
    db.session.commit()
    return {"id": new_employee.id, "name": new_employee.name, "position": new_employee.position}

def update_employee(employee_id, data):
    employee = Employee.query.get(employee_id)
    if employee:
        employee.name = data["name"]
        employee.position = data["position"]
        db.session.commit()
        return {"id": employee.id, "name": employee.name, "position": employee.position}
    return None

def delete_employee(employee_id):
    employee = Employee.query.get(employee_id)
    if employee:
        db.session.delete(employee)
        db.session.commit()
        return True
    return False
