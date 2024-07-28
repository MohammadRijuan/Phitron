// array destructuring

const numbers= [1,2,3,4,5,6,7,8,9];

// if i mess the position of object it will serial it again
const [first,second] = numbers;
console.log(first,second)


// object destructuring

const obj = {
    name: "Rijuan",
    age : 20,
    friends : 21,
    github : "yes",
    status: "single"
};

const {age} =obj;
const {name,status} =obj;

console.log(age)
console.log(name,status)


// nested obj destructuring in an array

const test = [
    {
        name: "Rijuan",
        age : 20,
        friends : ["rahim","karim",{
            name : "hii"
        }],
        github : "yes",
        status: "single"
    },
    {},
    {}
];

console.log(test)
console.log(test.length)
console.log(test[0].friends)
console.log(test[0].friends[1])
console.log(test[0].friends[2].name)
