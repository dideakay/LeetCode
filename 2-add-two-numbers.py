# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        list1 = []
        list2 = []
        cur1 = l1
        cur2 = l2
        carry = False
        length = 0
        result = ListNode(0,None)
        resultCur = ListNode(0,None)
        while(cur1 and cur2) :

            curSum = cur1.val+cur2.val 
            
            if(carry):
                list1.append((curSum + 1) % 10)
                carry = False
                if(curSum + 1 - 10 >= 0):
                    carry = True
                
            else:
                list1.append(curSum % 10)
            
            if(curSum - 10 >= 0):
                carry = True
                
            length = length + 1   
            cur1 = cur1.next
            cur2 = cur2.next
            
            
            
        while(cur1):
            if(carry):
                list1.append((cur1.val + 1) % 10)
                carry = False
                if(cur1.val + 1 == 10):
                    carry = True
            else:
                list1.append(cur1.val % 10)
            cur1 = cur1.next
                
        while(cur2):
            if(carry):
                list1.append((cur2.val + 1) % 10)
                carry = False
                if(cur2.val + 1 == 10):
                    carry = True
            else:
                list1.append(cur2.val % 10)
            cur2 = cur2.next
            
        if(carry):   
            list1.append(1)
            
        
        resultCur = result
        
        for i in range(0, len(list1)-1):
            resultCur.val = list1[i]
            resultCur.next = ListNode(0,None)
            resultCur = resultCur.next
            
        resultCur.val = list1[len(list1)-1]
        
        return result
            
          
            
            
