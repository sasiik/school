import tkinter as tk
import random


def tulosta_kasvavasti_tk():
    root = tk.Tk()
    root.title("Kasvava merkkijono")
    canvas = tk.Canvas(root, width=200, height=200)
    canvas.pack()

    for i in range(1, 8):
        canvas.create_text(100, i * 20, text="o" * i, font=("Arial", 14))

    root.mainloop()


def liikkuva_pallo():
    def move_ball():
        x1, y1, x2, y2 = canvas.coords(ball)
        if x2 > 300 or x1 < 0:
            dx[0] = -dx[0]
        if y2 > 300 or y1 < 0:
            dy[0] = -dy[0]
        canvas.move(ball, dx[0], dy[0])
        root.after(30, move_ball)

    root = tk.Tk()
    root.title("Liikkuva pallo")
    canvas = tk.Canvas(root, width=300, height=300)
    canvas.pack()

    ball = canvas.create_oval(50, 50, 70, 70, fill="red")
    dx, dy = [2], [3]
    move_ball()
    root.mainloop()


def toinen_liikkuva_pallo():
    def move_ball():
        canvas.move(ball, random.randint(-5, 5), random.randint(-5, 5))
        root.after(50, move_ball)

    root = tk.Tk()
    root.title("Toinen liikkuva pallo")
    canvas = tk.Canvas(root, width=300, height=300)
    canvas.pack()

    ball = canvas.create_oval(100, 100, 120, 120, fill="blue")
    move_ball()
    root.mainloop()


def piirra_ruudukko(leveys, korkeus):
    root = tk.Tk()
    root.title("Ruudukko")
    canvas = tk.Canvas(root, width=leveys*20, height=korkeus*20)
    canvas.pack()

    for i in range(leveys + 1):
        canvas.create_line(i * 20, 0, i * 20, korkeus * 20)
    for j in range(korkeus + 1):
        canvas.create_line(0, j * 20, leveys * 20, j * 20)

    root.mainloop()


def piirra_vareilla(leveys, korkeus, tilat):
    root = tk.Tk()
    root.title("Ruudukko värityksellä")
    canvas = tk.Canvas(root, width=leveys * 20, height=korkeus * 20)
    canvas.pack()

    for i in range(leveys):
        for j in range(korkeus):
            color = "black" if tilat[i * korkeus + j] else "white"
            canvas.create_rectangle(
                i * 20, j * 20, (i+1) * 20, (j+1) * 20, fill=color, outline="gray")

    root.mainloop()


# Example usage
tulosta_kasvavasti_tk()
liikkuva_pallo()
toinen_liikkuva_pallo()
piirra_ruudukko(10, 10)
piirra_vareilla(10, 10, [random.choice([True, False]) for _ in range(100)])
