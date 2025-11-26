from abc import ABC, abstractmethod
from typing import List, Dict
from datetime import datetime
from enum import Enum

class EventType(Enum):
    """Tipos de eventos en el sistema"""
    EMPLOYEE_ADDED = "employee_added"
    EMPLOYEE_UPDATED = "employee_updated"
    SALARY_CHANGED = "salary_changed"
    ROLE_CHANGED = "role_changed"
    EMPLOYEE_TERMINATED = "employee_terminated"


class Observer(ABC):
    """Interfaz para observadores"""
    
    @abstractmethod
    def update(self, event_type: EventType, data: Dict):
        """
        Método llamado cuando ocurre un evento
        
        Args:
            event_type: Tipo de evento ocurrido
            data: Datos relacionados con el evento
        """
        pass


class Subject:
    """Sujeto observable que mantiene lista de observadores"""
    
    def __init__(self):
        self._observers: List[Observer] = []
    
    def attach(self, observer: Observer):
        """Agrega un observador"""
        if observer not in self._observers:
            self._observers.append(observer)
            print(f"Observador {observer.__class__.__name__} registrado")
    
    def detach(self, observer: Observer):
        """Remueve un observador"""
        if observer in self._observers:
            self._observers.remove(observer)
            print(f"Observador {observer.__class__.__name__} removido")
    
    def notify(self, event_type: EventType, data: Dict):
        """Notifica a todos los observadores sobre un evento"""
        print(f"\nNotificando evento: {event_type.value}")
        for observer in self._observers:
            observer.update(event_type, data)


class AuditLogger(Observer):
    """Observador que registra todos los cambios para auditoría"""
    
    def __init__(self):
        self.audit_log: List[Dict] = []
    
    def update(self, event_type: EventType, data: Dict):
        log_entry = {
            'timestamp': datetime.now(),
            'event_type': event_type.value,
            'data': data
        }
        self.audit_log.append(log_entry)
        print(f"   [AuditLogger] Evento registrado en log de auditoría")
    
    def get_audit_trail(self) -> List[Dict]:
        """Retorna el historial completo de auditoría"""
        return self.audit_log


class EmailNotifier(Observer):
    """Observador que envía notificaciones por email"""
    
    def update(self, event_type: EventType, data: Dict):
        # Simular envío de email
        if event_type == EventType.SALARY_CHANGED:
            print(f"   [EmailNotifier] Email enviado a HR sobre cambio salarial")
            print(f"      Empleado: {data.get('employee_name')}")
            print(f"      Nuevo salario: ${data.get('new_salary'):,}")
        
        elif event_type == EventType.ROLE_CHANGED:
            print(f"   [EmailNotifier] Email enviado sobre cambio de rol")
            print(f"      Empleado: {data.get('employee_name')}")
            print(f"      Nuevo rol: {data.get('new_role')}")
        
        elif event_type == EventType.EMPLOYEE_ADDED:
            print(f"   [EmailNotifier] Email de bienvenida enviado")
            print(f"      Nuevo empleado: {data.get('employee_name')}")


class ReportGenerator(Observer):
    """Observador que actualiza reportes automáticamente"""
    
    def __init__(self):
        self.reports_updated = 0
    
    def update(self, event_type: EventType, data: Dict):
        if event_type in [EventType.EMPLOYEE_ADDED, EventType.SALARY_CHANGED, 
                          EventType.ROLE_CHANGED]:
            print(f"   [ReportGenerator] Actualizando reportes del sistema")
            self.reports_updated += 1
            print(f"      Total de actualizaciones: {self.reports_updated}")


class AnalyticsDashboard(Observer):
    """Observador que actualiza dashboard de analytics"""
    
    def __init__(self):
        self.metrics = {
            'total_employees': 0,
            'salary_changes': 0,
            'role_changes': 0
        }
    
    def update(self, event_type: EventType, data: Dict):
        if event_type == EventType.EMPLOYEE_ADDED:
            self.metrics['total_employees'] += 1
            print(f"   [AnalyticsDashboard] Dashboard actualizado")
            print(f"      Total empleados: {self.metrics['total_employees']}")
        
        elif event_type == EventType.SALARY_CHANGED:
            self.metrics['salary_changes'] += 1
            print(f"   [AnalyticsDashboard] Métricas salariales actualizadas")
        
        elif event_type == EventType.ROLE_CHANGED:
            self.metrics['role_changes'] += 1
            print(f"   [AnalyticsDashboard] Distribución de roles actualizada")


