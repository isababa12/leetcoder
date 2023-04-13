def addTwoNumbers(l1, l2):

    carry = 0
    result = ListNode(0)
    pointer = result

    while l1 or l2 or carry:
        first = l1.val if l1 else 0
        second = l2.val if l2 else 0

        sum = first + second + carry
        num = sum % 10
        carry = sum //10

        pointer.next = ListNode(num)
        pointer = pointer.next

        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
    return result.next

print(addTwoNumbers([2,4,3],[5,6,4]))
