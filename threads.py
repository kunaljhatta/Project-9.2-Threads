import threading

ranges = [
        [10, 20],
        [1, 5],
        [70, 80],
        [27, 92],
        [0, 16]
        ]  
   
threads = []
result = [0] * len(ranges)

def main():     
    launch_threads()
    join_threads()
    display_results_and_sum()

def launch_threads():
    for i in range(len(ranges)):
        thread = threading.Thread(target=sum_range, args=(ranges[i][0], ranges[i][1], result, i))
        threads.append(thread)
        thread.start()
         
def display_results_and_sum():
    print(result)
    print(sum(result))

def join_threads():
    for t in threads:
        t.join()
        
def sum_range(start, end, result, index):
    result[index] = (end * (end + 1)) // 2 - (start * (start - 1)) // 2

if __name__ == "__main__":
    main()