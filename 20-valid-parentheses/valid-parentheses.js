let isValid = function(s) {
    let stack = [];
    let map = {
        ')': '(',
        ']': '[',
        '}': '{'
    };

    for (let ch of s) {
        if (ch === '(' || ch === '[' || ch === '{') {
            stack.push(ch);
        } else {
            if (stack.pop() !== map[ch]) {
                return false;
            }
        }
    }

    return stack.length === 0;
};
