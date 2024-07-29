const getData = new Promise(function (resolve ,reject) {
    return resolve(20);
});

getData.then(data => console.log(data))

const getsData = new Promise(function (resolve ,reject) {
    return reject("no data found");
});

getsData.then(data => console.log(data)).catch((err) => console.log(err));
    

fetch("https://fakestoreapi.com/products/1")
      .then((res) => res.json())
          .then((data) => console.log(data))
          .catch(err => console.log(err));

//  in asyncronus way

const loadData = async() => {
    const response = await fetch("https://fakestoreapi.com/products/1")
    // console.log(response.json());
    const data=await response.json(); //await use korte hbe nahole data pending obostay thakbe
    console.log(data);
};

loadData();

// if promise got rejected then how we handle it
const loadsData = async() => {
    try{
        const response = await fetch("https://fakestoreapi.com/products/1")
    // console.log(response.json());
    const data=await response.json(); //await use korte hbe nahole data pending obostay thakbe
    console.log(data);
    } catch {
        (err) => {
            console.log(err);
        };
    }
};

loadsData();


