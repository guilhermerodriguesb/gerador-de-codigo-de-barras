import tkinter as tk
from tkinter import messagebox
from barcode import Code128
from barcode.writer import ImageWriter

def gerar_codigo_barras():
    codigo = entrada_codigo.get()

    # Verifica se o código tem exatamente 6 dígitos
    if len(codigo) != 6 or not codigo.isdigit():
        messagebox.showerror("Erro", "O código deve ter exatamente 6 dígitos numéricos.")
        return

    try:
        # Gera o código de barras no formato Code128 e salva no diretório do projeto
        code128 = Code128(codigo, writer=ImageWriter())
        code128.save(f"codigo_barras_{codigo}")
        messagebox.showinfo("Sucesso", f"Código de barras salvo como codigo_barras_{codigo}.png")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao gerar código de barras: {e}")

# Criação da janela principal
janela = tk.Tk()
janela.title("Gerador de Código de Barras")
janela.geometry("400x200")

# Label e entrada para o código
tk.Label(janela, text="Digite o código (6 dígitos):", font=("Arial", 14)).pack(pady=10)
entrada_codigo = tk.Entry(janela, font=("Arial", 14), justify="center")
entrada_codigo.pack(pady=5)

# Botão para gerar o código de barras
botao_gerar = tk.Button(janela, text="Gerar Código de Barras", font=("Arial", 14), command=gerar_codigo_barras)
botao_gerar.pack(pady=20)

# Inicia a interface gráfica
janela.mainloop()
