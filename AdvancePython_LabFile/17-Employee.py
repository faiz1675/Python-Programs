# 17-WAP that extends the class Employee. Derive two classes Manager and Team Leader from 
# Employee class. Display all the details of the employee working under a particular Manager and 
# Team Leader. 


class Employee:
    def __init__(self, emp_id, name):
        self.emp_id = emp_id
        self.name = name

    def display_details(self):
        print("Employee ID:", self.emp_id)
        print("Name:", self.name)


class Manager(Employee):
    def __init__(self, emp_id, name, employees=None):
        super().__init__(emp_id, name)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_employee(self, employee):
        self.employees.append(employee)

    def display_details(self):
        super().display_details()
        print("Employees under this manager:")
        for employee in self.employees:
            employee.display_details()
            print()


class TeamLeader(Employee):
    def __init__(self, emp_id, name, employees=None):
        super().__init__(emp_id, name)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_employee(self, employee):
        self.employees.append(employee)

    def display_details(self):
        super().display_details()
        print("Employees under this team leader:")
        for employee in self.employees:
            employee.display_details()
            print()


# Create some employees
employee1 = Employee(1, "Sumit")
employee2 = Employee(2, "Himanshu")
employee3 = Employee(3, "Sadan")
employee4 = Employee(4, "Kaushik")

# Create a manager and add employees
manager = Manager(100, "Manager: Afiya Khan")
manager.add_employee(employee1)
manager.add_employee(employee2)

# Create a team leader and add employees
team_leader = TeamLeader(200, "Team Leader: Faiz")
team_leader.add_employee(employee3)
team_leader.add_employee(employee4)

# Display details of the manager and employees
print("Manager details:")
manager.display_details()

# Display details of the team leader and employees
print("Team Leader details:")
team_leader.display_details()