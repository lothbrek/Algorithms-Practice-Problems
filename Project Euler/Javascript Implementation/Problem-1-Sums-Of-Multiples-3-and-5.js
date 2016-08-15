//Project Euler #1
//If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

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

var sum = 0;

for(var i = 0; i < 1000; i++)
{
    if (i %3 === 0 || i %5 === 0)
    {
        sum = sum + i;
    }

}

//output should be 233168
console.log(sum);