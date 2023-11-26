import PySimpleGUI as sg
import random

class NumberGame:
    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.min_value, self.max_value = self.get_difficulty_range(self.difficulty)
        self.secret_number = self.generate_new_secret_number(self.min_value, self.max_value)

    def generate_new_secret_number(self, min_value, max_value):
        return random.randint(min_value, max_value)

    def get_difficulty_range(self, difficulty):
        if difficulty == "Легкий":
            return 1, 50
        elif difficulty == "Середній":
            return 1, 100
        elif difficulty == "Важкий":
            return 1, 200
        else:
            raise ValueError("Непідтримуваний рівень складності")

    def play(self):
        layout = [
            [sg.Text("Виберіть рівень складності:"), sg.Combo(["Легкий", "Середній", "Важкий"], default_value=self.difficulty, key="difficulty")],
            [sg.Button("Почати нову гру")],
            [sg.Text("Вгадайте число:"), sg.InputText(key="input_guess"), sg.Button("Вгадати")],
            [sg.Text("", size=(30, 1), key="output_message")]
        ]

        window = sg.Window("Гра 'Вгадай число'", layout, finalize=True)

        while True:
            event, values = window.read()

            if event == sg.WIN_CLOSED:
                break

            if event == "Почати нову гру":
                self.difficulty = values["difficulty"]
                self.min_value, self.max_value = self.get_difficulty_range(self.difficulty)
                self.secret_number = self.generate_new_secret_number(self.min_value, self.max_value)
                window["output_message"].update("")
                continue

            if event == "Вгадати":
                self.handle_guess(window, values)

        window.close()

    def handle_guess(self, window, values):
        try:
            user_guess = int(values["input_guess"])
        except ValueError:
            window["output_message"].update("Введіть коректне число.")
            return

        if self.min_value <= user_guess <= self.max_value:
            window["output_message"].update("")
            self.check_guess(window, user_guess)
        else:
            window["output_message"].update(f"Введене число має бути в діапазоні від {self.min_value} до {self.max_value}.")

    def check_guess(self, window, user_guess):
        if user_guess < self.secret_number:
            window["output_message"].update("Загадане число більше. Спробуйте ще раз.")
        elif user_guess > self.secret_number:
            window["output_message"].update("Загадане число менше. Спробуйте ще раз.")
        else:
            sg.popup_ok(f"Вітаємо! Ви вгадали число {self.secret_number}.")

if __name__ == "__main__":
    game = NumberGame("Середній")
    game.play()
