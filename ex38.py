paraula_1 = input("Introdueix una paraula: ")
paraula_2 = input("Introdueix una altre paraula: ")

ultims_3_paraula_1 = paraula_1[-3:]
ultims_3_paraula_2 = paraula_2[-3:]


ultims_2_paraula_1 = paraula_1[-2:]
ultims_2_paraula_2 = paraula_2[-2:]

if ultims_3_paraula_1 == ultims_3_paraula_2:
    print("Rimen molt!")
elif ultims_2_paraula_1 == ultims_2_paraula_2:
    print("Rimen poc")
else:
    print("No rimen")
