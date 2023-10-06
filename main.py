from Bio.SeqUtils import MeltingTemp as tm
from tkinter import *
from tkinter import messagebox
import random
import matplotlib.pyplot as plt


FONT_NAME = "Courier"
def generate_random_dna_sequence():
    how_long_text = how_long_entry.get()
    if len(how_long_text) == 0:
        messagebox.showinfo(title="Oops", message="Upewnij sie czy na pewno wpisales dlugosc sekwencji.")
    how_long = int(how_long_text)
    dna_bases = "ACGT"
    random_sequence = [random.choice(dna_bases) for _ in range(how_long)]
    sequence = "".join(random_sequence)
    random_sequence_entry.delete(0,"end")
    random_sequence_entry.insert(0,sequence)


def calculate_Tm():
    sequence_to_calculate_temp = random_sequence_entry.get()
    tm_valueGC = tm.Tm_GC(sequence_to_calculate_temp)
    tm_valueNN =tm.Tm_NN(sequence_to_calculate_temp)


    results_entry1.delete(0,"end")
    results_entry2.delete(0,"end")
    results_entry1.insert(0,str(tm_valueGC) + " °C")
    results_entry2.insert(0, str(tm_valueNN) + " °C")

def show_visualization():
    sequence = random_sequence_entry.get()

    # Obliczanie procentowej zawartości każdej z baz w sekwencji
    a_count = sequence.count("A")
    c_count = sequence.count("C")
    g_count = sequence.count("G")
    t_count = sequence.count("T")
    total_bases = len(sequence)

    # Tworzenie wykresu kołowego dla zawartości baz
    labels = ['A', 'C', 'G', 'T']
    sizes = [a_count, c_count, g_count, t_count]
    colors = ['blue', 'green', 'red', 'purple']
    explode = (0.1, 0, 0, 0)  # Wyciągnięcie kawałka wykresu dla 'A'
    plt.figure(figsize=(10, 5))  # Rozmiar wykresu
    plt.subplot(1, 2, 1)  # Tworzenie pierwszego subplotu
    plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
    plt.axis('equal')  # Równy wykres kołowy
    plt.title("Procentowa zawartość baz w losowej sekwencji DNA")

    # Tworzenie wykresu słupkowego dla ilości baz
    bases = ['A', 'C', 'G', 'T']
    base_counts = [a_count, c_count, g_count, t_count]
    plt.subplot(1, 2, 2)  # Tworzenie drugiego subplotu
    plt.bar(bases, base_counts, color=colors)
    plt.title("Ilość poszczególnych baz")
    plt.ylabel("Ilość")


    # Wyświetlenie wizualizacji
    plt.tight_layout()  # Zapobiega przekrywaniu się elementów wykresu
    plt.show()





#UI SETUP

window = Tk()
window.title("Kalkulator (Tm) dla sekwencji DNA")
window.geometry("600x720")
window.config(padx=60, bg="#222831")

canvas = Canvas(height=200, width=200, bg="#222831" , highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
logo_img = logo_img.subsample(6)
canvas.create_image(100,100, image=logo_img)
canvas.grid(row=1, column=0)

#LABELS

title_label = Label(text="Kalkulator Tm sekwencji DNA", fg="#00ADB5", bg="#222831", font=(FONT_NAME,18,"bold"))
title_label.grid(column=0, row=0,pady=55,padx=50)

how_long_label = Label(text="Podaj długość losowej sekwencji DNA:",bg=window.cget('bg'), font=(FONT_NAME,12,"bold"), fg="#EEEEEE")
how_long_label.grid(column=0,row=3, pady=15)

random_sequence_label = Label(text="Twoja losowa sekwencja DNA:",bg=window.cget('bg'), font=(FONT_NAME,12,"bold"), fg="#EEEEEE")
random_sequence_label.grid(column=0,row=6)

results_label1 = Label(text="GC melting temperature:",bg=window.cget('bg'), font=(FONT_NAME,12,"bold"), fg="#EEEEEE")
results_label1.grid(column=0,row=9)

results_label2 = Label(text="Nearest-neighbor melting temperature:",bg=window.cget('bg'), font=(FONT_NAME,12,"bold"), fg="#EEEEEE")
results_label2.grid(column=0,row=11)

view_label = Label(text="Pokaz wizualizacje % zawartosci baz!",bg=window.cget('bg'), font=(FONT_NAME,12,"bold"), fg="#EEEEEE")
view_label.grid(column=0,row=13)



#Entries
how_long_entry = Entry(width=30)
how_long_entry.grid(column=0, row=4)

random_sequence_entry = Entry(width=30)
random_sequence_entry.grid(column=0, row=7)

results_entry1 =Entry(width=30)
results_entry1.grid(column=0,row=10)

results_entry2 =Entry(width=30)
results_entry2.grid(column=0,row=12)



#Buttons

generate_random_DNA = Button(text="Generuj losową sekwencje DNA",bg="#00ADB5", width=30, command=generate_random_dna_sequence)
generate_random_DNA.grid(column=0,row=5,pady=10)

calculate_Tm_DNA = Button(text="Oblicz temperature topnienia powyzszej sekwencji DNA",bg="#00ADB5", width=50, command=calculate_Tm)
calculate_Tm_DNA.grid(column=0,row=8,pady=15)

view = Button(text="WIZUALIZACJA",bg="#00ADB5",width=15, command=show_visualization)
view.grid(column=0,row=14,pady=5)



window.mainloop()

