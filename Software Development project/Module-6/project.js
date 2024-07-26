// // alert("hi")

// function handleDeposit(){
//     var inputvalue=document.getElementById("deposit_input").value;

//     var convertedinputvalue=convertTonumber(inputvalue);

//     var depositamount=document.getElementById("depositamount").innerText;
    
//     var convertedDepositvalue=convertTonumber(depositamount);

//     var sum=(convertedinputvalue + convertedDepositvalue);

//     // console.log(sum)

//     document.getElementById("depositamount").innerText = sum;

//     document.getElementById("deposit_input").value = "";

//     var totalAmount=document.getElementById("total-amount").innerText;

//     var convertedTotalamount=convertTonumber(totalAmount);

//     var total_sum= (convertedinputvalue + convertedTotalamount);

//     document.getElementById("total-amount").innerText = total_sum;




// }

// function convertTonumber(value){
//     return parseFloat(value);
// }

// function handleWithdraw()
// {
//     var inputvalue=document.getElementById("withdraw_input").value;

//     var convertedinputvalue=convertTonumber(inputvalue);

//     var withdrawAmount=document.getElementById("withdraw-amount").innerText;
    
//     var convertedWithdrawvalue=convertTonumber(withdrawAmount);

//     var sum=(convertedinputvalue + convertedWithdrawvalue);

//     // console.log(sum)

//     document.getElementById("withdraw-amount").innerText = sum;

//     document.getElementById("withdraw_input").value = "";

//     var totalAmount=document.getElementById("total-amount").innerText;

//     var convertedTotalamount=convertTonumber(totalAmount);

//     var total_sum= (convertedTotalamount - convertedinputvalue);

//     document.getElementById("total-amount").innerText = total_sum;

// }












// modify the above code into short and standard


function handleDeposit(){
    // var inputvalue=document.getElementById("deposit_input").value;

    var convertedinputvalue=Getconvertnumber("deposit_input","value")

    // var depositamount=document.getElementById("depositamount").innerText;
    
    var convertedDepositvalue=Getconvertnumber("depositamount","innerText");

    var sum=(convertedinputvalue + convertedDepositvalue);



    // document.getElementById("depositamount").innerText = sum;
    setInnertext("depositamount",sum)

    document.getElementById("deposit_input").value = "";

    convertedTotalamount=Getconvertnumber("total-amount","innerText")

    var total_sum= (convertedinputvalue + convertedTotalamount);

    // document.getElementById("total-amount").innerText = total_sum;
    setInnertext("total-amount",total_sum)



}

function Getconvertnumber(id,element){
    if (element =="innerText")
    {
        var values = document.getElementById(id).innerText;
        return parseFloat(values);
    }
    else
    {
        var values = document.getElementById(id).value;
        return parseFloat(values);
    }
}

function setInnertext(id,value){
    document.getElementById(id).innerText = value;

}

function handleWithdraw()
{
   

    var convertedinputvalue=Getconvertnumber("withdraw_input","value")

    
    
    var convertedWithdrawvalue=Getconvertnumber("withdraw-amount","innerText")

    var sum=(convertedinputvalue + convertedWithdrawvalue);

    // console.log(sum)

   
    setInnertext("withdraw-amount",sum)

    document.getElementById("withdraw_input").value = "";



    var convertedTotalamount=Getconvertnumber("total-amount","innerText")

    var total_sum= (convertedTotalamount - convertedinputvalue);

    
    setInnertext("total-amount",total_sum)

}



