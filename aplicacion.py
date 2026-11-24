import tkinter as tk
from datetime import datetime

conectado = False


def actualizar_reloj():
    ahora = datetime.now().strftime("%H:%M:%S")
    lbl_reloj.config(text=f"⏱ {ahora}")
    ventana.after(1000, actualizar_reloj)


def ejecutar_comando(event=None):
    global conectado
    dato = entrada.get().strip()
    rol = var_rol.get()

    if dato:
        conectado = True
        hora = datetime.now().strftime("%H:%M")
        lbl_estado.config(text=f"◈ ENLACE ACTIVO // {dato.upper()} [{rol}]", fg="#00f5d4")
        lbl_log.config(text=f"Último acceso: {dato.upper()} ({rol}) a las {hora}", fg="#94a3b8")
        panel.config(highlightbackground="#00f5d4")
        btn_accion.config(text="✔ CONECTADO", bg="#00f5d4", fg="#090d16", highlightbackground="#00f5d4")
    else:
        conectado = False
        lbl_estado.config(text="▲ ALERTA: INTRODUCE UN IDENTIFICADOR", fg="#ff2a85")
        panel.config(highlightbackground="#ff2a85")


def reiniciar(event=None):
    global conectado
    conectado = False
    entrada.delete(0, tk.END)
    lbl_estado.config(text="◇ SISTEMA EN ESPERA DE DATOS...", fg="#64748b")
    panel.config(highlightbackground="#38bdf8")
    btn_accion.config(text="INICIAR ENLACE", bg="#090d16", fg="#38bdf8", highlightbackground="#38bdf8")
    entrada.focus()


def hover_accion(entrando):
    if conectado:
        return
    if entrando:
        btn_accion.config(bg="#38bdf8", fg="#090d16")
    else:
        btn_accion.config(bg="#090d16", fg="#38bdf8")


# --- VENTANA PRINCIPAL ---
ventana = tk.Tk()
ventana.title("DESIN TEMA 4 // Katya Thais Vargas Piñera")
ventana.geometry("540x430")
ventana.resizable(False, False)
ventana.configure(bg="#090d16")
ventana.bind("<Escape>", reiniciar)

# --- TARJETA PRINCIPAL CON BORDE NEÓN ---
panel = tk.Frame(
    ventana,
    bg="#111827",
    highlightbackground="#38bdf8",
    highlightthickness=2,
    padx=28,
    pady=22
)
panel.pack(expand=True, fill="both", padx=22, pady=20)

# Barra superior HUD (Módulo, Reloj y Estado)
barra_top = tk.Frame(panel, bg="#111827")
barra_top.pack(fill="x", pady=(0, 12))

tk.Label(
    barra_top,
    text="DESIN  //  TEMA 4",
    font=("Consolas", 13, "bold"),
    bg="#111827",
    fg="#38bdf8"
).pack(side="left")

lbl_reloj = tk.Label(
    barra_top,
    text="⏱ 00:00:00",
    font=("Consolas", 9, "bold"),
    bg="#1e293b",
    fg="#00f5d4",
    padx=8,
    pady=3
)
lbl_reloj.pack(side="right")

# Línea separadora luminosa
tk.Frame(panel, bg="#1e293b", height=2).pack(fill="x", pady=(0, 14))

# Selector de Nivel de Acceso (Radiobuttons estilizados)
tk.Label(
    panel,
    text="> NIVEL DE ACCESO:",
    font=("Consolas", 9, "bold"),
    bg="#111827",
    fg="#94a3b8"
).pack(anchor="w")

marco_roles = tk.Frame(panel, bg="#111827")
marco_roles.pack(fill="x", pady=(4, 14))

var_rol = tk.StringVar(value="ALUMNA")
for texto_rol in ("ALUMNA", "DOCENTE", "ADMIN"):
    tk.Radiobutton(
        marco_roles,
        text=texto_rol,
        variable=var_rol,
        value=texto_rol,
        font=("Consolas", 9, "bold"),
        bg="#111827",
        fg="#cbd5e1",
        selectcolor="#090d16",
        activebackground="#111827",
        activeforeground="#00f5d4",
        cursor="hand2"
    ).pack(side="left", padx=(0, 18))

# Campo de Identificación
tk.Label(
    panel,
    text="> IDENTIFICACIÓN DEL USUARIO:",
    font=("Consolas", 10, "bold"),
    bg="#111827",
    fg="#cbd5e1"
).pack(anchor="w")

entrada = tk.Entry(
    panel,
    font=("Consolas", 12),
    bg="#090d16",
    fg="#ffffff",
    insertbackground="#00f5d4",
    bd=0,
    highlightthickness=1,
    highlightbackground="#334155",
    highlightcolor="#00f5d4"
)
entrada.pack(fill="x", ipady=8, pady=(6, 18))
entrada.focus()
entrada.bind("<Return>", ejecutar_comando)

# Contenedor de botones
marco_botones = tk.Frame(panel, bg="#111827")
marco_botones.pack(fill="x")

btn_accion = tk.Button(
    marco_botones,
    text="INICIAR ENLACE",
    font=("Consolas", 10, "bold"),
    bg="#090d16",
    fg="#38bdf8",
    activebackground="#38bdf8",
    activeforeground="#090d16",
    bd=0,
    highlightthickness=1,
    highlightbackground="#38bdf8",
    cursor="hand2",
    pady=8,
    command=ejecutar_comando
)
btn_accion.pack(side="left", expand=True, fill="x", padx=(0, 6))

btn_reset = tk.Button(
    marco_botones,
    text="REINICIAR [ESC]",
    font=("Consolas", 10, "bold"),
    bg="#090d16",
    fg="#94a3b8",
    activebackground="#ff2a85",
    activeforeground="#ffffff",
    bd=0,
    highlightthickness=1,
    highlightbackground="#334155",
    cursor="hand2",
    pady=8,
    command=reiniciar
)
btn_reset.pack(side="right", expand=True, fill="x", padx=(6, 0))

# Efectos Hover
btn_accion.bind("<Enter>", lambda e: hover_accion(True))
btn_accion.bind("<Leave>", lambda e: hover_accion(False))
btn_reset.bind("<Enter>", lambda e: btn_reset.config(bg="#ff2a85", fg="#ffffff", highlightbackground="#ff2a85"))
btn_reset.bind("<Leave>", lambda e: btn_reset.config(bg="#090d16", fg="#94a3b8", highlightbackground="#334155"))

# Estado del sistema y registro
lbl_estado = tk.Label(
    panel,
    text="◇ SISTEMA EN ESPERA DE DATOS...",
    font=("Consolas", 9, "bold"),
    bg="#111827",
    fg="#64748b"
)
lbl_estado.pack(anchor="w", pady=(16, 2))

lbl_log = tk.Label(
    panel,
    text="Sin actividad reciente en esta sesión.",
    font=("Consolas", 8),
    bg="#111827",
    fg="#475569"
)
lbl_log.pack(anchor="w", pady=(0, 12))

# Pie de página con Autoría
tk.Frame(panel, bg="#1e293b", height=1).pack(fill="x", pady=(0, 8))

tk.Label(
    panel,
    text="AUTORA: KATYA THAIS VARGAS PIÑERA",
    font=("Consolas", 8, "bold"),
    bg="#111827",
    fg="#38bdf8"
).pack(anchor="e")

actualizar_reloj()
ventana.mainloop()
