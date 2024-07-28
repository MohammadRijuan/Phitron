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


const square =nums.map(x=>(x*x))
console.log(square)