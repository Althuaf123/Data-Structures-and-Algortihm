def function_one(n):
    if n < 0:
        return
    print(n)
    function_two(n-1)
    
def function_two(n):
    if n < 0:
        return
    print(n)
    function_one(n-1)

n = int(input('Enter a number: '))
# function_one(n)
function_two(n)