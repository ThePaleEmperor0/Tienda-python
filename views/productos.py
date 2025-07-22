import tkinter as tk
from services.gb import ejecutar_consulta, ejecutar_modificacion

def cargar_accesorios(v):
    bg = "#0d0d0d"
    fg = "#c0c0c0"
    lbg = "#1a1a1a"
    brd = "#333333"
    hl = "#4d4d4d"

    v.configure(bg=bg)

    p = tk.Frame(v, bg=bg, width=v.winfo_screenwidth(), height=v.winfo_screenheight())
    p.pack(fill="both", expand=True)

    pi = tk.Frame(p, bg=bg, width=v.winfo_screenwidth()//2, highlightbackground=brd, highlightthickness=1)
    pi.pack(side="left", fill="both", expand=True, padx=(0, 10), pady=10)

    ti = tk.Label(pi, text="REGISTRAR PRODUCTO", fg=fg, bg=bg, font=("Helvetica", 20, "bold"), anchor="w")
    ti.pack(padx=40, pady=(30, 20), anchor="w")

    campos = [("Producto:", "ep"), ("Género:", "eg"), ("Descripción:", "ed"), ("Precio:", "epc")]

    for texto, var in campos:
        f = tk.Frame(pi, bg=bg)
        f.pack(padx=40, pady=(0, 15), fill="x")

        l = tk.Label(f, text=texto, fg=fg, bg=bg, font=("Helvetica", 12), anchor="w", width=12)
        l.pack(side="left", padx=(0, 10))

        if texto == "Descripción:":
            e = tk.Text(f, bg=lbg, fg=fg, font=("Helvetica", 12), height=5, width=30, insertbackground=fg, highlightbackground=brd, highlightthickness=1, relief="flat")
        else:
            e = tk.Entry(f, bg=lbg, fg=fg, font=("Helvetica", 12), insertbackground=fg, highlightbackground=brd, highlightthickness=1, relief="flat")

        globals()[var] = e
        e.pack(side="left", fill="x", expand=True)

    def act():
        try:
            base = ejecutar_consulta("SELECT producto FROM accesorios")
            pdb = [r[0] for r in base if r[0]]
        except Exception:
            pdb = []

        txt = "\n".join(f"• {p}" for p in pdb) if pdb else "No hay productos registrados"
        lbl.config(text=txt)

    def reg():
        p = ep.get()
        g = eg.get()
        d = ed.get("1.0", tk.END).strip()
        pc = epc.get()

        if not all([p, g, d, pc]):
            print("Todos los campos son obligatorios")
            return

        try:
            precio = float(pc)
        except ValueError:
            print("El precio debe ser un número válido")
            return

        sql = "INSERT INTO accesorios (producto, genero, descripcion, precio) VALUES (?, ?, ?, ?)"
        ok = ejecutar_modificacion(sql, (p, g, d, precio))
        if ok:
            print("Producto registrado en la base de datos")
        else:
            print("Error al registrar producto")
            return

        ep.delete(0, tk.END)
        eg.delete(0, tk.END)
        ed.delete("1.0", tk.END)
        epc.delete(0, tk.END)

        act()

    b = tk.Button(pi, text="REGISTRAR PRODUCTO", bg=hl, fg=fg, font=("Helvetica", 12, "bold"), relief="flat", command=reg)
    b.pack(padx=40, pady=(20, 0), fill="x")

    pd = tk.Frame(p, bg=bg, highlightbackground=brd, highlightthickness=1)
    pd.pack(side="left", fill="both", expand=True, padx=(10, 0), pady=10)

    td = tk.Label(pd, text="ACCESORIOS DISPONIBLES", fg=fg, bg=bg, font=("Helvetica", 20, "bold"), anchor="w")
    td.pack(padx=40, pady=(30, 10), anchor="w")

    cl = tk.Frame(pd, bg=brd)
    cl.pack(padx=40, pady=10, fill="both", expand=True)

    lbl = tk.Label(cl, text="Cargando productos...", fg=fg, bg=lbg, font=("Consolas", 13), justify="left", anchor="nw", padx=10, pady=10)
    lbl.pack(fill="both", expand=True)

    act()
    print("panel accesorios cargado")
