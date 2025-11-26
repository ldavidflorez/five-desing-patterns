from abc import ABC, abstractmethod
from typing import List

class EmployeeRole(ABC):
    """Clase abstracta base para roles de empleados"""
    
    def __init__(self, title: str):
        self.title = title
    
    @abstractmethod
    def get_responsibilities(self) -> List[str]:
        """Retorna las responsabilidades del rol"""
        pass
    
    @abstractmethod
    def get_salary_range(self) -> tuple:
        """Retorna el rango salarial (min, max)"""
        pass
    
    @abstractmethod
    def get_department(self) -> str:
        """Retorna el departamento al que pertenece"""
        pass


class ManagerRole(EmployeeRole):
    """Rol de Gerente"""
    
    def __init__(self):
        super().__init__("Gerente")
    
    def get_responsibilities(self) -> List[str]:
        return [
            "Supervisar equipo de trabajo",
            "Planificación estratégica",
            "Toma de decisiones ejecutivas",
            "Gestión de presupuesto",
            "Evaluación de desempeño"
        ]
    
    def get_salary_range(self) -> tuple:
        return (8000000, 15000000)
    
    def get_department(self) -> str:
        return "Administración"


class DeveloperRole(EmployeeRole):
    """Rol de Desarrollador"""
    
    def __init__(self):
        super().__init__("Desarrollador")
    
    def get_responsibilities(self) -> List[str]:
        return [
            "Desarrollo de software",
            "Mantenimiento de código",
            "Pruebas unitarias",
            "Documentación técnica",
            "Code reviews"
        ]
    
    def get_salary_range(self) -> tuple:
        return (4000000, 10000000)
    
    def get_department(self) -> str:
        return "Tecnología"


class AccountantRole(EmployeeRole):
    """Rol de Contador"""
    
    def __init__(self):
        super().__init__("Contador")
    
    def get_responsibilities(self) -> List[str]:
        return [
            "Gestión contable",
            "Preparación de estados financieros",
            "Declaraciones tributarias",
            "Auditorías internas",
            "Control de gastos"
        ]
    
    def get_salary_range(self) -> tuple:
        return (5000000, 9000000)
    
    def get_department(self) -> str:
        return "Finanzas"


class HRSpecialistRole(EmployeeRole):
    """Rol de Especialista en Recursos Humanos"""
    
    def __init__(self):
        super().__init__("Especialista en RRHH")
    
    def get_responsibilities(self) -> List[str]:
        return [
            "Reclutamiento y selección",
            "Capacitación de personal",
            "Gestión de nómina",
            "Relaciones laborales",
            "Desarrollo organizacional"
        ]
    
    def get_salary_range(self) -> tuple:
        return (4500000, 8000000)
    
    def get_department(self) -> str:
        return "Recursos Humanos"


class EmployeeRoleFactory:
    """Factory para crear roles de empleados"""
    
    @staticmethod
    def create_role(role_type: str) -> EmployeeRole:
        """
        Crea y retorna un rol de empleado según el tipo especificado
        
        Args:
            role_type: Tipo de rol ('manager', 'developer', 'accountant', 'hr')
        
        Returns:
            Instancia del rol correspondiente
        
        Raises:
            ValueError: Si el tipo de rol no es válido
        """
        roles = {
            'manager': ManagerRole,
            'developer': DeveloperRole,
            'accountant': AccountantRole,
            'hr': HRSpecialistRole
        }
        
        role_class = roles.get(role_type.lower())
        
        if role_class is None:
            raise ValueError(f"Tipo de rol no válido: {role_type}")
        
        return role_class()
    
    @staticmethod
    def get_available_roles() -> List[str]:
        """Retorna lista de roles disponibles"""
        return ['manager', 'developer', 'accountant', 'hr']


# Ejemplo de uso
if __name__ == "__main__":
    factory = EmployeeRoleFactory()
    
    # Crear diferentes roles
    manager = factory.create_role('manager')
    developer = factory.create_role('developer')
    accountant = factory.create_role('accountant')
    
    print(f"Rol: {manager.title}")
    print(f"Departamento: {manager.get_department()}")
    print(f"Responsabilidades: {', '.join(manager.get_responsibilities()[:3])}")
    print(f"Rango salarial: ${manager.get_salary_range()[0]:,} - ${manager.get_salary_range()[1]:,}")
    
    print("\n" + "="*50 + "\n")
    
    print(f"Rol: {developer.title}")
    print(f"Departamento: {developer.get_department()}")
    print(f"Rango salarial: ${developer.get_salary_range()[0]:,} - ${developer.get_salary_range()[1]:,}")