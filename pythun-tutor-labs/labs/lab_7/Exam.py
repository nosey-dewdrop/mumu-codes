# Exam.py
from Question import Question
from MultipleChoiceQuestion import MultipleChoiceQuestion
from TrueFalseQuestion import TrueFalseQuestion

def initializeQuestions(fileName, questionsList):
    """
    Dosyadan soruları okuyup uygun nesneleri oluşturur ve listeye ekler.
    [cite: 50-54]
    """
    try:
        with open(fileName, 'r') as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                
                parts = line.split(';')
                if len(parts) < 4:
                    continue

                qType = parts[0].strip()
                qText = parts[1].strip()
                qAnswer = parts[2].strip()
                qScore = parts[3].strip()

                if qType == 'M': # Multiple Choice
                    choices = parts[4].strip().split(',')
                    # Şıkların başındaki sonundaki boşlukları temizleyelim
                    choices = [c.strip() for c in choices]
                    q = MultipleChoiceQuestion(qText, qAnswer, qScore, choices)
                    questionsList.append(q)
                
                elif qType == 'T': # True False
                    incorrectPoints = parts[4].strip()
                    q = TrueFalseQuestion(qText, qAnswer, qScore, incorrectPoints)
                    questionsList.append(q)
                
                elif qType == 'R': # Regular Question
                    q = Question(qText, qAnswer, qScore)
                    questionsList.append(q)

    except FileNotFoundError:
        print(f"Error: File {fileName} not found.")

def gradeExam(questionsList):
    """
    Sınavı puanlar, yanlışları gösterir ve toplam sonucu döner.
    [cite: 55-61]
    """
    print("\n***********Grading Exam*****************")
    total_score = 0
    
    for q in questionsList:
        score = q.getScore()
        total_score += score
        
        # Sadece yanlış cevapları yazdır [cite: 59]
        if not q.isCorrectAnswer():
            print("Incorrect Answer")
            print(q.getQuestion()) # Soru metni
            # Question sınıfındaki __str__ yapısına erişip parse edebiliriz 
            # ya da doğrudan getterları kullanabiliriz. 
            # Föydeki sample run çıktısına [cite: 116-117] uyması için:
            # Ancak Question.py içindeki __str__ zaten bu formatı veriyor.
            # Fakat __str__ tüm yapıyı döndüğü için burada manuel yazdırıyoruz:
            # Lab Guide sample run [cite: 116] formatı:
            # Your Answer: ...
            # Correct Answer: ...
            
            # Not: Question.py'da studentAnswer private (__studentAnswer).
            # Getter olmadığı için __str__ üzerinden gitmek veya Question.py'ı editlemek gerekir.
            # Ancak ben size verilen Question.py'ı değiştirmeden __str__ çıktısını kullanacağım.
            # Question.__str__ zaten bu formatta dönüyor[cite: 27].
            print(str(q).split('\n', 1)[1]) # Soruyu tekrar yazmamak için split ediyoruz
            
    print("*****************END OF GRADING*****************")
    return total_score

def main():
    questions = []
    # Soruları dosyadan oku
    initializeQuestions("questions.txt", questions)
    
    # Sınavı uygula [cite: 64]
    for q in questions:
        q.displayQuestion()
        stu_ans = input("Enter choice: ")
        q.answerQuestion(stu_ans.strip()) # Boşlukları temizle
        
    # Notlandır ve sonucu yazdır [cite: 66]
    final_score = gradeExam(questions)
    print(f"Your score is: {final_score}")

if __name__ == "__main__":
    main()