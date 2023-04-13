var maximumWealth = function(accounts) {
    let max = 0;
    for (let i = 0; i < accounts.length; i++) {
        let result = 0;
        accounts[i].map(x => result += x);
            if (result > max) {
                max = result;
            };
    };
    return max
};
