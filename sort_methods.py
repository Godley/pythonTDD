def insertionSort(input):
    if input is None:
        raise BaseException("INVALID INPUT")
    elif len(input) < 2:
        return input
    elem = input[-1]
    first = input[0]
    input[0] = elem
    input[-1] = first
    for i in range(len(input)):
        for j in range(i, len(input)):
            if input[j] < input[i]:
                selected = input[j]
                swap = input[i]
                input[i] = selected
                input[j] = swap
    return input


def selectionSort(input):
    if input is None:
        raise BaseException("INVALID INPUT")
    elif len(input) < 2:
        return input
    mini = min(input)
    index = input.index(mini)
    first_elem = input[0]
    input[0] = mini
    input[index]=first_elem
    for i in range(1, len(input)-1):
        minim=min(input[i:])
        minim_in=input.index(minim)
        elem=input[i]
        input[i]=minim
        input[minim_in]=elem


    return input

def MergeSort(input):
    if input is None:
        raise BaseException("INVALID INPUT")
    elif len(input) < 2:
        return input
    split_point = int(len(input)/2)
    split1=input[:split_point]
    split2=input[split_point:]
    MergeSort(split1)
    MergeSort(split2)
    result=[]
    while len(split1)>0 or len(split2)>0:
        if len(split1) > 0 and len(split2) > 0:
            if split1[0]>split2[0]:
                result.append(split2[0])
                split2.pop(0)
            elif split2[0]>split1[0]:
                result.append(split1[0])
                split1.pop(0)
        elif len(split1)>0 and len(split2) is 0:
            result.append(split1[0])
            split1.pop(0)
        elif len(split1) is 0 and len(split2)>0:
            result.append(split2[0])
            split2.pop(0)
        if len(split1) > 0 and len(split2) > 0 and split1[0] == split2[0]:
            result.append(split1[0])
            result.append(split2[0])
            split1.pop(0)
            split2.pop(0)
    return result

def QuickSort(input):
    if input is None:
        raise BaseException("INVALID INPUT")
    elif len(input) < 2:
        return input
    pivot = input[0]
    seg1 =[]
    seg2=[]
    for i in range(1,len(input)):
        if input[i] > pivot:
            seg2.append(input[i])
        elif input[i] < pivot:
            seg1.append(input[i])
        elif input[i] == pivot:
            seg1.append(input[i])
    res_1=QuickSort(seg1)
    res_1.append(pivot)
    res_2=QuickSort(seg2)
    return res_1 + res_2

def BubbleSort(input):
    if input is None:
        raise BaseException("INVALID INPUT")
    if len(input) < 2:
        return input

    swaps = 0
    while swaps != -1:
        for i in range(len(input)):
            if i != len(input)-1:
                if input[i] > input[i+1]:
                    elem = input[i+1]
                    input[i+1] = input[i]
                    input[i] = elem
                    swaps=0
                else:
                    swaps=-1
    return input
