"""
Dynamic Application Generator. Accept user inputs for their name,class,section,roll no , teacher's name and reason . By this information you have to generate a application of leave. 
"""

nameofthestudent=input("Enter The Name of the Student: ")
classofstudent=input("Enter the Class of student: ")
section=input("Section: ")
rollnum=input("Roll Number: ")
teachername=input("Teachers Name: ")
reason=input("Reason For Leave: ")

application=f"""
To,
{teachername}

                    Subject:- Leave Application

I am {nameofthestudent} of {classofstudent} section {section} wants leave because {reason} please grant me leave otherwise i dont care actually.

Thamking you,
Yours Sincerly
{nameofthestudent}
Rockstar

"""
print(application)
