
const searchbar=()=>{
   let filter=document.querySelector('#search').value.toLowerCase();
 
   const cname=document.getElementsByClassName('name');
   const cards=document.getElementsByClassName('person');

    for (let i = 0; i < cards.length; i++) {
 
       let value=cname[i].innerHTML.toLowerCase();
          if(value.indexOf(filter)>-1){
            cards[i].style.display="";
            
          }else{
             cards[i].style.display="none";
          }
       }
}
// const searchbar=()=>{
//    const cards=document.getElementById('person')
//    let filter=document.querySelector("#search").ariaValueMax.toLowerCase();
//    const cname=document.getElementsByClassName('name');
//    fetch("https://jsonplaceholder.typicode.com/users").then(res=>res.json()).then(data=>{
//       for (let i = 0; i < data.length; i++) {
//         console.log(data[i].name);
   
//         cname[i].innerHTML=data[i].name;
//         let value=data[i].name.toLowerCase();
//    if(value.indexOf(filter)>-1){
//       cards[i].style.display=""
//    }else{
//       cards[i].style.display="none";
//    }
        
//       }
//    });
//    console.log((data));
// }



//   fetch(`https://api.openweathermap.org/data/2.5/weather?q=Pune&units=metric&appid=229d4742c2729ac4d50b9637396abf79`)
//   .then(res=>res.json())
//   .then(data=>console.log(data));