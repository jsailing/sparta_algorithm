import heapq

ramen_stock = 4
supply_dates = [4, 10, 15]
supply_supplies = [20, 5, 10]
supply_recover_k = 30


def get_minimum_count_of_overseas_supply(stock, dates, supplies, k):
    count = 0
    next_index = 0
    max_heap = []

    while stock < k:
        for i in range(next_index, len(dates)):
            print(i, dates[i], supplies[i])
            if dates[i] <= stock:
                heapq.heappush(max_heap, -supplies[i])
            else:
                next_index = i
                break

        count += 1
        print("max_heap", max_heap)
        stock += -heapq.heappop(max_heap)
        print("stock is", stock)
        max_heap.clear()

    return count


print(get_minimum_count_of_overseas_supply(ramen_stock, supply_dates, supply_supplies, supply_recover_k))