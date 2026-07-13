function add(a,b){
    return a+b;
}
console.log(add(2,3));

function changeText(){
    document.getElementById("Text").innerText = "Text changed";
}
let heading = document.querySelector("#title")
heading.innerText="welcome Student"

document.getElementById("myBtn").addEventListener("click",function(){
    document.getElementById("msg").innerText="Button Clicked!";
});