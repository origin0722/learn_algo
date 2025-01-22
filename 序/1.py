def nested_for_loop(n:int) -> str:
    res=""
    for i in range(1,n+1):
        for j in range(1,n+1):
            res +=f"({1},{j}),"
    return res