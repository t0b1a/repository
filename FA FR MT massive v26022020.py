import tkinter as tk
from tkinter import ttk
import random
import re

# Create instance
win = tk.Tk( )

# Add a title
win.title("Tool per FA FR IMISEC v 1.0")

tabControl = ttk.Notebook(win)  # Create Tab Control

tab1 = ttk.Frame(tabControl)  # Create a tab
tabControl.add(tab1,text='FA e FR')  # Add the tab

tab2 = ttk.Frame(tabControl)  # Add a second tab
tabControl.add(tab2,text='MT')  # Make second tab visible

tabControl.pack(expand=1,fill="both")  # Pack to make visible

# psw bit
def randompassword():
	chars = 'abcdefghmnopqrstuvzxykw'
	chars2 = 'ABCDEFGHLMNOPQRSTUVZWXYK'
	nums = '23456789'
	size = random.randint(8,8)
	return ''.join(random.choice(chars) for x in range(4)).join(random.choice(nums) for x in range(2)).join(
		random.choice(chars2) for x in range(2))

psw = randompassword( )

# titoli tab
titolo_tab = ttk.Label(tab1,text="*** Generiamo FA o FR ***",background='aquamarine2')
titolo_tab.grid(column=0,row=0)

titolo_tab = ttk.Label(tab2,text="*** Generiamo MT ***",background='aquamarine2')
titolo_tab.grid(column=0,row=0)

# RADIOBUTTONS
# fa e fr label
tipo_lab = ttk.Label(tab1,text="Scegli tipologia")
tipo_lab.grid(column=0,row=2)
# fa e fr label
tipo_lab = ttk.Label(tab2,text="Scegli tipologia")
tipo_lab.grid(column=0,row=2)

# Radiobutton Callback FA FR
def radCall():
	radSel = radVar.get( )
	if radSel == 1:
		tipo_prodotto = 'FA'
	elif radSel == 2:
		tipo_prodotto = 'FR'

# Radiobutton Callback MT
def radCall_mt():
	radSel_mt = radVar_mt.get( )
	if radSel_mt == 1:
		tipo_marca = 'Infinite'
	elif radSel_mt == 2:
		tipo_marca = 'Precaricate'

# create two Radiobuttons using one variable for FA o FR
radVar = tk.IntVar( )
rad1 = tk.Radiobutton(tab1,text='FA',variable=radVar,value=1,command=radCall)
rad1.grid(column=1,row=2,sticky=tk.W,columnspan=1)
rad2 = tk.Radiobutton(tab1,text='FR',variable=radVar,value=2,command=radCall)
rad2.grid(column=1,row=2,sticky=tk.E,columnspan=1)

# create two Radiobuttons using one variable for infinite o precaricate
radVar_mt = tk.IntVar( )
rad1 = tk.Radiobutton(tab2,text='Infinite',variable=radVar_mt,value=1,command=radCall_mt)
rad1.grid(column=1,row=2,sticky=tk.W,columnspan=1)
rad2 = tk.Radiobutton(tab2,text='Precar.',variable=radVar_mt,value=2,command=radCall_mt)
rad2.grid(column=1,row=2,sticky=tk.E,columnspan=1)

# lista label
testo_label = ['Path per i file senza ultima \\','Cod cliente','Nome azienda','Account','Prima usr libera','Quante ne fai']
nome_label = ['user_label','cod_cli_label','nome azienda','acc_label','prima_libera_label','numero_cicli']
nome_entry = ['user_entry','cod_cli_entry','nome azienda','acc_entry','prima_libera_entry','numero_cicli_label']

testo_label_mt = ['Path per i file senza ultima \\','Cod cliente','Nome azienda','Account','Prima usr libera','Quante ne fai']
nome_label_mt  = ['user_label','cod_cli_label','nome azienda','acc_label','prima_libera_label','numero_cicli']
nome_entry_mt  = ['user_entry','cod_cli_entry','nome azienda','acc_entry','prima_libera_entry','numero_cicli_label']

