class Solution(object):
    def isPalindrome(self, x):

        x_str = str(x)
        x_list = []
        new_x_list = []

        for i in x_str:
            x_list.append(i)

        for j in range(len(x_str)-1, -1, -1):
            new_x_list.append(x_str[j])

        if new_x_list == x_list:
            return True

        return False

