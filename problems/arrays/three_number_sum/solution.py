def three_number_sum(array, targetSum):
    final = []
    sorted = array.copy()
    sorted.sort()

    for i in range(0, len(array)):
        left = i+1
        right = len(array)-1
        while left < right:
            currentSum = sorted[i] + sorted[left] + sorted[right]
            if currentSum == targetSum:
                final.append([sorted[i], sorted[left], sorted[right]])
                right -=1
                left+=1
            elif currentSum > targetSum:
               right -=1
            elif currentSum < targetSum:
                left +=1
    return final