# genera FR FA entry
for x in range(len(testo_label)):
	nome_label[x] = ttk.Label(tab1,text=testo_label[x])
	nome_label[x].grid(column=0,row=x + 4)
	nome_entry[x] = ttk.Entry(tab1)
	nome_entry[x].grid(column=1,row=x + 4)
	
# genera MT entry
for x in range(len(testo_label)):
	nome_label_mt[x] = ttk.Label(tab2,text=testo_label[x])
	nome_label_mt[x].grid(column=0,row=x + 4)
	nome_entry_mt[x] = ttk.Entry(tab2)
	nome_entry_mt[x].grid(column=1,row=x + 4)
	
def clickme(button_id):
	
	if button_id == 1:
		print('FA FR')
	
		# get values FA o FR
		path = nome_entry[0].get( )
		cod_cliente_isec = nome_entry[1].get( )
		nome_azienda = nome_entry[2].get( )
		account_isec = nome_entry[3].get( )
		prima_libera = nome_entry[4].get( )
		numero_cicli = nome_entry[5].get( )
		
		output_testo1 = ttk.Label(tab1,text="ho creato il file -"+path+"\\file_per_tool.txt")
		output_testo1.grid(column=0,row=10)
		output_testo2 = ttk.Label(tab1,text="ho creato il file - "+path+"\\file_con_usr_e_psw.txt")
		output_testo2.grid(column=0,row=11)
		output_testo3 = ttk.Label(tab1,text='FATTO! PUOI CHIUDERE LA FINESTRA',background='green',foreground='white')
		output_testo3.grid(column=0,row=13)
		
		# PER LAVORO
		baconFile2 = open(path+'\\file_con_usr_e_psw.txt','w')
		baconFile = open(path+'\\file_per_tool.txt','w')
	
	if button_id == 2:
		print('MT')
		
		# get values FA o FR
		path = nome_entry_mt[0].get( )
		cod_cliente_isec_mt = nome_entry_mt[1].get( )
		nome_azienda_mt = nome_entry_mt[2].get( )
		account_isec_mt = nome_entry_mt[3].get( )
		prima_libera_mt = nome_entry_mt[4].get( )
		numero_cicli_mt = nome_entry_mt[5].get( )
		
		output_testo1 = ttk.Label(tab2,text="ho creato il file -"+path+"\\file_per_tool.txt")
		output_testo1.grid(column=0,row=10)
		output_testo2 = ttk.Label(tab2,text="ho creato il file - "+path+"\\file_con_usr_e_psw.txt")
		output_testo2.grid(column=0,row=11)
		output_testo3 = ttk.Label(tab2,text='FATTO! PUOI CHIUDERE LA FINESTRA',background='green',foreground='white')
		output_testo3.grid(column=0,row=13)
		
		# PER LAVORO
		baconFile2 = open(path+'\\file_con_usr_e_psw.txt','w')
		baconFile = open(path+'\\file_per_tool.txt','w')
	
	# SCOMPOSIZIONE NUMERI E LETTERE PER LA USER LIBERA
	if button_id == 2:
		prima_libera = prima_libera_mt
		numero_cicli = numero_cicli_mt
	elif button_id == 1:
		prima_libera = prima_libera
		numero_cicli = numero_cicli
		
	numero_nella_stringa = (re.search('\d+\Z',prima_libera)).group( )
	
	try:
		count_zero_iniziali = (re.search(r'^0+',numero_nella_stringa)).group( )
		# print('zeri iniziali',count_zero_iniziali)
		lunghezza_zeri_iniziali = len(count_zero_iniziali)
	
	# print('lunghezza zeri iniziali',lunghezza_zeri_iniziali)
	except:
		print('+++')
	finally:
		lettere_nella_stringa = re.split(numero_nella_stringa,prima_libera)
		lettere_nella_stringa = lettere_nella_stringa[0]
	# print('lettere nella stringa',lettere_nella_stringa)
	# print('numero nella stringa',numero_nella_stringa)
		lunghezza_numero_stringa = len(numero_nella_stringa)
	
	# USER E PSW BLOCCO COMUNE A FA,FR E MARCHE
	
	
	for x in range(int(numero_cicli)):
		try:
			if lunghezza_zeri_iniziali is not None and numero_nella_stringa[-1] != '0':
				parte_numerica = str(int(numero_nella_stringa) + x)
				parte_numerica = parte_numerica.zfill(lunghezza_zeri_iniziali + 1)
				user = lettere_nella_stringa + parte_numerica
				# print('parte numerica',parte_numerica)
				# print('user',user)
			elif lunghezza_zeri_iniziali is not None and numero_nella_stringa[-1] == '0':
				parte_numerica = str(int(numero_nella_stringa) + x)
				parte_numerica = parte_numerica.zfill(lunghezza_zeri_iniziali)
				user = lettere_nella_stringa + parte_numerica
				# print('parte numerica',parte_numerica)
				# print('user',user)
		except:
			parte_numerica = str(int(numero_nella_stringa) + x)
			parte_numerica = parte_numerica.zfill(0 + 1)
			user = lettere_nella_stringa + parte_numerica
			psw_user = randompassword( )
		
		# FIRME REMOTE
		if radVar.get( ) == 2:
			# file da incollare su imisec
			# print('ADDP -d "FR" "FR" "FR"',cod_cliente_isec,user,file=baconFile)
			print('ADDP -d "FR" "FR" "' + nome_azienda + '"',cod_cliente_isec,user,file=baconFile)
			print('ADDI -d "FR" -pl 0','ncfr0101',user,user,account_isec,file=baconFile)
			print('ABID',user,'NCFR',file=baconFile)
			# file con user e marche
			print(user,'ncfr0101',file=baconFile2)
		
		# FIRME AUTOMATICHE
		elif radVar.get( ) == 1:
			# file da incollare su imisec
			# print('ADDP -d "FA" "FA" "FA"',cod_cliente_isec,user,file=baconFile)
			print('ADDP -d "FA" "FA" "' + nome_azienda + '"',cod_cliente_isec,user,file=baconFile)
			print('ADDI -d "FA" -pl 0','ncfr0101',user,user,account_isec,file=baconFile)
			print('ABID',user,'NCFA',file=baconFile)
			# file con user e marche
			print(user,'ncfr0101',file=baconFile2)
		
		# MARCHE TEMPORALI
		if radVar_mt.get( ) == 1:
			# file da incollare su imisec
			# print('ADDP -d "FA" "FA" "FA"',cod_cliente_isec,user,file=baconFile)
			print('ADDP -d "Marca Tecnica" "MT" "Tecnica"',cod_cliente_isec_mt,user,file=baconFile)
			print('ADDI -d "Marca Tecnica" -pl 0',psw_user,user,user,account_isec_mt,file=baconFile)
			print('STPRI',user,'tiposessione 10',file=baconFile)
			print('ABID',user,'W-CAMR',file=baconFile)
			print('ABID',user,'Q-CARM',file=baconFile)
			# file con user e marche
			print(user,psw_user,file=baconFile2)
		
		# MARCHE TEMPORALI
		elif radVar_mt.get( ) == 2:
			# file da incollare su imisec
			# print('ADDP -d "FA" "FA" "FA"',cod_cliente_isec,user,file=baconFile)
			print('ADDP -d "Marca Tecnica" "MT" "Tecnica"',cod_cliente_isec_mt,user,file=baconFile)
			print('ADDI -d "Marca Tecnica" -pl 0',psw_user,user,user,account_isec_mt,file=baconFile)
			print('STPRI',user,'tiposessione 10',file=baconFile)
			print('ABID',user,'W-CARM',file=baconFile)
			print('ABID',user,'Q-CARM',file=baconFile)
			# file con user e marche
			print(user,psw_user,file=baconFile2)

#bottone fa tab
bottone = ttk.Button(tab1,text='GENERA!',command=lambda: clickme(1))
bottone.grid(column=1,row=10)

#bottone mt tab
bottone2 = ttk.Button(tab2,text='GENERA!',command=lambda: clickme(2))
bottone2.grid(column=1,row=10)

# Exit GUI cleanly
def _quit():
	win.quit()
	win.destroy()
	exit()

# ======================
# Start GUI
# ======================
win.mainloop()