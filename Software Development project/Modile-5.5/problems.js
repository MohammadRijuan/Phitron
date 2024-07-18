// 1 .Sum of Array Elements:

function sumArray(arr) {
    let sum = 0;
    for (let i = 0; i < arr.length; i++) {
        sum += arr[i];
    }
    return sum;
}

// 2. Find Maximum Value:

function findMax(arr) {
    if (arr.length === 0) return undefined;
    let max = arr[0];
    for (let i = 1; i < arr.length; i++) {
        if (arr[i] > max) {
            max = arr[i];
        }
    }
    return max;
}


// 3. Filter Even Numbers:

function filterEvenNumbers(arr) {
    let result = [];
    for (let i = 0; i < arr.length; i++) {
        if (arr[i] % 2 === 0) {
            result.push(arr[i]);
        }
    }
    return result;
}

// 4. Reverse String:

function reverseString(str) {
    let reversed = '';
    for (let i = str.length - 1; i >= 0; i--) {
        reversed += str[i];
    }
    return reversed;
}


// 5. Check Prime Numbers:

function isPrime(num) {
    if (num <= 1) return false;
    for (let i = 2; i < num; i++) {
        if (num % i === 0) return false;
    }
    return true;
}


// 6. Remove Duplicates:

function removeDuplicates(arr) {
    let uniqueElements = [];
    for (let i = 0; i < arr.length; i++) {
        if (!uniqueElements.includes(arr[i])) {
            uniqueElements.push(arr[i]);
        }
    }
    return uniqueElements;
}

// 7. FizzBuzz:

function fizzBuzz() {
    for (let i = 1; i <= 100; i++) {
        if (i % 15 === 0) {
            console.log('FizzBuzz');
        } else if (i % 3 === 0) {
            console.log('Fizz');
        } else if (i % 5 === 0) {
            console.log('Buzz');
        } else {
            console.log(i);
        }
    }
}

// 8. Factorial Calculation:

function factorial(num) {
    if (num < 0) return undefined;
    let result = 1;
    for (let i = 1; i <= num; i++) {
        result += i;
    }
    return result;
}

// 9. Check Palindrome:

function isPalindrome(str) {
    let reversed = '';
    for (let i = str.length - 1; i >= 0; i--) {
        reversed += str[i];
    }
    return str === reversed;
}

// 10. Find Common Elements:

function findCommonElements(arr1, arr2) {
    let commonElements = [];
    for (let i = 0; i < arr1.length; i++) {
        if (arr2.includes(arr1[i]) && !commonElements.includes(arr1[i])) {
            commonElements.push(arr1[i]);
        }
    }
    return commonElements;
}




