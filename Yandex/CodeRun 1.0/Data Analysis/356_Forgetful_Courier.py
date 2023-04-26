"""
Use Monte Carlo simulation to get assess the probability
"""
import sys
import random
# import matplotlib.pyplot as plt


def simulation(N, k):
    visited = [False for _ in range(N+1)]
    visited[0] = True
    now = 0
    while not visited[k]:
        direction = random.choice([-1, 1])
        now += direction
        if now == N+1:
            now = 0
        elif now == -1:  # never go to Lavka again
            now = N
        visited[now] = True

    if sum(visited) == N+1:
        return True
    else:
        return False





def main():
    N, k = map(int, input().split())

    num_simulations = 10000
    count_last = 0
    # list_temp = []
    for i in range(num_simulations):
        count_last += simulation(N, k)
        # if i > 100:
        #     list_temp.append(count_last/(i+1))

    print(count_last/num_simulations)
    # plt.plot(list_temp)
    # plt.show()


if __name__ == '__main__':
	main()