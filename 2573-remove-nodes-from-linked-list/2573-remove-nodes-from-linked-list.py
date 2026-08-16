# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Approach 1
        # stack=[]
        # current=head
        # while current:
        #     stack.append(current)
        #     current=current.next
        # current=stack.pop()
        # maximum=current.val
        # resultList=ListNode(maximum)
        # while stack:
        #     current=stack.pop()
        #     if current.val<maximum:
        #         continue
        #     else:
        #         newNode=ListNode(current.val)
        #         newNode.next=resultList
        #         resultList=newNode
        #         maximum=current.val
        # return resultList
        # Approach 2
        if head is None or head.next is None:
            return head
        nextNode=self.removeNodes(head.next)
        if head.val<nextNode.val:
            return nextNode
        head.next=nextNode
        return head
        