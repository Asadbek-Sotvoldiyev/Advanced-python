def likee(arr):
    if not arr:
        return "Bu hech kimga yoqmaydi"
    elif len(arr)==1:
        return f"Bu {arr[0]}ga yoqadi"
    elif len(arr)==2:
        return f"{arr[0]} va {arr[1]}ga yoqadi"
    elif len(arr)==3:
        return f"{arr[0]},{arr[1]} va {arr[2]}ga yoqadi"
    else:
        return f"{arr[0]},{arr[1]} va yana {len(arr)-2} kishiga yoqadi"

print(likee(['Asadbek', 'Boburjon', 'Yahyobek', 'Murodali']))