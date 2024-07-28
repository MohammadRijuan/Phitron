// In the context of ES6 (ECMAScript 2015 or ES6), there isn't a direct concept of "attributes" in the sense used in HTML or certain object-oriented programming paradigms.

// we can declare variable in the following way

// var is functional scope
var s="ab";

// let and cond const are block scope
let a="abc";
const x="abcd";


// --------- here is a beautiful example of these -------- 

// functional scope which is (var) here u can get the output outside the condition
function name()
{
    if (true)
    {
        var x="hello"
    }
    console.log(x);
}

console.log(name());


// block scope (let) and (const)
// here u cannot get the ans outside the condition what functional scope can do but if u wanna get ans then u have to call output inside the condition

function name()
{
    if (true)
    {
        let x="hello";
        // const x="hello"
        console.log(x)
    }
    // console.log(x);  this one will not work here
}

console.log(name());





// but here is little bit difference between const and let
// let can be reinitialixed but const will be fixed cannot be reinitialized

// --- let ---

let names="rijuan"

names="monju"

console.log(names) // u will get monju here

// --- const ---
// const namess="rijuan"

// namess="monju"

// console.log(namess) u will not get aNS




// ----------------------
// template string or dynamic string
const test ="Rijuan"
//dynamic string
const abc='Monju ${test}'

console.log(abc);


const NUM =[1,2,3,4,5,6,7,8,9]

const newarray = ["rahim","karim",...NUM]
console.log(newarray)

//only element of an array
console.log(...NUM)
console.log(Math.max(...NUM)) //the max value of an array




