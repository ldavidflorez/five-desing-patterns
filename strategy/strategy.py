from abc import ABC, abstractmethod
from datetime import datetime
from typing import Dict

class SalaryCalculationStrategy(ABC):
    """Interfaz para estrategias de cálculo salarial"""
    
    @abstractmethod
    def calculate_salary(self, base_salary: float, employee_data: Dict) -> float:
        """
        Calcula el salario según la estrategia específica
        
        Args:
            base_salary: Salario base del empleado
            employee_data: Datos adicionales del empleado necesarios para el cálculo
        
        Returns:
            Salario calculado
        """
        pass
    
    @abstractmethod
    def get_strategy_name(self) -> str:
        """Retorna el nombre de la estrategia"""
        pass


class StandardSalaryStrategy(SalaryCalculationStrategy):
    """Estrategia estándar: salario base sin modificaciones"""
    
    def calculate_salary(self, base_salary: float, employee_data: Dict) -> float:
        return base_salary
    
    def get_strategy_name(self) -> str:
        return "Salario Estándar"


class PerformanceBonusStrategy(SalaryCalculationStrategy):
    """Estrategia con bono por desempeño"""
    
    def calculate_salary(self, base_salary: float, employee_data: Dict) -> float:
        performance_rating = employee_data.get('performance_rating', 0)
        
        # Bono según calificación (0-100)
        if performance_rating >= 90:
            bonus_percentage = 0.20  # 20% de bono
        elif performance_rating >= 75:
            bonus_percentage = 0.10  # 10% de bono
        elif performance_rating >= 60:
            bonus_percentage = 0.05  # 5% de bono
        else:
            bonus_percentage = 0.0
        
        return base_salary * (1 + bonus_percentage)
    
    def get_strategy_name(self) -> str:
        return "Salario con Bono por Desempeño"


class SeniorityBonusStrategy(SalaryCalculationStrategy):
    """Estrategia con bono por antigüedad"""
    
    def calculate_salary(self, base_salary: float, employee_data: Dict) -> float:
        hire_date = employee_data.get('hire_date')
        
        if not hire_date:
            return base_salary
        
        # Calcular años de servicio
        years_of_service = (datetime.now() - hire_date).days / 365.25
        
        # Bono de 2% por cada año de servicio (máximo 30%)
        seniority_bonus = min(years_of_service * 0.02, 0.30)
        
        return base_salary * (1 + seniority_bonus)
    
    def get_strategy_name(self) -> str:
        return "Salario con Bono por Antigüedad"


class CommissionBasedStrategy(SalaryCalculationStrategy):
    """Estrategia con comisiones por ventas"""
    
    def calculate_salary(self, base_salary: float, employee_data: Dict) -> float:
        sales_amount = employee_data.get('sales_amount', 0)
        commission_rate = employee_data.get('commission_rate', 0.05)  # 5% por defecto
        
        commission = sales_amount * commission_rate
        
        return base_salary + commission
    
    def get_strategy_name(self) -> str:
        return "Salario Base + Comisiones"


class ComprehensiveStrategy(SalaryCalculationStrategy):
    """Estrategia integral que combina múltiples factores"""
    
    def calculate_salary(self, base_salary: float, employee_data: Dict) -> float:
        # Base salary
        total = base_salary
        
        # Bono por desempeño
        performance_rating = employee_data.get('performance_rating', 0)
        if performance_rating >= 80:
            total *= 1.15
        
        # Bono por antigüedad
        hire_date = employee_data.get('hire_date')
        if hire_date:
            years_of_service = (datetime.now() - hire_date).days / 365.25
            seniority_bonus = min(years_of_service * 0.02, 0.20)
            total *= (1 + seniority_bonus)
        
        # Comisiones si aplica
        sales_amount = employee_data.get('sales_amount', 0)
        if sales_amount > 0:
            commission = sales_amount * 0.03
            total += commission
        
        return total
    
    def get_strategy_name(self) -> str:
        return "Estrategia Integral"


class SalaryCalculator:
    """Contexto que utiliza las estrategias de cálculo"""
    
    def __init__(self, strategy: SalaryCalculationStrategy):
        self._strategy = strategy
    
    def set_strategy(self, strategy: SalaryCalculationStrategy):
        """Cambia la estrategia de cálculo"""
        self._strategy = strategy
    
    def calculate(self, base_salary: float, employee_data: Dict) -> Dict:
        """
        Calcula el salario usando la estrategia actual
        
        Returns:
            Diccionario con detalles del cálculo
        """
        calculated_salary = self._strategy.calculate_salary(base_salary, employee_data)
        
        return {
            'strategy': self._strategy.get_strategy_name(),
            'base_salary': base_salary,
            'final_salary': calculated_salary,
            'difference': calculated_salary - base_salary,
            'percentage_increase': ((calculated_salary - base_salary) / base_salary) * 100
        }


# Ejemplo de uso
if __name__ == "__main__":
    base_salary = 5000000
    
    # Datos del empleado
    employee_data = {
        'performance_rating': 85,
        'hire_date': datetime(2020, 3, 15),
        'sales_amount': 50000000,
        'commission_rate': 0.04
    }
    
    # Crear calculadora con estrategia estándar
    calculator = SalaryCalculator(StandardSalaryStrategy())
    
    print("=" * 60)
    print("CÁLCULOS SALARIALES CON DIFERENTES ESTRATEGIAS")
    print("=" * 60)
    
    # Probar diferentes estrategias
    strategies = [
        StandardSalaryStrategy(),
        PerformanceBonusStrategy(),
        SeniorityBonusStrategy(),
        CommissionBasedStrategy(),
        ComprehensiveStrategy()
    ]
    
    for strategy in strategies:
        calculator.set_strategy(strategy)
        result = calculator.calculate(base_salary, employee_data)
        
        print(f"\n{result['strategy']}")
        print(f"   Salario Base: ${result['base_salary']:,.0f}")
        print(f"   Salario Final: ${result['final_salary']:,.0f}")
        print(f"   Incremento: ${result['difference']:,.0f} ({result['percentage_increase']:.1f}%)")