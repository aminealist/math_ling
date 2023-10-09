from Monopoly import Servant, Sys_admin, Manager

CPP_enjoyer = Servant(8, {"Do_nothing": 1, "Report": 2, "Make_great_code": 7}, 11)
sys1 = Sys_admin(6, {"Do_nothing": 1, "Report": 3, "Calculating": 4}, feeling=60)
m1 = Manager({"Do_nothing": 1}, feeling=40)


sys1.do_something(CPP_enjoyer)
print(CPP_enjoyer.h_for_work, CPP_enjoyer.bonus, "\n")

m1.create_difficulties(sys1, CPP_enjoyer, 200)
print(CPP_enjoyer.h_for_work, CPP_enjoyer.bonus)