class Servant:

    def __init__(self, hours_for_work, work_list, salary, bonus=0):
        self.hours_for_work = hours_for_work
        self.work_list = work_list
        self.salary = salary
        self.bonus = bonus

    def stop_working(self):
        self.hours_for_work = 0

    def do_work(self):
        h = -1
        for work in self.work_list:
            if self.hours_for_work - self.work_list[work] > 0:
                self.hours_for_work -= self.work_list[work]
                h *= -1
                break
        if h == -1:
            print("Stop")
            self.hours_for_work = 0


class Sys_admin(Servant):
    def __init__(self, hours_for_work, work_list, salary=1, bonus=0, feeling=0):
        super().__init__(hours_for_work, work_list, salary * 1.3)
        self.bonus = bonus
        self.feeling = feeling

    def do_something(self, Servant_n):
        if self.feeling > 50:
            print("GJ")
            Servant_n.hours_for_work -= 1
        elif self.feeling < -50:
            print("Work better")
            Servant_n.bonus -= 1


class Manager(Sys_admin):
    def __init__(self, work_list, hours_for_work=2, salary=1, feeling=1):
        super().__init__(hours_for_work=hours_for_work // 2, work_list=work_list, salary=salary)
        self.salary = salary * 1.6
        self.feeling = feeling

    def create_difficulties(self, Sys, Servant_n, f):
        Sys.feeling -= f
        Sys.do_something(Servant_n)
