from numpy import double
import n_regine_bt
import n_regine_alpinist
import n_regine_alg_genetic
import comis_voiajor_bt
import comis_voiajor_cel_mai_apropiat_vecin
import utility_functions
import matplotlib.pyplot as plt
from datetime import datetime

#TODO: measure the time for all algorithms and plot the 2 travelling salesman ones into another


while True:
    input()
    print("""
    a. Problema celor N regine (backtracking recursiv)
    b. Problema celor N regine (alg. alpinistului)
    c. Problema celor N regine (alg. genetic)
    d. Plotare grafice problema celor N regine
    e. Problema comis-voiajorului (backtracking recursiv)
    f. Problema comis-voiajorului (alg. celui mai apropiat vecin)
    g. Plotare grafice problema comis-voiajorului
    i. Info
    q. Exit

    Alegeti o optiune:
          
""")
    
    option = input()

    if option.strip() == "q":
        break

    elif option.strip() == "i":
        #update later
        print("Acest program a fost creat de Stamate Raluca din grupa 3132a")

    elif option.strip() == "a":
        n = int(input("Marimea tablei de sah: "))
        board_bt = n_regine_bt.BTChess(n)
        start_time_bt = datetime.now()
        board_bt.rezolvaBT()
        end_time_bt = (datetime.now() - start_time_bt).microseconds / 1000
        f = open('n_regine_grafic.txt', 'a')
        f.write(f"{n}x{n} bt {end_time_bt}\n")
        f.close()
    
    elif option.strip() == "b":
        n = int(input("Marimea tablei de sah: "))
        state = [0] * n
        alpinist_board = n_regine_alpinist.AlpinistChess(n)
        alpinist_board.randomBoard(state)
        start_time_alpinist = datetime.now()
        alpinist_board.alg_alpinistului(state)
        end_time_alpinist = (datetime.now() - start_time_alpinist).microseconds / 1000
        f = open('n_regine_grafic.txt', 'a')
        f.write(f"{n}x{n} alpinist {end_time_alpinist}\n")
        f.close()
    
    elif option.strip() == "c":
        n = int(input("Marimea tablei de sah: "))
        ga_board = n_regine_alg_genetic.GAChess(n)
        start_time_ga = datetime.now()
        solution = ga_board.solveGA()
        end_time_ga = (datetime.now() - start_time_ga).microseconds / 1000
        ga_board.printSolution(solution)
        f = open('n_regine_grafic.txt', 'a')
        f.write(f"{n}x{n} genetic {end_time_ga}\n")
        f.close()

    elif option.strip() == "d":
        #for the chart
        table_sizes = []
        solving_times = []
        labels = []
        f = open('n_regine_grafic.txt', 'r')
        lines = f.readlines()
        f.close()
        for line in lines:
            table_size, label, solving_time = line.split()
            solving_time = double(solving_time)
            if table_size not in table_sizes:
                table_sizes.append(table_size)
            if label not in labels:
                labels.append(label)
            solving_times.append(solving_time)
            
        print(table_sizes)
        print(solving_times)
        print(labels)
        aux = solving_times
        
        #for each algorithm    
        for i in range(len(labels)):
            #luam cate 5, pentru fiecare marime a tablei
            #8x8 12x12 15x15 20x20 25x25
            solving_time = solving_times[0:len(table_sizes)]
            print(solving_time)
            plt.plot(table_sizes, solving_time, label=labels[i])
            solving_times = solving_times[len(table_sizes):]
        plt.xlabel('Complexitate')
        plt.ylabel('Timp (s)')
        plt.xticks(range(len(table_sizes)), table_sizes)
        plt.grid()
        plt.legend()
        plt.show()
        
    elif option.strip() == "e":
        cv = comis_voiajor_bt.ComisVoiajor.read_graph_from_file('graf.txt')
        start_time_cv = datetime.now()
        min_cost, shortest_path = cv.find_min_cost_path()
        end_time_cv = (datetime.now() - start_time_cv).microseconds / 1000
        print(f"Drumul cel mai scurt este {shortest_path}, costul sau fiind {min_cost}")
        f = open('comis_voiajor_grafic.txt', 'a')
        f.write(f"bt {len(cv.mat_cost)} {end_time_cv} \n")
        f.close()
        
    elif option.strip() == "f":
        ncv = comis_voiajor_cel_mai_apropiat_vecin.NComisVoiajor.read_graph_from_file('graf.txt')
        start_time_ncv = datetime.now()
        min_cost, shortest_path = ncv.comis_voiajor_cal_mai_apropiat_vecin()
        end_time_ncv = (datetime.now() - start_time_ncv).microseconds / 1000
        print(f"Drumul cel mai scurt este {shortest_path}, costul sau fiind {min_cost}")
        f = open('comis_voiajor_grafic.txt', 'a')
        f.write(f"nearest_neighbor {len(ncv.mat_cost)} {end_time_ncv} \n")
        f.close()

    else:
        print("Nu exista acea optiune!")
    