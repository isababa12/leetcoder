

var numJewelsInStones = function(jewels, stones) {

    var count = 0;

    for(let i = 0; i < stones.length; i++){
        if(jewels.includes(stones[i])){
            count++;
        }
    }
    return count
};
