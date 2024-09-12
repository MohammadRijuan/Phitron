// js is a single threated syncronus language...it will work as a sequentially
// asyncronus will not work sequentially...like  1 2 3 4 .. 6 .. 8


console.log(1)
console.log(2)
console.log(3)
console.log(4)
name(5)
console.log(6)
console.log(7)
console.log(8)
console.log(9)
console.log(10)

function name(x){
    console.log(x)
}



// asyncronus behaviour
console.log(1)
console.log(2)
console.log(3)
console.log(4)
name(5)
console.log(6)
console.log(7)
console.log(8)
console.log(9)
console.log(10)

// fetch holo syncronus
function name(x){
    fetch('https://fakestoreapi.com/products/1')
            .then(res=>res.json())
            .then(json=>console.log(json))
}




console.log(1)
console.log(2)
console.log(3)
console.log(4)
name(5)
console.log(6)
console.log(7)
console.log(8)
console.log(9)
console.log(10)

function name(x){
    setTimeout(() => console.log(x));
}