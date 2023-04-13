var reverseLinkedList = function(head){

    var prev = null
    var current = head

    while(current.next !== null){
        temp = current.next
        current.next = prev
        prev = current
        current = temp
    }
    return prev
}
