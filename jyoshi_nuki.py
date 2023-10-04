import tkinter
import MeCab


start_MeCab = MeCab.Tagger()

root = tkinter.Tk()
root.geometry("700x500")

def convert():
    global la_bel_answer
    
    la_bel_answer.delete(0,tkinter.END)
    word = []
    hinshi = []
    move_pos = 0

    sentence = en_try.get()
    node = start_MeCab.parseToNode(sentence)

    while node:


        
        word.append(node.surface)
        

        
        hinshi.append(node.feature)
        

        node = node.next


    


    for i in range(int(len(word))):
        
        if "助詞" in hinshi[move_pos]:
            

            word[move_pos] = ""
            
        move_pos = move_pos + 1
        

    result = "　".join(word)

    print(result)

    la_bel_answer.insert(tkinter.END,result)
    




la_bel = tkinter.Label(text="助詞を抜く")
en_try = tkinter.Entry(text="彼は助詞を抜いた")
bu_tton = tkinter.Button(text="変換",command=convert)
la_bel_answer = tkinter.Entry(text="結果")


la_bel.pack()
en_try.pack()
bu_tton.pack()
la_bel_answer.place(x=10,y=100,width=600,height=300)


root.mainloop()