from abc import ABC, abstractmethod
from typing import Dict, List
from datetime import datetime


class EmployeeDataSource(ABC):
    """Interfaz objetivo que define cómo acceder a datos de empleados"""

    @abstractmethod
    def get_employee_data(self, employee_id: str) -> Dict:
        """Retorna datos de empleado en formato estandarizado"""
        pass

    @abstractmethod
    def get_all_employees(self) -> List[Dict]:
        """Retorna lista de todos los empleados"""
        pass


class LegacyHRSystem:
    """Sistema legacy de RRHH con interfaz diferente"""

    def __init__(self):
        # Simular datos legacy
        self.legacy_data = {
            "EMP001": {
                "full_name": "Juan Pérez García",
                "job_title": "Desarrollador Senior",
                "monthly_salary": 5500000,
                "hire_date": "2020-03-15",
                "department": "Tecnología"
            },
            "EMP002": {
                "full_name": "María González López",
                "job_title": "Gerente de Proyecto",
                "monthly_salary": 7500000,
                "hire_date": "2019-08-20",
                "department": "Administración"
            }
        }

    def fetch_employee_info(self, emp_id: str) -> Dict:
        """Método legacy para obtener info de empleado"""
        return self.legacy_data.get(emp_id, {})

    def get_employee_list(self) -> List[str]:
        """Método legacy para obtener lista de IDs"""
        return list(self.legacy_data.keys())


class ExternalPayrollAPI:
    """API externa de nómina con interfaz diferente"""

    def __init__(self):
        # Simular datos de API externa
        self.payroll_data = {
            "EMP001": {
                "name": "Juan Pérez García",
                "position": "Senior Developer",
                "salary": 5500000.0,
                "start_date": "2020-03-15T00:00:00Z",
                "division": "IT"
            },
            "EMP002": {
                "name": "María González López",
                "position": "Project Manager",
                "salary": 7500000.0,
                "start_date": "2019-08-20T00:00:00Z",
                "division": "Management"
            }
        }

    def retrieve_employee(self, id: str) -> Dict:
        """Método de API externa para recuperar empleado"""
        return self.payroll_data.get(id, {})

    def list_employees(self) -> List[Dict]:
        """Método de API externa para listar empleados"""
        return list(self.payroll_data.values())


class LegacyHRAdapter(EmployeeDataSource):
    """Adapter para el sistema legacy de RRHH"""

    def __init__(self, legacy_system: LegacyHRSystem):
        self.legacy_system = legacy_system

    def get_employee_data(self, employee_id: str) -> Dict:
        """Adapta datos del sistema legacy al formato estándar"""
        legacy_data = self.legacy_system.fetch_employee_info(employee_id)

        if not legacy_data:
            return {}

        # Convertir formato legacy al estándar
        return {
            'id': employee_id,
            'name': legacy_data['full_name'],
            'role': legacy_data['job_title'],
            'salary': legacy_data['monthly_salary'],
            'hire_date': datetime.fromisoformat(legacy_data['hire_date']),
            'department': legacy_data['department']
        }

    def get_all_employees(self) -> List[Dict]:
        """Adapta lista de empleados del sistema legacy"""
        employee_ids = self.legacy_system.get_employee_list()
        return [self.get_employee_data(emp_id) for emp_id in employee_ids if self.get_employee_data(emp_id)]


