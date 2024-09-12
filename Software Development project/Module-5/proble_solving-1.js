1.
var num= 55

if (num%2==0)
{
    console.log("Yes,it is even")
}
else
{
    console.log("No,its odd")
}


2.
var nums=[2,9,4,1,5,7,11,3,14,10,12]

console.log(nums.sort(function(a,b)
{
    return a-b
}))


// Step 1: Create the array with messy numbers
let messyArray = [12, 5, 8, 19, 1, 20, 6, 17, 3, 10, 4, 18, 7, 9, 2, 15, 11, 14, 13, 16];

// Step 2: Sort the array
messyArray.sort((a, b) => a - b);

// Output the sorted array
console.log(messyArray);


3.
var friends=["Rijuan","Monju","sifat","abid","fahad"]

var largename=friends[0]

for (var i=0; i< friends.length ;i++)
{
    var element =friends[i]

    if (largename.length < element.length)
    {
        largename=element
    }
}
console.log(largename)



let duplicateArray = [2, 5, 8, 1, 1, 20, 6, 17, 3, 10, 4, 5, 7, 9, 2, 1, 9, 14, 13, 16];

duplicateArray.filter()