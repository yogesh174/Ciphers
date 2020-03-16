def encrypt(label_result,pt,k):
    pt = pt.get()
    k = int(k.get())%26
    ct=""
    for i in pt:
        asc_i = ord(i)
        if(65 <= asc_i <= 90):
            if(asc_i + k > 90):
                asc_i -= 26
            ct = ct + chr(asc_i + k)        
            continue
        elif(97 <= asc_i <= 122):
            if(asc_i + k > 122):
                asc_i -= 26
            ct = ct + chr(asc_i + k)
            continue
        ct = ct + i
    label_result.config(text="Cipher text:"+ct)
    
  
def decrypt(label_result,ct,k):
    ct = ct.get()
    k = int(k.get())%26
    pt=""
    for i in ct:
        asc_i = ord(i)
        if(65 <= asc_i <= 90):
            if(asc_i - k < 65):
                asc_i += 26
            pt = pt + chr(asc_i - k)        
            continue
        elif(97 <= asc_i <= 122):
            if(asc_i - k < 97):
                asc_i += 26
            pt = pt + chr(asc_i - k)
            continue
        pt = pt + i
        
    label_result.config(text="Plain text:"+pt)


from functools import partial
from tkinter import *

root = Tk()
root.title("Shift Cipher")
root.geometry('600x300+650+300')
root.config(bg='black')

label_shift_cipher = Label(root,text="Shift Cipher",font=("Helvetica",25),bg='black',fg='white').pack(fill='x',ipady=10)

frame_e_t = Frame(root,bg='black')
frame_e_t.pack()

frame_e_k = Frame(root,bg="black")
frame_e_k.pack()

frame_e_but = Frame(root,bg="black")
frame_e_but.pack()

frame_e_res = Frame(root,bg="black")
frame_e_res.pack()


button_text = StringVar()
type_of_text = StringVar()
button_text.set('Encrypt')
type_of_text.set('Plain text')

opt_men_t = OptionMenu(frame_e_t,type_of_text,'Plain text','Cipher text')
opt_men_t.config( font=('Helvetica', 15),fg = 'red',bg='black')
opt_men_t['menu'].config(font=('Helvetica', 15),fg = 'skyblue',bg='black')
opt_men_t.pack(side='left',padx=10,pady=10)
label_k = Label(frame_e_k,text = "Key(1-25)",bg='black',fg='red',font=("Helvetica", 15))
label_k.pack(side='left',padx=25,pady=5)

t = StringVar()
k = StringVar()

entry_t = Entry(frame_e_t,textvariable=t,font=("Helvetica", 13))
entry_t.pack(side='right')
entry_k = Entry(frame_e_k,textvariable=k,font=("Helvetica", 13))
entry_k.pack(side='right')

label_result = Label(frame_e_res,bg='black',font=("Helvetica", 15),fg='#15bbed')
label_result.pack(pady=10)

encrypt = partial(encrypt,label_result,t,k)
decrypt = partial(decrypt,label_result,t,k)

button_encrypt = Button(frame_e_but,text=button_text.get(),command=encrypt)
button_encrypt.pack(pady=5)

def on_chng_of_txt_typ(label_result,but_enc,label_k,*args):
    label_result.config(text = "")
    if "Plain text" == type_of_text.get():
        but_enc.config(text = "Encrypt",command = encrypt)
        label_k.config(padx=1)
        
    elif "Cipher text" == type_of_text.get():
        but_enc.config(text = "Decrypt",command = decrypt)
        label_k.config(padx=11)
        
on_chng_of_txt_typ = partial(on_chng_of_txt_typ,label_result,button_encrypt,label_k)
type_of_text.trace('w',on_chng_of_txt_typ)

root.mainloop()
