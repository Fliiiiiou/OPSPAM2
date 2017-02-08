from tkinter import *
import time #Necessaire pour le timer

#DébutTimer
class App():
    def __init__(self):
        self.root = tk.Tk()
        self.label = tk.Label(text="")
        self.label.pack()
        self.update_clock()
        self.root.mainloop()

    def update_clock(self):
        now = time.strftime("%H:%M:%S")
        self.label.configure(text=now)
        self.root.after(1000, self.update_clock)
#FinTimer

class Fonctions_Boutons() :
    def Start() :
        ab#Insérer fonction
    def Stop() :
        ab#Insérer fonction
    def Exit():
        ab#Insérer fonction

fen=Tk()
fen.title("MailBomber")
fen.geometry('800x600')#Taille de la fenêtre en pixel

#Boutons :
bouton_Start = Button(fen, text="Demarrer") #Bouton Démarrer
bouton_Start.pack(pady=10)

bouton_Stop = Button(fen, text="Arrêter") #Bouton Arrêter
bouton_Stop.pack(pady=10)

bouton_Exit = Button(fen, text="Quitter") #Bouton Quitter
bouton_Exit.pack(pady=10)
#Fin de boutons.

#Zones de texte :
var_texte = StringVar()
ligne_texte = Entry(fen, textvariable=var_texte, width=30)
ligne_texte.pack(pady=10)

var_texte2 = StringVar()
ligne_texte = Entry(fen, textvariable=var_texte2, width=30)
ligne_texte.pack(pady=10)

var_texte3 = StringVar()
ligne_texte = Entry(fen, textvariable=var_texte3, width=30)
ligne_texte.pack(pady=10)

var_texte4 = StringVar()
ligne_texte = Entry(fen, textvariable=var_texte4, width=30)
ligne_texte.pack(pady=10)

var_texte5 = StringVar()
ligne_texte = Entry(fen, textvariable=var_texte5, width=30)
ligne_texte.pack(pady=10)
#Fin de zones de texte.

#Step4 :

#Dim MyMailssage As New MailMessage()
#MyMailssage.From = New MailAddress(textbox1.Text)
#MyMailssage.To.Add(textbox3.Text)
#MyMailssage.Subject = (textbox4.Text)
#MyMailssage.Body = textbox5.Text
#Dim SMTPServer As New SmtpClient("smtp.gmail.com")
#SMTPServer.Port = 587
#SMTPServer.Credentials = New System.Net.NetworkCredential(textbox1.Text, textbox2.Text)
#SMTPServer.EnableSsl = True
#Label1.Text = Val(Label1.Text + 1)
#SMTPServer.Send(MyMailssage)

fen.mainloop()