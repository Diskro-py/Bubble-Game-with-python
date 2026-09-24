import tkinter as tk
import random

root = tk.Tk()  # fenster erstellen
root.title("bubble popp")  # name des fensters
root.state('zoomed')  # vollbild

los = False

speed = 10
speedkugel = 5

score = 0

red = None
red2 = None
red3 = None
red4 = None
red5 = None
red6 = None
red7 = None

größe = random.randint(50, 75)
yzufall = random.randint(0, 1000 - größe)

größe2 = random.randint(50, 75)
yzufall2 = random.randint(0, 1000 - größe2)

größe3 = random.randint(50, 75)
yzufall3 = random.randint(0, 1000 - größe3)

größe4 = random.randint(50, 75)
yzufall4 = random.randint(0, 1000 - größe4)

größe5 = random.randint(50, 75)
yzufall5 = random.randint(0, 1000 - größe5)

größe6 = random.randint(50, 75)
yzufall6 = random.randint(0, 1000 - größe6)

größe7 = random.randint(50, 75)
yzufall7 = random.randint(0, 1000 - größe7)

tasten = {}

root.bind("<KeyPress>", lambda e: tasten.update({e.keysym: True}))
root.bind("<KeyRelease>", lambda e: tasten.update({e.keysym: False}))


canvas = tk.Canvas(root, width=1800, height=1000, bg="midnightblue")  # breite/höhe/farbe des fensters
canvas.pack()  # fenster erstellen


kreis = canvas.create_oval(250 - 50, 600 - 50, 250 + 50, 400 + 50, fill="midnightblue", outline="lime", width=16)  # kreis erstellen

bubble = canvas.create_oval(1800, yzufall, 1800 + größe, yzufall + größe, fill="blue", outline="blue", width=1)
bubble2 = canvas.create_oval(1800, yzufall2, 1800 + größe2, yzufall2 + größe2, fill="blue", outline="blue", width=1)
bubble3 = canvas.create_oval(1800, yzufall3, 1800 + größe3, yzufall3 + größe3, fill="blue", outline="blue", width=1)
bubble4 = canvas.create_oval(1800, yzufall4, 1800 + größe4, yzufall4 + größe4, fill="blue", outline="blue", width=1)
bubble5 = canvas.create_oval(1800, yzufall5, 1800 + größe5, yzufall5 + größe5, fill="blue", outline="blue", width=1)
bubble6 = canvas.create_oval(1800, yzufall6, 1800 + größe6, yzufall6 + größe6, fill="blue", outline="blue", width=1)
bubble7 = canvas.create_oval(1800, yzufall7, 1800 + größe7, yzufall7 + größe7, fill="blue", outline="blue", width=1)


linie = canvas.create_line(0, 1000, 0, 0, fill="midnightblue", width=5)


timer = 0
los = random.randint(60, 360)
los2 = random.randint(60, 360)
los3 = random.randint(60, 360)
los4 = random.randint(60, 360)
los5 = random.randint(60, 360)
los6 = random.randint(60, 360)
los7 = random.randint(60, 360)


score_anzeige = canvas.create_text(75, 25, text=f"Score: {score}", fill="white", font=("Arial", 20, "bold"))