class PayrollAPIAdapter(EmployeeDataSource):
    """Adapter para la API externa de nómina"""

    def __init__(self, payroll_api: ExternalPayrollAPI):
        self.payroll_api = payroll_api

    def get_employee_data(self, employee_id: str) -> Dict:
        """Adapta datos de la API externa al formato estándar"""
        api_data = self.payroll_api.retrieve_employee(employee_id)

        if not api_data:
            return {}

        # Convertir formato API al estándar
        return {
            'id': employee_id,
            'name': api_data['name'],
            'role': api_data['position'],
            'salary': api_data['salary'],
            'hire_date': datetime.fromisoformat(api_data['start_date'].replace('Z', '+00:00')),
            'department': api_data['division']
        }

    def get_all_employees(self) -> List[Dict]:
        """Adapta lista de empleados de la API externa"""
        api_employees = self.payroll_api.list_employees()
        adapted_employees = []

        # La API externa no proporciona IDs, así que generamos uno basado en el índice
        for i, emp_data in enumerate(api_employees, 1):
            emp_id = f"EXT{i:03d}"
            adapted_data = {
                'id': emp_id,
                'name': emp_data['name'],
                'role': emp_data['position'],
                'salary': emp_data['salary'],
                'hire_date': datetime.fromisoformat(emp_data['start_date'].replace('Z', '+00:00')),
                'department': emp_data['division']
            }
            adapted_employees.append(adapted_data)

        return adapted_employees


class EmployeeDataIntegrator:
    """Integrador que usa múltiples fuentes de datos adaptadas"""

    def __init__(self):
        self.data_sources: List[EmployeeDataSource] = []

    def add_data_source(self, adapter: EmployeeDataSource):
        """Agrega una fuente de datos adaptada"""
        self.data_sources.append(adapter)

    def get_employee(self, employee_id: str) -> Dict:
        """Busca empleado en todas las fuentes adaptadas"""
        for source in self.data_sources:
            employee = source.get_employee_data(employee_id)
            if employee:
                return employee
        return {}

    def get_all_employees_from_all_sources(self) -> List[Dict]:
        """Obtiene todos los empleados de todas las fuentes"""
        all_employees = []
        for source in self.data_sources:
            all_employees.extend(source.get_all_employees())
        return all_employees


# Ejemplo de uso
if __name__ == "__main__":
    print("=" * 80)
    print("SISTEMA DE GESTIÓN DE EMPLEADOS - PATRÓN ADAPTER")
    print("=" * 80)

    # Crear sistemas legacy y externos
    legacy_system = LegacyHRSystem()
    payroll_api = ExternalPayrollAPI()

    # Crear adapters
    legacy_adapter = LegacyHRAdapter(legacy_system)
    payroll_adapter = PayrollAPIAdapter(payroll_api)

    # Crear integrador
    integrator = EmployeeDataIntegrator()
    integrator.add_data_source(legacy_adapter)
    integrator.add_data_source(payroll_adapter)

    # Consultar empleados individuales
    print("\nCONSULTA DE EMPLEADOS INDIVIDUALES")
    print("-" * 80)

    for emp_id in ["EMP001", "EMP002", "EXT001", "EXT002"]:
        employee = integrator.get_employee(emp_id)
        if employee:
            print(f"ID: {employee['id']}")
            print(f"Nombre: {employee['name']}")
            print(f"Rol: {employee['role']}")
            print(f"Salario: ${employee['salary']:,.0f}")
            print(f"Fecha de contratación: {employee['hire_date'].strftime('%Y-%m-%d')}")
            print(f"Departamento: {employee['department']}")
            print("-" * 40)
        else:
            print(f"Empleado {emp_id} no encontrado")
            print("-" * 40)

    # Obtener todos los empleados
    print("\nTODOS LOS EMPLEADOS DE TODAS LAS FUENTES")
    print("-" * 80)

    all_employees = integrator.get_all_employees_from_all_sources()
    for i, emp in enumerate(all_employees, 1):
        print(f"{i}. {emp['name']} - {emp['role']} ({emp['department']})")

    print(f"\nTotal de empleados integrados: {len(all_employees)}")

    # Demostrar flexibilidad del adapter
    print("\nDEMOSTRACIÓN DE FLEXIBILIDAD")
    print("-" * 80)
    print("Sistema legacy integrado sin modificar su código")
    print("API externa integrada sin cambiar su interfaz")
    print("Datos unificados en un formato común")
    print("Fácil agregar nuevas fuentes de datos")