class EmployeeDatabaseObservable(Subject):
    """Base de datos de empleados observable"""
    
    def __init__(self):
        super().__init__()
        self.employees: Dict[str, Dict] = {}
    
    def add_employee(self, employee_id: str, employee_data: Dict):
        """Agrega un nuevo empleado y notifica observadores"""
        self.employees[employee_id] = employee_data
        
        self.notify(EventType.EMPLOYEE_ADDED, {
            'employee_id': employee_id,
            'employee_name': employee_data.get('name'),
            'role': employee_data.get('role'),
            'salary': employee_data.get('salary')
        })
    
    def update_salary(self, employee_id: str, new_salary: float):
        """Actualiza salario y notifica observadores"""
        if employee_id in self.employees:
            old_salary = self.employees[employee_id].get('salary')
            self.employees[employee_id]['salary'] = new_salary
            
            self.notify(EventType.SALARY_CHANGED, {
                'employee_id': employee_id,
                'employee_name': self.employees[employee_id].get('name'),
                'old_salary': old_salary,
                'new_salary': new_salary,
                'change': new_salary - old_salary
            })
    
    def update_role(self, employee_id: str, new_role: str):
        """Actualiza rol y notifica observadores"""
        if employee_id in self.employees:
            old_role = self.employees[employee_id].get('role')
            self.employees[employee_id]['role'] = new_role
            
            self.notify(EventType.ROLE_CHANGED, {
                'employee_id': employee_id,
                'employee_name': self.employees[employee_id].get('name'),
                'old_role': old_role,
                'new_role': new_role
            })


# Ejemplo de uso
if __name__ == "__main__":
    print("=" * 70)
    print("SISTEMA DE GESTIÓN DE EMPLEADOS - PATRÓN OBSERVER")
    print("=" * 70)
    
    # Crear base de datos observable
    employee_db = EmployeeDatabaseObservable()
    
    # Crear observadores
    audit_logger = AuditLogger()
    email_notifier = EmailNotifier()
    report_generator = ReportGenerator()
    analytics_dashboard = AnalyticsDashboard()
    
    # Registrar observadores
    print("\nRegistrando observadores...")
    employee_db.attach(audit_logger)
    employee_db.attach(email_notifier)
    employee_db.attach(report_generator)
    employee_db.attach(analytics_dashboard)
    
    # Operaciones que generan eventos
    print("\n" + "=" * 70)
    print("OPERACIÓN 1: Agregar nuevo empleado")
    print("=" * 70)
    employee_db.add_employee("EMP001", {
        'name': 'Carlos Martínez',
        'role': 'Desarrollador',
        'salary': 5000000
    })
    
    print("\n" + "=" * 70)
    print("OPERACIÓN 2: Cambio de salario")
    print("=" * 70)
    employee_db.update_salary("EMP001", 6000000)
    
    print("\n" + "=" * 70)
    print("OPERACIÓN 3: Cambio de rol")
    print("=" * 70)
    employee_db.update_role("EMP001", "Senior Developer")
    
    print("\n" + "=" * 70)
    print("OPERACIÓN 4: Agregar otro empleado")
    print("=" * 70)
    employee_db.add_employee("EMP002", {
        'name': 'Ana López',
        'role': 'Gerente',
        'salary': 8000000
    })
    
    # Mostrar estadísticas finales
    print("\n" + "=" * 70)
    print("ESTADÍSTICAS FINALES")
    print("=" * 70)
    print(f"Eventos registrados en auditoría: {len(audit_logger.audit_log)}")
    print(f"Reportes actualizados: {report_generator.reports_updated}")
    print(f"Métricas del dashboard: {analytics_dashboard.metrics}")