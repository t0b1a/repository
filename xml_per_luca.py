import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

# Create instance
win = tk.Tk()

#titolo finestra
win.title("Aggiungi GB a PEC conservazione")

#titolo programma
titolo_label = ttk.Label(win,text='Crea .xml per aggiungere GB alle PEC')
titolo_label.grid(column=0,row=0)

#riga vuota dopo titolo
spazio_label = ttk.Label(win,text=' ')
spazio_label.grid(column=0,row=1)

#user label e user entry
user_label = ttk.Label(win,text='La tua userID')
user_label.grid(column=0,row=2)
user_entry = ttk.Entry(win)
user_entry.grid(column=1,row=2)

#mb label e user entry
mb_label = ttk.Label(win,text='Quanti MB aggiungere (senza+)')
mb_label.grid(column=0,row=3)
mb_entry = ttk.Entry(win)
mb_entry.grid(column=1,row=3)

#funzione per click button
def UploadAction(event=None):
	# casa
	#baconfile = open('C:\\Users\\tobia\\Desktop\\risultato.txt','w')
	user_infocert = user_entry.get( )
	# lavoro
	baconfile = open('C:\\Users\\'+user_infocert+'\\Desktop\\risultato.xml','w')


	filename = filedialog.askopenfilename()

	fh = open(filename)
	print('<ORDINE>',file=baconfile)
	for line in fh:
		line = line.strip()
		#print(line+' '+mb_entry.get(),file=baconfile)
		print('<MODIFICA><CONSERVAZIONE><QTA>+'+mb_entry.get()+'</QTA></CONSERVAZIONE><CASELLE><CASELLA uid ="'+line+'"/></CASELLE></MODIFICA>',file=baconfile)
	print('</ORDINE>',file=baconfile)
	fh.close()
	
	# output
	output_label = ttk.Label(win,text='SUCCESSO!',background='Green',foreground='White')
	output_label.grid(column=0,row=5)

	#output1
	output1_label = ttk.Label(win,text='File creato C:\\Users\\'+user_infocert+'\\Desktop\\risultato.xml')
	output1_label.grid(column=0,row=6)

#button
button = tk.Button(win, text='Carica .txt con user', command=UploadAction, bg='#5daced')
button.grid(column=1,row=4)

# Exit GUI cleanly
def _quit():
	win.quit()
	win.destroy()
	exit()

# ======================
# Start GUI
# ======================
win.mainloop()