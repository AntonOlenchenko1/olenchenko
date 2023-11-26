import PySimpleGUI as sg
import random

def play_guess_the_number(difficulty):
    def generate_new_secret_number(min_value, max_value):
        return random.randint(min_value, max_value)

    def get_difficulty_range(difficulty):
        if difficulty == "Легкий":
            return 1, 50
        elif difficulty == "Середній":
            return 1, 100
        elif difficulty == "Важкий":
            return 1, 200
        else:
            raise ValueError("Непідтримуваний рівень складності")

    layout = [
        [sg.Text("Виберіть рівень складності:"), sg.Combo(["Легкий", "Середній", "Важкий"], default_value=difficulty, key="difficulty")],
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
            difficulty = values["difficulty"]
            min_value, max_value = get_difficulty_range(difficulty)
            secret_number = generate_new_secret_number(min_value, max_value)
            window["output_message"].update("")
            continue

        if event == "Вгадати":
            try:
                user_guess = int(values["input_guess"])
            except ValueError:
                window["output_message"].update("Введіть коректне число.")
                continue

            if min_value <= user_guess <= max_value:
                window["output_message"].update("")
                if user_guess < secret_number:
                    window["output_message"].update("Загадане число більше. Спробуйте ще раз.")
                elif user_guess > secret_number:
                    window["output_message"].update("Загадане число менше. Спробуйте ще раз.")
                else:
                    sg.popup_ok(f"Вітаємо! Ви вгадали число {secret_number}.")
            else:
                window["output_message"].update(f"Введене число має бути в діапазоні від {min_value} до {max_value}.")

    window.close()

if __name__ == "__main__":
    play_guess_the_number("Середній")
