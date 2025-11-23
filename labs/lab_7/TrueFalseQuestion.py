# TrueFalseQuestion.py
from Question import Question

class TrueFalseQuestion(Question):
      def __init__(self, question, answer, score, incorrectPoints): #INCORRECTPOINTS yeni. annede yok.
            super().__init__(question, answer, score)
            self.__incorrectPoints = int(incorrectPoints)

      def getScore(self):
            #bir tane isCorrectAnswer var. o da anneden. compilerın şaşırması için hiçbir neden yok. SUPER diye belirtmemize gerek yok.
            if self.isCorrectAnswer():
                  return super().getScore()
            return -self.__incorrectPoints #neden - koyduk ki???? else altına yazmak zorunda mıyız

      def displayQuestion(self):
            print("True or False:")
            super().displayQuestion() 
            #bir de çocuğa method yazdık. ama annede olanı kullanmak istiyoruz.