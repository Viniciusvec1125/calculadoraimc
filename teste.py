import tkinter as tk
from tkinter import messagebox

# Funções para calcular o IMC, categoria do IMC, diferença de peso, peso ideal e metabolismo basal
def calculate_bmi(weight, height):
    return weight / (height ** 2)

def calculate_bmi_category(bmi):
    if bmi < 18.5:
        return 'A BAIXO DO PESO'
    elif 18.5 <= bmi < 25:
        return 'NORMAL'
    elif 25 <= bmi < 30:
        return 'SOBREPESO'
    else:
        return 'OBESIDADE'

def weight_difference(category, bmi, height, weight):
    if category == 'A BAIXO DO PESO':
        return (18.5 * height ** 2 - weight, None)
    elif category == 'NORMAL':
        return ("Mantenha o peso", None)
    elif category == 'SOBREPESO':
        return (weight - 24.9 * height ** 2, 30 - bmi)
    elif category == 'OBESIDADE':
        return (weight - 29.9 * height ** 2, None)

def calculate_ideal_weight(height, bmi_category):
    if bmi_category == 'A BAIXO DO PESO':
        return 18.5 * height ** 2
    elif bmi_category == 'NORMAL':
        return "Mantenha o peso"
    elif bmi_category == 'SOBREPESO' or bmi_category == 'OBESIDADE':
        return 24.9 * height ** 2

def calculate_ideal_bmi(height):
    return 22 * (height ** 2)

def calculate_bmr(weight, height, age, gender):
    if gender.lower() == 'masculino':
        bmr = 88.362 + (13.397 * weight) + (4.799 * height * 100) - (5.677 * age)
    elif gender.lower() == 'feminino':
        bmr = 447.593 + (9.247 * weight) + (3.098 * height * 100) - (4.330 * age)
    else:
        raise ValueError("Invalid gender specified. Please enter 'masculino' or 'feminino'.")
    return bmr

# Função para lidar com o clique do botão
def handle_calculate():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())
        age = int(age_entry.get())
        gender = gender_var.get()

        if weight <= 0 or height <= 0 or age <= 0:
            raise ValueError("Peso, altura e idade devem ser números positivos.")

        bmi = calculate_bmi(weight, height)
        bmi_category = calculate_bmi_category(bmi)
        weight_diff, obesidade_diff = weight_difference(bmi_category, bmi, height, weight)
        ideal_weight = calculate_ideal_weight(height, bmi_category)
        ideal_bmi = calculate_ideal_bmi(height)
        bmr = calculate_bmr(weight, height, age, gender)

        if obesidade_diff is not None:
            msg = f"Falta {obesidade_diff:.2f} kg para alcançar a obesidade."
        else:
            msg = ""

        # Mostrar os resultados em uma caixa de mensagem
        messagebox.showinfo("Resultados", f"IMC: {bmi}\nCategoria IMC: {bmi_category}\nDiferença de peso necessária: {weight_diff}\nPeso Ideal: {ideal_weight}\nIMC Ideal: {ideal_bmi}\nMetabolismo Basal: {bmr}\n\n{msg}")
    except ValueError as e:
        messagebox.showerror("Erro", str(e))

# Criar a janela principal
root = tk.Tk()
root.title("Calculadora de Saúde")

# Definir cores
bg_color = "#d4efdf"  # Verde claro para o fundo
label_color = "#404040"  # Cinza escuro para rótulos de texto
button_color = "#4CAF50"  # Verde para botões
button_text_color = "#FFFFFF"  # Texto branco para botões

# Configurar estilo
root.configure(bg=bg_color)

# Criar as entradas e rótulos
tk.Label(root, text="Peso (kg):", bg=bg_color, fg=label_color).grid(row=0, column=0, padx=5, pady=5)
weight_entry = tk.Entry(root)
weight_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Altura (m):", bg=bg_color, fg=label_color).grid(row=1, column=0, padx=5, pady=5)
height_entry = tk.Entry(root)
height_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(root, text="Idade:", bg=bg_color, fg=label_color).grid(row=2, column=0, padx=5, pady=5)
age_entry = tk.Entry(root)
age_entry.grid(row=2, column=1, padx=5, pady=5)

tk.Label(root, text="Gênero:", bg=bg_color, fg=label_color).grid(row=3, column=0, padx=5, pady=5)
gender_var = tk.StringVar(root)
gender_var.set("masculino")
gender_menu = tk.OptionMenu(root, gender_var, "masculino", "feminino")
gender_menu.config(bg=button_color, fg=button_text_color)
gender_menu["menu"].config(bg=button_color, fg=button_text_color)
gender_menu.grid(row=3, column=1, padx=5, pady=5)

# Botão para calcular
calculate_button = tk.Button(root, text="Calcular", command=handle_calculate, bg=button_color, fg=button_text_color)
calculate_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5, sticky="we")

# Iniciar a interface gráfica
root.mainloop()
def weight_difference(category, bmi, height, weight):
    if category == 'A BAIXO DO PESO':
        falta_desnutricao = 16 * height ** 2 - weight
        if falta_desnutricao <= 0:
            falta_desnutricao = "Você está na categoria de desnutrição."
        return (18.5 * height ** 2 - weight, falta_desnutricao)
    elif category == 'NORMAL':
        return ("Mantenha o peso", None)
    elif category == 'SOBREPESO':
        return (weight - 24.9 * height ** 2, 30 - bmi)
    elif category == 'OBESIDADE':
        return (weight - 29.9 * height ** 2, None)
