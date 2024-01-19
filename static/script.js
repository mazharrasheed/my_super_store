
console.log("dfsdfdffd")

//  let pera=document.querySelector("#fact")

//  console.log(pera)

const URL= "jasondata"

const factpara=document.querySelector("#fact")
factpara.innerHTML="fgfgret6546566"
const div1=document.querySelector('#div1')
const btn=document.querySelector("#btn")

const getfacts= async()=>{
    let response=await fetch(URL);
    console.log(response); // Json formate
    // let data=await response.json(); // java script formate
    // console.log(data)
    div1.innerHTML=response
    // console.log(data[0].text);
    // factpara.innerHTML=data[0].text;
}

let getdata=()=>{
    div1.innerHTML='dfgrsdxxcczxs'
}

btn.addEventListener('click',getfacts);
btn.onclick=getdata 
