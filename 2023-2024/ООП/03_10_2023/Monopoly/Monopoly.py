class Servant:

    def __init__(self, h_f_w, w_l, salary, bonus=0):
        self.h_for_work = h_f_w
        self.work_list = w_l
        self.salary = salary
        self.bonus = bonus

    def stop_working(self):
        self.h_for_work = 0

    def do_work(self):
        h = -1
        for work in self.work_list:
            if self.h_for_work - self.work_list[work] > 0:
                self.h_for_work -= self.work_list[work]
                h *= -1
                break
        if h == -1:
            print("Stop")
            self.h_for_work = 0


class Sys_admin(Servant):
    def __init__(self, h_f_w, w_l, salary=1, bonus=0, feeling=0):
        super().__init__(h_f_w, w_l, salary * 1.3)
        self.bonus = bonus
        self.feeling = feeling

    def do_something(self, Serv):
        if self.feeling > 50:
            print("GJ")
            Serv.h_for_work -= 1
        elif self.feeling < -50:
            print("Work better")
            Serv.bonus -= 1


class Manager(Sys_admin):
    def __init__(self, w_l, h_f_w=2, salary=1, feeling=1):
        super().__init__(h_f_w=h_f_w // 2, w_l=w_l, salary=salary)
        self.salary = salary * 1.6
        self.feeling = feeling

    def create_difficulties(self, Sys, Serv, f):
        Sys.feeling -= f