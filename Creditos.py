import tkinter as tk
from tkinter import messagebox, font

creditos_por_carrera = {
    "Ingeniería de sistemas": 151,
    "Medicina": 302,
    "Artes Audiovisuales": 147,
    "Ingeniería mecatronica": 154,
    "Ingenieria biomedica": 153,
    "Derecho": 175,
}

def calcular_creditos():
    carrera = entry_carrera.get()
    creditos_actuales = entry_creditos.get()

    try:
        creditos_actuales = int(creditos_actuales)
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa un número válido de créditos.")
        return
    
    if carrera not in creditos_por_carrera:
        messagebox.showerror("Error", "Carrera no reconocida. Por favor, verifica la ortografía.")
        return

    creditos_necesarios = creditos_por_carrera[carrera]
    creditos_faltantes = creditos_necesarios - creditos_actuales

    if creditos_faltantes > 0:
        mensaje = f"Te faltan {creditos_faltantes} créditos para completar {carrera}."
    else:
        mensaje = f"¡Felicidades! Has completado todos los créditos requeridos para {carrera}."

    messagebox.showinfo("Resultado", mensaje)


ventana = tk.Tk()
ventana.title("Créditos Universitarios")


bg_frame = tk.Frame(ventana)
bg_frame.pack(fill=tk.BOTH, expand=True)


bg_color1 = "#000000"
bg_color2 = "#FF0000"
bg_frame.config(bg=bg_color1)


label_titulo = tk.Label(bg_frame, text="Créditos Universitarios", bg=bg_color1, fg="#fff", font=font.Font(family="Helvetica", size=16, weight="bold"))
label_titulo.pack(pady=20)


label_carrera = tk.Label(bg_frame, text="Ingresa tu carrera:", bg=bg_color1, fg="#fff", font=font.Font(family="Helvetica", size=12))
label_carrera.pack(pady=5)

entry_carrera = tk.Entry(bg_frame, font=font.Font(family="Helvetica", size=12), width=30)
entry_carrera.pack(pady=5)


label_creditos = tk.Label(bg_frame, text="Créditos que tienes hasta ahora:", bg=bg_color1, fg="#fff", font=font.Font(family="Helvetica", size=12))
label_creditos.pack(pady=5)

entry_creditos = tk.Entry(bg_frame, font=font.Font(family="Helvetica", size=12), width=30)
entry_creditos.pack(pady=5)


boton_calcular = tk.Button(bg_frame, text="Calcular Créditos Faltantes", command=calcular_creditos, bg="#FF0000", fg="white", font=font.Font(family="Helvetica", size=12, weight="bold"), padx=10, pady=5)
boton_calcular.pack(pady=20)


frame_adorn = tk.Frame(bg_frame, bg="#fff")
frame_adorn.pack(pady=10, padx=10)
frame_adorn.config(bd=2, relief="groove")


ventana.mainloop()
