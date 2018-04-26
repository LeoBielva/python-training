#Write a function that takes in a list of integers and returns True if it contains 007 in orde

def spy_game(nums):
        code = [0, 0, 7, 'x']
        for num in nums:
            if num == code[0]:
                code.pop(0)
        return len(code) == 1





print(spy_game([0,1,2,3,7]))
