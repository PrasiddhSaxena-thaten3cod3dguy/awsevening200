def ctccalc(basicsal,hra,ent,fuel,lazy,internet):
    HRA=basicsal * hra
    ENT=basicsal * ent
    FUEL= basicsal * fuel
    LAZY=basicsal * lazy
    INTERNET=basicsal * internet
    CTC=basicsal + HRA + ENT + FUEL + LAZY + INTERNET 
    return CTC

basicsalary=int(input("Enter  the Basic Salary: "))

if basicsalary >= 100000:
    ctc=ctccalc(basicsalary, 0.15, 0.20, 0.12, 0.35, 0.55)
elif basicsalary >=60000:
    ctc=ctccalc(basicsalary, 0.20, 0.15, 0.10, 0.25, 0.35)
elif basicsalary >= 40000:
    ctc=ctccalc(basicsalary, 0.25, 0.10, 0.05, 0.20, 0.30)
else:
    ctc=0

print(ctc)