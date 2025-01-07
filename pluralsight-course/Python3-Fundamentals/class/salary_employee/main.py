from employee import Employee
from employee import SalaryEmployee
from employee import HourlyEmployee

from company import Company

def main():
    my_company = Company()
    
    employee1 = SalaryEmployee('Sarah', 'Hess', 50000)
    my_company.add_employee(employee1)
    
    employee2 = HourlyEmployee('Lee', 'Smith', 25, 50)
    my_company.add_employee(employee2)
    
    employee3 = HourlyEmployee('Bob', 'Brown', 40, 15)
    my_company.add_employee(employee3)
    

    my_company.display_employees()
    my_company.pay_employees()

main()