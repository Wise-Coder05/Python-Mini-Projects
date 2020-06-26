

#
# Complete the simpleArraySum function below.
#

# Write your code here.
def simpleArraySum(n, ar):
       sum = 0 
       i = 0 
       while i < n :
              sum += ar[i]
              i += 1
       return sum


if __name__ == '__main__':

       n = int(input())

       ar = list(map(int, input().rstrip().split()))

       result = simpleArraySum(n, ar)

       print(str(result) + '\n')

    
