grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
grade1=grades[0]
grade1_avr= (sum(grade1)/len(grade1))
grade2=grades[1]
grade2_avr= (sum(grade2)/len(grade2))
grade3=grades[2]
grade3_avr= (sum(grade3)/len(grade3))
grade4=grades[3]
grade4_avr= (sum(grade4)/len(grade4))
grade5=grades[4]
grade5_avr= (sum(grade5)/len(grade5))
students_list= list(students)
students_list_sort= students_list.sort()
student1=students_list[0]
student2=students_list[1]
student3=students_list[2]
student4=students_list[3]
student5=students_list[4]
dict={student1:grade1_avr,student2:grade2_avr,student3:grade3_avr,student4:grade4_avr,student5:grade5_avr}
print(dict)

