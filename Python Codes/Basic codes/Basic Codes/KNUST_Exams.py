Index_Number = ['10021007', '10021107', '10021207', '10021307', '10021407', '10021507', '10021607', '10021707', '10021807', '10021907', '10022007', '10022107', '10022207', '10022307','10022407']
mid_sem = [65, 48, 22, 32, 80, 12, 45, 25, 33, 67, 23, 45, 56, 34, 81]
exams = [78, 54, 90, 32, 66, 60, 48, 65, 45, 56, 33, 45, 67, 90, 67]
grade = []
Final_Score = []
for values in range(0,15,1):
    mid_sem[values]=(mid_sem[values]/100)*30   
    exams[values]=(exams[values]/100)*70
    Final_Score.append(mid_sem[values] + exams[values])
for values in Final_Score:
    if values >= 70:
        grade.append('A')
    elif values >= 60:
        grade.append('B')
    elif values >= 50:
        grade.append('C')
    elif values >= 40:
        grade.append('D')
    elif values >= 30:
        grade.append('E')
    else:
         grade.append('F')
print('Index Number\tFinal score\tGrade')
for values in range(1,15,1):
    print(str(Index_Number[values]) + '\t' + str(Final_Score[values]) + '\t\t' + str(grade[values]))
                                                    
                                           

                                           

                                         

                                         
                                                                                

                                                                                
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      