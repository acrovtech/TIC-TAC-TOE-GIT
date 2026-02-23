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
        self.turno = "X"
        self.tablero = [""] * 9
        self.botones: list[tk.Button] = []

        self._build_ui()

    def _build_ui(self):
        # Frame tablero
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

        # Frame controles (más adelante aquí irá Reset en su rama)
        controls = tk.Frame(self.root, pady=5)
        controls.pack()

        self.lbl_turno = tk.Label(controls, text=f"Turno: {self.turno}", font=("Arial", 12))
        self.lbl_turno.pack()

    def marcar_casilla(self, i: int):
        if self.tablero[i] != "":
            return

        self.tablero[i] = self.turno
        self.botones[i].config(text=self.turno)

        # NOTA: lógica de ganador/empate irá en feature-logic
        self.turno = "O" if self.turno == "X" else "X"
        self.lbl_turno.config(text=f"Turno: {self.turno}")


if __name__ == "__main__":
    root = tk.Tk()
    app = TicTacToe(root)
    root.mainloop()