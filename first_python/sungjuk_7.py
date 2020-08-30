from sungjuk_6 import Sungjuk

def f_menu():
    print(" *** 메뉴 ***")
    print("1. 성적정보 입력")
    print("2. 성적정보 출력")
    print("3. 성적정보 조회")
    print("4. 성적정보 수정")
    print("5. 성적정보 삭제")
    print("6. 프로그램 종료")
     
def f_input():
    obj = Sungjuk()
    
    print()
    if obj.input_sungjuk(students):
        print("\n이미 등록된 학번입니다.\n")
        return

    obj.process_sungjuk()
                
    students.append(obj)
    print("\n성적정보 입력 성공!!\n")

def f_output():
    total_avg = 0
    if len(students) == 0:
        print("\n출력할 데이터가 없습니다!!!\n")
        return
            
    print("\n                      *** 성적표 ***")
    print("============================================================")
    print("학번    이름    국어    영어    수학    총점    평균     등급")
    print("============================================================")
    for obj in students:
        total_avg += obj.avg
        obj.output_sungjuk()           
    print("============================================================")
    print("            총학생수 = %d,  전체 평균 = %.2f\n" % (len(students), total_avg / len(students)))

def f_search():
    hakbun = input("\n조회할 학번을 입력하세요 : ")
    for obj in students:
        if (obj.hakbun == hakbun):
            print("\n학번    이름    국어    영어    수학    총점    평균     등급")
            print("============================================================")
            obj.output_sungjuk() 
            print("============================================================\n")
            break
    else:
        print("\n조회할 학번 %s가 없습니다!!\n" % hakbun)    

def f_update():
    hakbun = input("\n수정할 학번을 입력하세요 : ")
    for obj in students:
        if (obj.hakbun == hakbun):
            obj.kor = int(input("국어점수를 입력하세요 : "))
            obj.eng = int(input("영어점수를 입력하세요 : "))
            obj.math = int(input("수학점수를 입력하세요 : "))
            obj.process_sungjuk()
        print("\n학번 %s 성적정보 수정 성공!!\n" % obj.hakbun)
        break
    else:
        print("\n수정할 제품코드 %s가 없습니다!!\n" % hakbun)

def f_delete():
    hakbun = input("\n삭제할 학번을 입력하세요 : ")
    for obj in students:
        if (obj.hakbun == hakbun):
            students.remove(obj)
            print("\n학번 %s 성적정보 삭제 성공!!\n" % obj.hakbun)
            break
    else:
        print("\n삭제할 제품코드 %s가 없습니다!!\n" % hakbun)        

if __name__ == "__main__":
    students = []
    while True:
        f_menu()
        
        menu = int(input("\n메뉴를 선택하세요 : "))
        
        if menu == 1:
            f_input()
        elif menu == 2:
            f_output()
        elif menu == 3:
            f_search()        
        elif menu == 4:
            f_update()        
        elif menu == 5:
            f_delete()        
        elif menu == 6:
            print("\n프로그램 종료...")
            break;
        else:
            print("\n메뉴를 다시 입력하세요!!!\n")