def game_loop():
    
    global score
    global timer

    linksoben = 0
    linksunten = 0
    rechtsoben = 0
    rechtunten = 0


    x1, y1, x2, y2 = canvas.bbox(kreis)
    collision = canvas.find_overlapping(x1, y1, x2, y2)

    if y1 > 0: 
        if tasten.get("Up") or tasten.get("w"):
            canvas.move(kreis, 0, -speed)
    if y2 < 1000:
        if tasten.get("Down") or tasten.get("s"):
            canvas.move(kreis, 0, +speed)
    if x1 > 0:
        if tasten.get("a") or tasten.get("Left"):
            canvas.move(kreis, -speed, 0)
    if x2 < 1800:
        if tasten.get("d") or tasten.get("Right"):
            canvas.move(kreis, +speed, 0)
        


    if bubble in collision:
        
        canvas.itemconfig(bubble, fill="blue", outline="blue")
        red = 0
        größe = random.randint(10, 300)
        yzufall = random.randint(0, 1000 - größe)
        canvas.coords(bubble, 1800, yzufall, 1800 + größe, yzufall + größe)
        score += 1
        canvas.itemconfig(score_anzeige, text=f"Score: {score}")
        
            
    elif bubble2 in collision:
        
        canvas.itemconfig(bubble2, fill="blue", outline="blue")
        größe2 = random.randint(10, 300)
        yzufall2 = random.randint(0, 1000 - größe2)
        canvas.coords(bubble2, 1800, yzufall2, 1800 + größe2, yzufall2 + größe2)
        score += 1
        canvas.itemconfig(score_anzeige, text=f"Score: {score}")
         
    elif bubble3 in collision:
       
        canvas.itemconfig(bubble3, fill="blue", outline="blue")
        größe3 = random.randint(10, 300)
        yzufall3 = random.randint(0, 1000 - größe3)
        canvas.coords(bubble3, 1800, yzufall3, 1800 + größe3, yzufall3 + größe3)
        score += 1
        canvas.itemconfig(score_anzeige, text=f"Score: {score}")
        red3 = random.randint(1, 10)
        
    elif bubble4 in collision:
        
        canvas.itemconfig(bubble4, fill="blue", outline="blue")
        größe4 = random.randint(10, 300)
        yzufall4 = random.randint(0, 1000 - größe4)
        score += 1
        canvas.coords(bubble4, 1800, yzufall4, 1800 + größe4, yzufall4 + größe4)
        canvas.itemconfig(score_anzeige, text=f"Score: {score}")
        
    elif bubble5 in collision:
        
        canvas.itemconfig(bubble5, fill="blue", outline="blue")
        größe5 = random.randint(10, 300)
        yzufall5 = random.randint(0, 1000 - größe5)
        canvas.coords(bubble5, 1800, yzufall5, 1800 + größe5, yzufall5 + größe5)
        score += 1
        canvas.itemconfig(score_anzeige, text=f"Score: {score}")
        red5 = random.randint(1, 10)
        
    elif bubble6 in collision:
        
        canvas.itemconfig(bubble6, fill="blue", outline="blue")
        größe6 = random.randint(10, 300)
        yzufall6 = random.randint(0, 1000 - größe6)
        canvas.coords(bubble6, 1800, yzufall6, 1800 + größe6, yzufall6 + größe6)
        score += 1
        canvas.itemconfig(score_anzeige, text=f"Score: {score}")
        red6 = random.randint(1, 10)
       
    elif bubble7 in collision:
        
        canvas.itemconfig(bubble7, fill="blue", outline="blue")
        größe7 = random.randint(10, 300)
        yzufall7 = random.randint(0, 1000 - größe7)
        canvas.coords(bubble7, 1800, yzufall7, 1800 + größe7, yzufall7 + größe7)
        score += 1
        canvas.itemconfig(score_anzeige, text=f"Score: {score}")
       


    xline1, yline1, xline2, yline2 = canvas.bbox(linie)
    collisionline = canvas.find_overlapping(xline1, yline1, xline2, yline2)


    if bubble in collisionline:
        canvas.delete("all")
        canvas.create_text(900, 500, text=f"Final Score: {score}", fill="white", font=("Arial", 100, "bold"))
        
    if bubble2 in collisionline:
        canvas.delete("all")
        canvas.create_text(900, 500, text=f"Final Score: {score}", fill="white", font=("Arial", 100, "bold"))
    
    if bubble3 in collisionline:
        if red3 != 1:
            canvas.delete("all")
            canvas.create_text(900, 500, text=f"Final Score: {score}", fill="white", font=("Arial", 100, "bold"))
        else:
            größe3 = random.randint(10, 300)
            yzufall3 = random.randint(0, 1000 - größe3)
            canvas.coords(bubble3, 1800, yzufall3, 1800 + größe3, yzufall3 + größe3)
        
    if bubble4 in collisionline:
        canvas.delete("all")
        canvas.create_text(900, 500, text=f"Final Score: {score}", fill="white", font=("Arial", 100, "bold"))
        
    if bubble5 in collisionline and red5 != 1:
        canvas.delete("all")
        canvas.create_text(900, 500, text=f"Final Score: {score}", fill="white", font=("Arial", 100, "bold"))
        
    if bubble6 in collisionline:
        canvas.delete("all")
        canvas.create_text(900, 500, text=f"Final Score: {score}", fill="white", font=("Arial", 100, "bold"))
        
    if bubble7 in collisionline:
        canvas.delete("all")
        canvas.create_text(900, 500, text=f"Final Score: {score}", fill="white", font=("Arial", 100, "bold"))
        


    timer += 1
    if los <= timer:
        canvas.move(bubble, -speedkugel, 0)
    if los2 <= timer:
        canvas.move(bubble2, -speedkugel, 0)
    if los3 <= timer:
        canvas.move(bubble3, -speedkugel, 0)
    if los4 <= timer:
        canvas.move(bubble4, -speedkugel, 0)
    if los5 <= timer:
        canvas.move(bubble5, -speedkugel, 0)
    if los6 <= timer:
        canvas.move(bubble6, -speedkugel, 0)
    if los7 <= timer:
        canvas.move(bubble7, -speedkugel, 0)

 
    root.after(5, game_loop)

def time():
    global speedkugel
    speedkugel += 0.1
    root.after(1000, time)
time()
game_loop()
root.mainloop()# loslegen
