

# def main():
# 	count = 0
# 	recursive(1, 10)


# def recursive(num):
# 	if(num == 1):
# 		newNum = 2
# 		return newNum
# 	else:
# 		newNum = (num + num-1)
# 	print(newNum)
# 	recursive(newNum)

# 1 1 2 3 5 8 13...
def recursive(num):
    if num == 1:
        return 1
    if num == 2:
        return 1
    else:
        return recursive(num - 1) + recursive(num - 2)

print(recursive(5))