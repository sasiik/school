# Task 1: Growing and Decreasing Output
import tkinter as tk


def tulosta_kasvavasti(maksimi, merkki):
    for i in range(1, maksimi + 1):
        print(merkki * i)


def tulosta_vahenevasti(maksimi, merkki):
    for i in range(maksimi, 0, -1):
        print(merkki * i)

# Task 2: Pyramid


def tulosta_pyramidi(korkeus, merkki):
    for i in range(1, korkeus + 1):
        print(merkki * i)
    for i in range(korkeus - 1, 0, -1):
        print(merkki * i)


# Task 3: Tkinter Graphics


def piirra_ympyra(canvas, x, y, r, vari):
    canvas.create_oval(x - r, y - r, x + r, y + r, outline=vari, fill=vari)


def piirra_grafiikka():
    root = tk.Tk()
    root.title("Piirtotesti")
    canvas1 = tk.Canvas(root, width=400, height=400)
    canvas1.pack()
    piirra_ympyra(canvas1, 200, 200, 50, 'green')
    canvas1.create_line(0, 0, 356, 356, fill='yellow', width=3)
    root.mainloop()


# Uncomment to test functions:
# tulosta_kasvavasti(7, "o")
# tulosta_vahenevasti(7, "o")
# tulosta_pyramidi(5, "o")
# piirra_grafiikka()
