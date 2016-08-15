//Finds the sum of all fibonacci sequences that are even sequences below 4 million.

<div id="console-log"></div>
.console-line
{
    font-family: monospace;
    margin: 2px;
}
var consoleLine = "<p class=\"console-line\"></p>";
 
console = {
    log: function (text) {
        $("#console-log").append($(consoleLine).html(text));
    }
};

function fibo(index,n)
{
    if (n == 0)
        return 1;
    if (n == 1)
        return 2;
    
    return index[n-1]+index[n-2];
}

var sum = 0;
var max = 4000000;
var index = [];

for(var i = 0; i < max; i++)
{
    index[i] = fib(index, i);
    if(index[i] > max)
    {
        break;
    }
    
    if(index[i] % 2 === 0) 
    {
        sum += index[i];
    }
}

console.log(sum);
