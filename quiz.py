import random

class Question:
    def __init__(self, prompt, options, correct_option):
        self.prompt = prompt
        self.options = options
        self.correct_option = correct_option

def run_quiz(questions):
    score = 0
    random.shuffle(questions)

    for question in questions:
        print(question.prompt)
        for i, option in enumerate(question.options, 1):
            print(f"{i}. {option}")

        user_choice = int(input("Escolha a opção correta (1, 2, 3, ...): ")) - 1

        if user_choice == question.correct_option:
            print("Correto!\n")
            score += 1
        else:
            print(f"Incorreto. A resposta correta era: {question.options[question.correct_option]}\n")

    print(f"Você acertou {score} de {len(questions)} perguntas.")

if __name__ == "__main__":
    # Exemplo de perguntas
    questions = [
        Question("Qual é a capital do Brasil?", ["Rio de Janeiro", "Brasília", "São Paulo"], 1),
        Question("Quem escreveu 'Romeu e Julieta'?", ["Charles Dickens", "Jane Austen", "William Shakespeare"], 2),
        Question("Qual é o maior planeta do nosso sistema solar?", ["Marte", "Júpiter", "Vênus"], 1),
    ]

    run_quiz(questions)
