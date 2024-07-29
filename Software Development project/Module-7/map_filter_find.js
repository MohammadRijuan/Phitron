// map
// proti ta element ke niye kicu korbe, new ekta array return korbe

// filter
// kicu conditions dewa thakbe ,sei onusare element ke nibe and r kicu element ke nibe na..atao ekta array return korbe

// find
// conditions jodi onek gulo element puron kore tahole sudu 1st conditions e puro element ke return korbe..r kicu na parle undefined return korbe


const nums=[2,2];

let temp=[];

for (let i=0;i<nums.length;i++)
{
    const element=nums[i];
    const square = element*element;
    temp.push(square);
}
console.log(temp);

// using map
const square =nums.map(x=>(x*x))
console.log(square)



// filter 

const product=[
    {name: "samsung",price : 12000, color : "Golden"},
    {name: "samsung A20",price : 11000, color : "black"},
    {name: "macbook",price : 125000, color : "silver"},
    {name: "iphone x",price : 20000, color : "platinum"},
];

const result = product.filter((pd) => pd.color != "black");
console.log(result)


// find
const result2 = product.find((pd) => pd.color == "black");
console.log(result2);


// using forEach to see all the object with dynamic value
const productContainer = document.getElementById("product-container");
const result3 = product.forEach((product) => {
    console.log(product);
    const h1 = document.createElement("h1");
    h1.innerText = product.name;
    productContainer.appendChild(h1);

});












