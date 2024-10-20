import tkinter as tk
import requests
import webbrowser
from tkinter import messagebox, font, Menu
from key import VIRUS_TOTAL

# Función para verificar el enlace usando la API de VirusTotal
def check_link(link):
    API_KEY = VIRUS_TOTAL 
    url = 'https://www.virustotal.com/vtapi/v2/url/report'
    params = {'apikey': API_KEY, 'resource': link}
    
    try:
        response = requests.get(url, params=params)
        result = response.json()

        if result['response_code'] == 1:
            if result['positives'] > 0:
                recommendations = (
                    f"El enlace es sospechoso: {result['positives']} análisis positivos.\n\n"
                    "Recomendaciones:\n"
                    "- No hagas clic en el enlace.\n"
                    "- No ingreses ninguna información personal.\n"
                    "- Si has ingresado información, cambia tus contraseñas inmediatamente.\n"
                    "- Utiliza un antivirus actualizado para realizar un análisis de tu sistema.\n"
                    "- Considera crear una cuenta en Proton VPN para mayor seguridad."
                )
                result_label.config(state=tk.NORMAL)
                result_label.delete(1.0, tk.END)
                result_label.insert(tk.END, recommendations)
                result_label.config(state=tk.DISABLED)
                proton_button.pack(pady=10)
            else:
                result_label.config(state=tk.NORMAL)
                result_label.delete(1.0, tk.END)
                result_label.insert(tk.END, "El enlace es seguro.")
                result_label.config(state=tk.DISABLED)
                proton_button.pack_forget()
        else:
            result_label.config(state=tk.NORMAL)
            result_label.delete(1.0, tk.END)
            result_label.insert(tk.END, "No se pudo analizar el enlace. Inténtelo más tarde.")
            result_label.config(state=tk.DISABLED)
            proton_button.pack_forget()
    except requests.RequestException as e:
        messagebox.showerror("Error", f"Error al conectar con VirusTotal: {e}")

# Función para abrir el enlace de Proton VPN
def open_proton_vpn():
    webbrowser.open("https://protonvpn.com/free-vpn/")

# Función para abrir la página del desarrollador
def open_developer_page():
    webbrowser.open("https://www.pentestercr.com/about_me/")

# Función para verificar el enlace desde la interfaz gráfica
def check_link_gui():
    link = entry_link.get()
    if link:
        check_link(link)
    else:
        messagebox.showwarning("Advertencia", "Por favor, ingrese un enlace válido.")

# Función para pegar desde el menú contextual
def paste(event=None):
    try:
        entry_link.insert(tk.END, root.clipboard_get())
    except:
        pass

# Crear la ventana principal
root = tk.Tk()
root.title("Verificador de Seguridad de Enlaces")
root.geometry("800x700")
root.config(bg="#f0f0f0")

# Cambiar el icono de la ventana
icon_path = r'C:\Users\s4mma\Desktop\VPN\link_valid\icon.ico'  # Asegúrate de que sea la ruta correcta
root.iconbitmap(icon_path)

# Definir estilos de fuente
title_font = font.Font(family='Helvetica', size=24, weight='bold')
label_font = font.Font(family='Helvetica', size=16)
button_font = font.Font(family='Helvetica', size=18)

# Título de la aplicación
title_label = tk.Label(root, text="Verificador de Enlaces", font=title_font, fg="#3ABEF9", bg="#f0f0f0")
title_label.pack(pady=20)

# Texto explicativo para la verificación de enlaces
label = tk.Label(root, text="Ingrese el enlace para verificar su seguridad:", font=label_font, bg="#f0f0f0", fg="#070F2B")
label.pack(pady=10)

# Campo de entrada para el enlace
entry_link = tk.Entry(root, width=40, font=label_font, bg="white", borderwidth=2, relief="groove")
entry_link.pack(pady=5)

# Menú contextual (click derecho)
menu = Menu(root, tearoff=0)
menu.add_command(label="Pegar", command=paste)

def show_context_menu(event):
    menu.post(event.x_root, event.y_root)

entry_link.bind("<Button-3>", show_context_menu)

# Botón para verificar el enlace
button_check_link = tk.Button(root, text="Verificar Enlace", font=button_font, bg="#7ECA9C", fg="white", command=check_link_gui, relief="raised", bd=3)
button_check_link.pack(pady=20)

# Etiqueta para mostrar el resultado y recomendaciones
result_label = tk.Text(root, height=10, width=60, font=label_font, bg="white", wrap=tk.WORD, borderwidth=2, relief="groove")
result_label.pack(pady=10)
result_label.config(state=tk.DISABLED)

# Botón para crear cuenta en Proton VPN
proton_button = tk.Button(root, text="Crear cuenta en Proton VPN", font=button_font, bg="#8758FF", fg="white", command=open_proton_vpn, relief="raised", bd=3)
proton_button.pack_forget()

# Botón para abrir la página del desarrollador
developer_button = tk.Button(root, text="Visitar página del desarrollador", font=button_font, bg="#7BC9FF", fg="white", command=open_developer_page, relief="raised", bd=3)
developer_button.pack(pady=10)

# Ejecutar la interfaz gráfica
root.mainloop()