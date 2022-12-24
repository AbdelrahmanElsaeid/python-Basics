# __init__  called Automatically


class Skill:
    def __init__(self):

        self.skills = ["python","MySql","Django"]
    def __str__(self):
        return f"My Skills -----> {self.skills}"



pro = Skill()
print(pro)
#    >>>>>>>>>>>>>>  My Skills -----> ['python', 'MySql', 'Django']
print(len(pro))
#    >>>>>>>>>>>>>>  TypeError: object of type 'Skill' has no len()


class Skill2:
    def __init__(self):

        self.skills = ["python","MySql","Django"]
    def __str__(self):
        return f"My Skills -----> {self.skills}"
    def __len__(self):
        return len(self.skills)


pro2= Skill2()
print(pro2)
#    >>>>>>>>>>>>>>  My Skills -----> ['python', 'MySql', 'Django']
print(len(pro2))
#    >>>>>>>>>>>>>>    3
