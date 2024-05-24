import matplotlib.pyplot as plt

def printSolution(board, n):
    for i in range(n):
        for j in range(n):
            print(board[i][j], end=' ')
        print()

def plot_chart(table_sizes, solving_times, solving_times_alt):
    plt.plot(table_sizes, solving_times, label='Backtracking')
    plt.plot(table_sizes, solving_times_alt, label='Alg Alpinistului', linestyle='--')
    plt.xlabel('Complexitate')
    plt.ylabel('Timp (s)')
    plt.xticks(range(len(table_sizes)), table_sizes)
    plt.grid()
    plt.legend()
    plt.show()