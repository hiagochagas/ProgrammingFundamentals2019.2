from tkinter import *
def reajuste():
    salario=float(entrada_salario.get())
    item=escolha.get()
    reajuste_a=1.15
    if item=="A":
        reajuste_b=1.1
        reajuste_c=1.05
    elif item=="B":
        reajuste_b=1.12
        reajuste_c=1.08
    if salario<500:
        salario*=reajuste_a
    elif(salario>1000):
        salario*=reajuste_c
    else:
        salario*=reajuste_b
    salario_reajustado["text"]="Salário reajustado: R$ %.2f"%salario

janelaPrincipal = Tk()
janelaPrincipal.title("Reajuste Salarial")
janelaPrincipal.geometry("500x500+500+200")

texto_salario = Label(janelaPrincipal, text="Salário do empregado:", font="impact 35 italic")
texto_salario.pack()

entrada_salario = Entry(janelaPrincipal)
entrada_salario.pack()

escolha = StringVar()
escolha1 = Radiobutton(janelaPrincipal,text='Item A', value='A', variable = escolha, font="35") 
escolha2 = Radiobutton(janelaPrincipal,text='Item B', value='B', variable = escolha, font="35") 
escolha1.pack()
escolha2.pack()

botao_reajuste = Button(janelaPrincipal, text="Reajustar", command=reajuste, font="35") 
botao_reajuste.pack()

salario_reajustado = Label(janelaPrincipal,font="impact 30", text="Salário reajustado: R$ 0")
salario_reajustado.pack()

janelaPrincipal.mainloop() #deixar por último

