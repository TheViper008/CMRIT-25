def merge_sort(nlist):
    lefthalf = []
    righthalf = []
    if len(nlist)>1:
        mid = len(nlist)//2
        lefthalf = nlist[:mid]
        righthalf = nlist[mid:]
        merge_sort(lefthalf)
        merge_sort(righthalf)
    
    i = j = k = 0
    while i < len(lefthalf) and j < len(righthalf):
        if lefthalf[i] < righthalf[j]:
            nlist[k] = lefthalf[i]
            i = i+1
        else:
            nlist[k] = righthalf[j]
            j = j+ 1
        k = k+1
    while i <len(lefthalf):
            nlist[k] = lefthalf[i]
            i = i+1
            k = k+1
    while j < len(righthalf):
         nlist[k] = righthalf[j]
         j = j + 1
    print("Merging ",nlist)

merge_sort(list(map(int,input("Enter the elements:").split()))) 
