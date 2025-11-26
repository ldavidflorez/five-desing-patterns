from datetime import datetime
from typing import Optional


class Employee:
    """Clase que representa un empleado"""

    def __init__(self):
        self.name: Optional[str] = None
        self.address: Optional[str] = None
        self.phone: Optional[str] = None
        self.email: Optional[str] = None
        self.hire_date: Optional[datetime] = None
        self.role: Optional[str] = None
        self.salary: Optional[float] = None

    def __str__(self):
        return f"Employee({self.name}, {self.role}, ${self.salary})"


class EmployeeBuilder:
    """Builder para construir objetos Employee paso a paso"""

    def __init__(self):
        self.employee = Employee()

    def set_name(self, name: str):
        """Establece el nombre del empleado"""
        self.employee.name = name
        return self

    def set_address(self, address: str):
        """Establece la dirección del empleado"""
        self.employee.address = address
        return self

    def set_contact(self, phone: str, email: str):
        """Establece información de contacto"""
        self.employee.phone = phone
        self.employee.email = email
        return self

    def set_hire_date(self, hire_date: datetime):
        """Establece la fecha de contratación"""
        self.employee.hire_date = hire_date
        return self

    def set_role(self, role: str):
        """Establece el rol del empleado"""
        self.employee.role = role
        return self

    def set_salary(self, salary: float):
        """Establece el salario inicial"""
        self.employee.salary = salary
        return self

    def build(self) -> Employee:
        """Construye y retorna el objeto Employee completo"""
        if not self.employee.name or not self.employee.role:
            raise ValueError("Name and Role are required fields")
        return self.employee


# Ejemplo de uso
if __name__ == "__main__":
    # Construcción de un empleado completo
    employee1 = (
        EmployeeBuilder()
        .set_name("Juan Pérez")
        .set_address("Calle 123, Cartagena")
        .set_contact("3001234567", "juan.perez@empresa.com")
        .set_hire_date(datetime(2024, 1, 15))
        .set_role("Desarrollador")
        .set_salary(5000000)
        .build()
    )

    # Construcción de un empleado con información mínima
    employee2 = (
        EmployeeBuilder()
        .set_name("María González")
        .set_role("Gerente")
        .set_salary(8000000)
        .build()
    )

    print(employee1)  # Employee(Juan Pérez, Desarrollador, $5000000.0)
    print(employee2)  # Employee(María González, Gerente, $8000000.0)
