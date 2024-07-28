function test(){
    return "hello world"
}

const result =test();

console.log(result);


// arrow function 
// if in single line equation u can return without calling return
const test2 = () => 2*2 ;
console.log(test2());

// if it in two line equation then u have to use return 
const test3 = () => {
    console.log("yes boss");
    return "bro"
};
console.log(test3());