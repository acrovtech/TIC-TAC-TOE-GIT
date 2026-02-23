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

        # Estado del juego
        self.turno = "X"
        self.tablero = [""] * 9
        self.botones: list[tk.Button] = []
        self.juego_activo = True  # evita seguir jugando tras ganar/empatar

        self._build_ui()

    def _build_ui(self):
        """Construye la interfaz: tablero + indicador de turno."""
        board = tk.Frame(self.root, padx=10, pady=10)
        board.pack()

        for i in range(9):
            btn = tk.Button(
                board,
                text="",
                font=("Arial", 20),
                width=5,
                height=2,
                command=lambda i=i: self.marcar_casilla(i),
            )
            btn.grid(row=i // 3, column=i % 3, padx=4, pady=4)
            self.botones.append(btn)

        controls = tk.Frame(self.root, pady=5)
        controls.pack()

        self.lbl_turno = tk.Label(controls, text=f"Turno: {self.turno}", font=("Arial", 12))
        self.lbl_turno.pack()

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


if __name__ == "__main__":
    root = tk.Tk()
    app = TicTacToe(root)
    root.mainloop()