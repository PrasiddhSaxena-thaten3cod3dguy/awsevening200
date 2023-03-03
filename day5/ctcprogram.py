'''
WAP to find the CTC value

Case1 :-
    if the Basic Salary =   >=40,000
    Then HRA=25%
    Entertanment Bounus = 10%
    Fuel :- 5%
    Internet:- 20%
    LazyAllowance:- 30%
Case2 :-
    if the Basic Salary = >=60,000
    Then HRA=20%
    Entertanment Bounus = 15%
    Fuel :- 10%
    Internet:- 25%
    LazyAllowance:- 35%
Case3 :-
    if the Basic Salary = >=1,00,000
    Then HRA=15%
    Entertanment Bounus = 20%
    Fuel :- 12%
    Internet:- 35%
    LazyAllowance:- 55% 


I/P :- User is going to enter the basic salary.
Rest Calculation to be done by program
    
'''

basicsal=int(input("Enter The Basic Salary: "))
ctc=0
if basicsal >= 100000:
    hra=basicsal * 0.25
    entertainment= basicsal * 0.20
    fuel=basicsal * 0.12
    internet= basicsal * 0.35
    lazy= basicsal * 0.55
    ctc=basicsal + hra + fuel + internet + lazy + entertainment
elif basicsal >= 60000:
    hra=basicsal * 0.15
    entertainment= basicsal * 0.15
    fuel=basicsal * 0.10
    internet= basicsal * 0.25
    lazy= basicsal * 0.35
    ctc=basicsal + hra + fuel + internet + lazy + entertainment
elif basicsal >= 40000:
    hra=basicsal * 0.25
    entertainment= basicsal * 0.10
    fuel=basicsal * 0.10
    internet= basicsal * 0.25
    lazy= basicsal * 0.35
    ctc=basicsal + hra + fuel + internet + lazy + entertainment
else:
    print("Too Low to calculate CTC")

print(ctc)