class employee:
    #constructor
    def __init__(self , name, designation,dept,salary,skills = None):
        self.name= name
        self.designation = designation
        self.department = dept
        self.salary = salary
        self.skill = skills

    def do_task(self,task):
        print(f"employee {self.name} is doing task {task}")

    def info(self):
        print("employee details")
        print(f'name : {self.name}')
        print(f'department : {self.department}')
        print(f'salary : {self.salary}')
        print(f'skills : {" ,".join(self.skill)}')
        
    def add_skill(self , skillname):
        if self.skill is None:
            self.skill=[skillname]
        else:
            self.skill.append(skillname)
e1 = employee('raj','Assitant 2','sales',40000,['talking'])
e2 = employee ('sonu','staff officer','finance',70000,['management','leadership'])
e3 = employee ('raju', 'HR','management',20000,['managerial skill','confidence'])


e1.info()
e2.info()
e3.info()
e1.do_task("making some sales")
e2.do_task("firing employees")
e3.do_task("of hiring employee and recuruting")

