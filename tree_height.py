# python3
class TreeDepth(object):
    def __init__(self, parents):
        self._parents = parents #all nodes pointing to their parents
        self._node_count = len(parents) #length of list
        self._max_height = 0
        self._heights = [None] * self._node_count

    def max_height(self):
        #iet cauri visiem elementu id, nolasot parenta atrašanās vietu un pierakstot zaru augstumus
        for id, parent in enumerate(self._parents):
            stack = []
            # saliekam stackā visus elementus sākot no id līdz root
            while parent != -1 and self._heights[id] is None: #kamēr nav root UN neeksistē augstums 
                stack.append(id) # gāžam iekšā stackā elementa id
                id, parent = parent, self._parents[parent] # ņemam elementa parentu
 
            # piešķiram pašreizējo augstumu
            if parent == -1:
                height = 1
            else:
                height = self._heights[id] #šajā brīdi agstums ir neieskaitot root

            # iztukšojam stacku sarakstot elementu augstumu   
            while stack:
                height += 1
                self._heights[stack.pop()] = height

            # pierakstam lielāko augstumu
            if self._max_height < height:
                self._max_height = height

        return self._max_height


def main():
    # implement input form keyboard and from files
    # let user input file name to use, don't allow file names with letter a
    # account for github input inprecision
    # input number of elements
    # input values in one variable, separate with space, split these values in an array

    nodes = 0

    inputChoice = input()
    if  inputChoice.lower()[0] == "i":
        input("input:")
        str = input()
        nodes = list(map(int, str.split()))

    elif inputChoice[0] == "F":
        #faila nosaukumam tiek pievienots relatīvais path, citādāk neizpildās testi
        file = open("test/" + input(), mode="r", encoding="utf-8")
        data = file.readlines()
        nodes = list(map(int, data[1].split()))
    
    # call the function and output it's result
    print(TreeDepth(nodes).max_height())

main()
