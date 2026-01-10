# Question.py

class Question:
      
      #we ndeed to use self when we use them as damla.getScore()
      #__ means to access private data members.
      
      def __init__(self, question, answer, score):
            self.__questionText = question
            self.__correctAnswer = answer
            self.__score = score
            self.__studentAnswer = None
            
      def getQuestion(self):
            return self.__questionText

      def getScore(self):
            if self.isCorrectAnswer():
                  return int(self.__score)
            return 0

      def getPoints(self):
            return int(self.__score)

      def getCorrectAnswer(self):
            return self.__correctAnswer

      def setQuestion(self, question):
            self.__questionText = question

      def setAnswer(self, answer):
            self.__correctAnswer = answer   
            
      def setScore(self, score):
            self.__score = int(score)
            
      def answerQuestion(self, stuAnswer):
            self.__studentAnswer = stuAnswer

      def isCorrectAnswer(self):
            if self.__studentAnswer == self.__correctAnswer:
                  return True
            return False

      def displayQuestion(self):
            print(self.getQuestion())

      def __str__(self):
            return self.__questionText+'\nYour Answer:'+str(self.__studentAnswer)+'\nCorrect Answer:'+self.__correctAnswer