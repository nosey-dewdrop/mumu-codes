# MultipleChoiceQuestion.py
from Question import Question

class MultipleChoiceQuestion(Question):
    def __init__(self, question, answer, score, choices): #CHOICES YENI 
        super().__init__(question, answer, score) 
        self.__choices = choices

    def displayQuestion(self):
        super().displayQuestion() 
        for choice in self.__choices:
            print(choice)
    def __str__(self):
        #bu str hiç içiem sinmöedi.
        base_str = super().__str__()
        choices_str = "\n" + "\n".join(self.__choices) #ekleniyor.
        return base_str + choices_str