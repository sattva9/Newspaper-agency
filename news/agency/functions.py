import math


def partition_list(a, k):
    #check degenerate conditions
    if k <= 1: return [a]
    if k >= len(a): return [[x] for x in a]
    partition_between = []
    for i in range(k-1):
        partition_between.append((i+1)*len(a)/k)
    average_height = float(sum(a))/k
    best_score = None
    best_partitions = None
    count = 0
    no_improvements_count = 0
    while True:
        partitions = []
        index = 0
        for div in partition_between:
            partitions.append(a[index:int(div)])
            index = int(div)
        partitions.append(a[index:])
        worst_height_diff = 0
        worst_partition_index = -1
        for p in partitions:
            height_diff = average_height - sum(p)
            if abs(height_diff) > abs(worst_height_diff):
                worst_height_diff = height_diff
                worst_partition_index = partitions.index(p)
        if best_score is None or abs(worst_height_diff) < best_score:
            best_score = abs(worst_height_diff)
            best_partitions = partitions
            no_improvements_count = 0
        else:
            no_improvements_count += 1
        if worst_height_diff == 0 or no_improvements_count > 5 or count > 100:
            return best_partitions
        count += 1
        if worst_partition_index == 0:   
            if worst_height_diff < 0: partition_between[0] -= 1   
            else: partition_between[0] += 1   
        elif worst_partition_index == len(partitions)-1:
            if worst_height_diff < 0: partition_between[-1] += 1
            else: partition_between[-1] -= 1   
        else:   
            left_bound = worst_partition_index - 1
            right_bound = worst_partition_index   
            if worst_height_diff < 0:   
                if sum(partitions[worst_partition_index-1]) > sum(partitions[worst_partition_index+1]):
                    partition_between[right_bound] -= 1
                else:
                    partition_between[left_bound] += 1
            else:   
                if sum(partitions[worst_partition_index-1]) > sum(partitions[worst_partition_index+1]):
                    partition_between[left_bound] -= 1
                else:   
                    partition_between[right_bound] += 1

