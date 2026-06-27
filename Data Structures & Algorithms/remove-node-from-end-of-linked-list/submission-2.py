# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next==None:
            return None
        size=0
        temp=head
        while temp:
            size+=1
            temp=temp.next
        temp1=head
        if size==n:
            temp=head.next
            head=temp
            
        for i in range(1,size-(n)):
            temp1=temp1.next
        if temp1.next.next==None:
            temp1.next=None
        else:
            temp1.next=temp1.next.next
        return head
        
        