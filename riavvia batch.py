import tkinter as tk
import requests

root = tk.Tk( )

canvas1 = tk.Canvas(root,width=400,height=300,relief='raised')
canvas1.pack( )

label1 = tk.Label(root,text='Riavvia un Batch')
label1.config(font=('helvetica',14))
canvas1.create_window(200,25,window=label1)

label2 = tk.Label(root,text='Metti batch_id:')
label2.config(font=('helvetica',10))
canvas1.create_window(200,100,window=label2)

entry1 = tk.Entry(root)
canvas1.create_window(200,140,window=entry1)


def getSquareRoot():
	x1 = entry1.get( )
	r = requests.post('https://mmig.print.infocert.it/mmig-loader/rest/batch/'+x1+'/restart')
	
	label3 = tk.Label(root,text=r.status_code)
	canvas1.create_window(200,210,window=label3)
	
	if r.status_code == 200 or r.status_code == 201:
		label4 = tk.Label(root,text='SUCCESSO',bg='green',fg='white')
		canvas1.create_window(200,230,window=label4)

	else:
		label4 = tk.Label(root,text='FALLITO',bg='red',fg='white')
		canvas1.create_window(200,230,window=label4)
	
	
	# else:
	# 	label4 = tk.Label(root,text='FALLITO')
	# 	canvas1.create_window(200,230,window=label4)


button1 = tk.Button(text='RIAVVIA',command=getSquareRoot,bg='black',fg='white',font=('helvetica',9,'bold'))
canvas1.create_window(200,180,window=button1)

root.mainloop( )