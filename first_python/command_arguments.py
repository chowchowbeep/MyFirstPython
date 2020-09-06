import sys

if __name__ == "__main__":
    print("명령행 인자의 갯수 : ", len(sys.argv))
    print(sys.argv)
    tot = 0
    for item in range(len(sys.argv)):
        if item == 0:
            continue
        tot += int(sys.argv[item])
    print("tot = ", tot)

#    for item in sys.argv:
#       print(item)





#(venv) C:\Users\cho03\Google 드라이브(chorongaiai@gmail.com)\pythonSource\first_python>python command_arguments.py
#10 20 30
#명령행 인자의 갯수 :  4
#['command_arguments.py', '10', '20', '30']
#command_arguments.py
#10
#20
#30
