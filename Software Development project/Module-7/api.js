// API - Application Programming Interface
// A way to communicate between client and server
// how to fetch ur api
// this data will provide backend developer and frontend developer will shows it on ui
fetch("https://fakestoreapi.com/products/1")
    // .then((res)=>console.log(res))
    .then((res)=>res.json())
    .then((data) => {
        console.log(data)
    })
    // if it deleted for once ... then shows it like an error or handling error
    .catch((err) => {
        console.log(err);
    });