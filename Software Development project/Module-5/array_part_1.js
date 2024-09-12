var friends=["Rijuan","Monju","sifat","abid","fahad"]

console.log(friends)
console.log(friends[0])
console.log(friends[1])
console.log(friends[2])
console.log(friends.length)


friends.push("Nibraj")
console.log(friends)

friends.pop()
console.log(friends)

// samner element badh dibe
friends.shift()
console.log(friends)

// samner element remain teke jbe
friends.unshift()
console.log(friends)

//it works and added in the last position...then why it does not work in frnds? 
console.log(['a','b'].concat('c'))

friends.concat('abc')
console.log(friends)

// reverse array
friends.reverse()
console.log(friends)

// slicing
console.log(friends.slice(2,3))

// find the index
console.log(friends.indexOf('sifat'))





