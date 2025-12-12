def bb(d: str):
    print(d)
chat=[]
def rite(ata: str, mg: str, ad: str):
    try:
        n2 = open("history.log", "a")
        n2.write(ata + "-" + ad + " said: " + mg + "\n")
        n2.close()
        # print(ata + "-" + ad + " said: " + mg)
    except Exception as e:
        print("Error alela ahe!!", e)

def get_temp(v: str) -> str:
    con = "<div class='mg'><p>{}</p></div>"
    return con.format(v)

def gt_fle() -> list:
    chat.clear()
    y = open("history.log", "r")
    for _ in y.readlines():
        if str(_)[32].isnumeric():
            try:
                b = str(_).strip("\n")
                chat.append(b[39:])
            except:
                print("Error in file!")
        else:
            try:
                c = str(_).strip("\n")                                  
                chat.append(c[38:])
            except:
                print("error in file!")
    y.close()
    return chat

def do() -> list:
    fuck = []
    fuck2 = gt_fle()
    for q in fuck2:
        fuck.append(q)
    return fuck
