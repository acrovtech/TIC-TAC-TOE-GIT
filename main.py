import tkinter as tk
from tkinter import messagebox

WIN_COMBOS = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),  # filas
    (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columnas
    (0, 4, 8), (2, 4, 6)              # diagonales
]

class TicTacToe:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Tic Tac Toe - Práctica Git")
 feature-gui-styling
        self.root.configure(bg="#1e1e1e")

 main

        # Estado del juego
        self.turno = "X"
        self.tablero = [""] * 9
        self.botones: list[tk.Button] = []
        self.juego_activo = True  # evita seguir jugando tras ganar/empatar

        self._build_ui()

    def _build_ui(self):
        """Construye la interfaz: tablero + indicador de turno."""
 feature-gui-styling
        board = tk.Frame(self.root, padx=10, pady=10, bg="#1e1e1e")

        board = tk.Frame(self.root, padx=10, pady=10)
 main
        board.pack()

        for i in range(9):
            btn = tk.Button(
                board,
                text="",
                font=("Arial", 20),
                width=5,
                height=2,
                bg="#2d2d2d",
                fg="white",
                activebackground="#3c3c3c",
                activeforeground="white",
                relief="flat",
                bd=0,
                command=lambda i=i: self.marcar_casilla(i),
            )
            btn.grid(row=i // 3, column=i % 3, padx=4, pady=4)
            self.botones.append(btn)

 feature-gui-styling
        controls = tk.Frame(self.root, pady=5, bg="#1e1e1e")

        controls = tk.Frame(self.root, pady=5)
 main
        controls.pack()

        self.lbl_turno = tk.Label(
            controls,
            text=f"Turno: {self.turno}",
            font=("Arial", 12, "bold"),
            bg="#1e1e1e",
            fg="white"
        )
        self.lbl_turno.pack()
 feature-gui-styling
        
        btn_reset = tk.Button(
            controls,
            text="Reiniciar",
            command=self.reset_game,
            bg="#ff8c00",
            fg="black",
            activebackground="#ffa733",
            activeforeground="black",
            relief="flat",
            bd=0,
            padx=12,
            pady=6
        )
        btn_reset.pack(pady=10)

        btn_reset = tk.Button(controls, text="Reiniciar", command=self.reset_game)
        btn_reset.pack(pady=6)
 main


    def marcar_casilla(self, i: int):
        """Marca una casilla si está vacía y el juego sigue activo."""
        if not self.juego_activo:
            return

        if self.tablero[i] != "":
            return

        # 1) marcar en tablero + UI
        self.tablero[i] = self.turno
        self.botones[i].config(text=self.turno)

        # 2) verificar ganador
        if self._hay_ganador(self.turno):
            self.juego_activo = False
            messagebox.showinfo("Fin del juego", f"¡Ganó {self.turno}!")
            return

        # 3) verificar empate
        if self._hay_empate():
            self.juego_activo = False
            messagebox.showinfo("Fin del juego", "¡Empate! No hay espacios disponibles.")
            return

        # 4) cambiar turno
        self.turno = "O" if self.turno == "X" else "X"
        self.lbl_turno.config(text=f"Turno: {self.turno}")

    def _hay_ganador(self, jugador: str) -> bool:
        """Devuelve True si 'jugador' tiene una combinación ganadora."""
        for a, b, c in WIN_COMBOS:
            if self.tablero[a] == jugador and self.tablero[b] == jugador and self.tablero[c] == jugador:
                return True
        return False

    def _hay_empate(self) -> bool:
        """Devuelve True si el tablero está lleno y nadie ganó."""
        return all(celda != "" for celda in self.tablero)
 feature-gui-styling

 feature-reset
 main
    

    def reset_game(self):
        """Reinicia tablero, turno y permite jugar otra vez sin cerrar la ventana."""
        self.turno = "X"
        self.tablero = [""] * 9
        self.juego_activo = True

        for btn in self.botones:
            btn.config(text="")

        self.lbl_turno.config(text=f"Turno: {self.turno}")

 feature-gui-styling

 main

 main

if __name__ == "__main__":
    root = tk.Tk()
    app = TicTacToe(root)
    root.mainloop()