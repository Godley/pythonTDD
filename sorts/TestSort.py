import unittest


class TestSort(unittest.TestCase):
    def setUp(self):
        self.valid_data = [1,5,20,30,5,0,7,6]
        self.one_input = [3]
        self.empty_data = []
        self.sorts = [self.insertionSort,self.selectionSort,self.MergeSort, self.QuickSort, self.BubbleSort]

    def testEmpty(self):
        for method in self.sorts:
            self.assertEquals(method(self.empty_data), self.empty_data, "Error: empty test failed on method: "+str(method))

    def testOneInput(self):
        for method in self.sorts:
            self.assertEqual(method(self.one_input), self.one_input, "Error: one input failed on method: "+str(method))

    def testNone(self):
        for method in self.sorts:
            self.assertRaises(BaseException, method, None, "Error: giving no data does not throw an exception in method: "+str(method))

    def testSorts(self):
        expected = [0,1,5,5,6,7,20,30]
        for method in self.sorts:
            self.assertEqual(method(self.valid_data),expected, "Error: sorting algorithm does not run as expected: "+str(method))


    def insertionSort(self, input):
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


    def selectionSort(self, input):
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

    def MergeSort(self, input):
        if input is None:
            raise BaseException("INVALID INPUT")
        elif len(input) < 2:
            return input
        split = int(len(input)/2)
        list_1=input[:split]
        list_2=input[split:]
        self.MergeSort(list_1)
        self.MergeSort(list_2)
        result=[]
        while len(list_1)>0 or len(list_2)>0:
            if len(list_1) > 0 and len(list_2) > 0:
                if list_1[0]>list_2[0]:
                    result.append(list_2[0])
                    list_2.pop(0)
                elif list_2[0]>list_1[0]:
                    result.append(list_1[0])
                    list_1.pop(0)
            elif len(list_1)>0 and len(list_2) is 0:
                result.append(list_1[0])
                list_1.pop(0)
            elif len(list_1) is 0 and len(list_2)>0:
                result.append(list_2[0])
                list_2.pop(0)
            if len(list_1) > 0 and len(list_2) > 0 and list_1[0] == list_2[0]:
                result.append(list_1[0])
                result.append(list_2[0])
                list_1.pop(0)
                list_2.pop(0)
        return result

    def QuickSort(self, input):
        if input is None:
            raise BaseException("INVALID INPUT")
        elif len(input) < 2:
            return input
        pivot = input[0]
        list1 =[]
        list2=[]
        for i in range(1,len(input)):
            if input[i] > pivot:
                list2.append(input[i])
            elif input[i] < pivot:
                list1.append(input[i])
            elif input[i] == pivot:
                list1.append(input[i])
        res_1=self.QuickSort(list1)
        res_1.append(pivot)
        res_2=self.QuickSort(list2)
        return res_1 + res_2

    def BubbleSort(self, input):
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
if __name__ == '__main__':
    unittest.main()