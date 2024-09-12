var h1=document.getElementsByTagName("h1")

console.log(h1);

var title =(document.getElementById("title").style.color = "red");

// document.getElementById("title").style.removeProperty("color")
console.log(title);

var child = document.getElementsByClassName("child")

console.log(child)
console.log(child[0])


// how to get ATTRIBUTE

var img= document.getElementById("img");

console.log(img.getAttribute("src"));

// how to set attribute

img.setAttribute("alt","Profilepicture")
console.log(img.getAttribute("alt"));


// classlist

img.classList.add("testclass");
console.log(img)

// how to get paragraph text
var hero= document.getElementById("hero")
console.log(hero.innerText)

// how to get input
var input = document.getElementById("input")
console.log(input.value);

// input type
var input = document.getElementById("input").value
console.log(typeof input);

// HOW TO GET INNER div file

var parent=document.getElementById("parent").innerHTML;
console.log(parent)

// how to get our child nodes from our parent div
var testdiv=document.getElementsByClassName("test")
console.log(testdiv[0].childNodes[1])

// to get parent node from child node
console.log(testdiv[0].childNodes[1].parentNode.parentNode.parentNode)

// how to create element using js and append ant text or file bla bla

// var newdiv=document.getElementById("newdiv")
// var p=document.createElement("p")
// p.innerText="notun ami";
// newdiv.appendChild(p)


function createel(){
    var p=document.createElement("p")
    p.innerText="notun ami";
    newdiv.appendChild(p)
}

createel()

// create add eventlistener

document.getElementById("submit-btn").addEventListener("click",function(e)
{
    console.log("yes boss")
    // createel()
    var inputvalue=document.getElementById("input").value;
    console.log(inputvalue)
});

// on change event

document.getElementById("input").addEventListener("blur",inputChange)

function inputchange(e){
    console.log("hellp");
};

// document.getElementById("input").addEventListener("blur",function (e){
//     console.log(e.target.value);
// });


