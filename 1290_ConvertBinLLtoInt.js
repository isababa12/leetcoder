var getDecimalValue = function(head) {

    var num = head.val;

    while(head.next!==null){

        num = num * 2 + head.next.val;
        head = head.next;

    }
    return num;
};
