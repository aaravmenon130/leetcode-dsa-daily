#https://leetcode.com/problems/build-an-array-with-stack-operations/?envType=problem-list-v2&envId=dsa-linear-shoal-stack
class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        output = []
        current_array = []
        pointer = -1

        for i in range(1, n + 1):

            if current_array == target:
                return output
                break
            current_array.append(i)
            #print('push')
            output.append('Push')
            pointer += 1

            if current_array[pointer] != target[pointer]:
                yea = current_array.pop()
                pointer -= 1
                #print('pop')
                output.append('Pop')
            
        return output
