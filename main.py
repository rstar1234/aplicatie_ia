n = 8
import n_regine_bt
import n_regine_alpinist
while True:
    input()
    print("""
    a. Problema celor N regine (backtracking recursiv)
    b. Problema celor N regine (alg. alpinistului)
    c. Problema celor N regine (alg. calirii simulate)
    d. Problema celor N regine (alg. genetic)
    e. Plotare grafice problema celor N regine
    f. Problema comis-voiajorului (backtracking recursiv)
    g. Problema comis-voiajorului (alg. celui mai apropiat vecin)
    h. Plotare grafice problema comis-voiajorului
    x. Info
    q. Exit

    Alegeti o optiune:
          
""")
    
    option = input()

    if option.strip() == "q":
        break

    elif option.strip() == "x":
        #update later
        print("Info")

    elif option.strip() == "a":
        """ n = int(input("Marimea tablei de sah: "))
        f = open("var.txt", "w")
        f.write(n)
        f.close() """
        n_regine_bt.rezolvaBT()
    
    elif option.strip() == "b":
        state = [0] * n
        board = [[0 for x in range(n)] for y in range(n)]
        n_regine_alpinist.randomBoard(board, state)
        n_regine_alpinist.alg_alpinistului(board, state)

    else:
        print("Nu exista acea optiune!")
    