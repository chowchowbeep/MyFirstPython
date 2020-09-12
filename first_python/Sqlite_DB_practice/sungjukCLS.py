# -*- coding:utf-8 -*-

class Sungjuk:
    def __init__(self):
        self._hakbun = None
        self._irum = None
        self._kor = 0
        self._eng = 0
        self._math = 0
        self._tot = 0
        self._avg = 0.0
        self._grade = None
        
    def get_hakbun(self):
        return self._hakbun

    def set_hakbun(self, hakbun):
        self._hakbun = hakbun
    
    hakbun = property(get_hakbun, set_hakbun)
    
    def get_irum(self):
        return self._irum
    
    def set_irum(self, irum):
        self._irum = irum
    
    irum = property(get_irum, set_irum)
    
    def get_kor(self):
        return self._kor
    
    def set_kor(self, kor):
        self._kor = kor
    
    kor = property(get_kor, set_kor)
    
    def get_eng(self):
        return self._eng
    
    def set_eng(self, eng):
        self._eng = eng
    
    eng = property(get_eng, set_eng)
    
    def get_math(self):
        return self._math
    
    def set_math(self, math):
        self._math = math
    
    math = property(get_math, set_math)
    
    def get_tot(self):
        return self._tot
    
    def set_tot(self, tot):
        self._tot = tot
    
    tot = property(get_tot, set_tot)
    
    def get_avg(self):
        return self._avg
    
    def set_avg(self, avg):
        self._avg = avg
    
    avg = property(get_avg, set_avg)
    
    def get_grade(self):
        return self._grade
    
    def set_grade(self, grade):
        self._grade = grade
    
    grade = property(get_grade, set_grade)
    
    def input_sungjuk(self):
        self._hakbun = input("학번을 입력하세요 : ")
        self._irum = input("이름을 입력하세요 : ")
        self._kor = int(input("국어점수를 입력하세요 : "))
        self._eng = int(input("영어점수를 입력하세요 : "))
        self._math = int(input("수학점수를 입력하세요 : "))
    
    def process_sungjuk(self):
        self._tot = self._kor + self._eng + self._math
        self._avg = self._tot / 3
        if self._avg >= 90:
            self._grade = "수"
        elif self._avg >= 80:
            self._grade = "우"
        elif self._avg >= 70:
            self._grade = "미"
        elif self._avg >= 60:
            self._grade = "양"
        else:
            self._grade = "가" 
    
    def output_sungjuk(self):
        print("%4s  %4s   %3d     %3d     %3d     %3d   %6.2f     %s"
            % (self._hakbun, self._irum, self._kor, self._eng, self._math, 
               self._tot, self._avg, self._grade))