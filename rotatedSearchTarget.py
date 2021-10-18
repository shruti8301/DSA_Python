from jovian.pythondsa import evaluate_test_case, evaluate_test_cases

def rotatedSearch(nums, target):
    if len(nums) == 0:
        return -1
    lowest = 0
    highest = len(nums) - 1
    while (lowest <= highest):
        middle = (lowest + highest) // 2
        if (nums[middle] == target):
            return middle
        if (nums[lowest] <= nums[middle]):
            if (target >= nums[lowest] and target < nums[middle]):
                highest = middle - 1
            else:
                lowest = middle + 1
        if (nums[middle] <= nums[highest]):
            if (target > nums[middle] and target <= nums[highest]):
                lowest = middle + 1
            else:
                highest = middle - 1
    return -1

tests = []

tests.append({
    'input': {
        'nums': [5,6,9,0,2,3,4],
        'target': 0
    },
    'output': 3
})

tests.append({
    'input': {
        'nums': [4,5,6,7,0,1,2],
        'target': 0
    },
    'output': 4
})

tests.append({
    'input': {
        'nums': [4,5,6,7,0,1,2],
        'target': 3
    },
    'output': -1
})

tests.append({
    'input': {
        'nums': [45,56,63,-5,0,3,4,12,23,44],
        'target': 45
    },
    'output': 0
})

tests.append({
    'input': {
        'nums': [5,6,9,12,13,2,3,4],
        'target': 2
    },
    'output': 5
})

tests.append({
    'input': {
        'nums': [0,2,3,4,5],
        'target': 0
    },
    'output': 0
})

tests.append({
    'input': {
        'nums': [2,3,4,5,0],
        'target': 0
    },
    'output': 4
})

tests.append({
    'input': {
        'nums': [30,0,5,6,9,13],
        'target': 6
    },
    'output': 3
})

tests.append({
    'input': {
        'nums': [0,2,3,4,5,6],
        'target': 0
    },
    'output': 0
})

tests.append({
    'input': {
        'nums': [],
        'target': 0
    },
    'output': -1
})

tests.append({
    'input': {
        'nums': [3],
        'target': 0
    },
    'output': -1
})

evaluate_test_cases (rotatedSearch, tests)