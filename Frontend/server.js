var VIDEO = document.getElementById("video");
var verification_container = document.getElementById("verification_container");

function playVideo(){
    navigator.getUserMedia({video:{}}, (stream)=>{
        VIDEO.srcObject = stream;
    }, (err)=>{
        console.log(err);
    });
}

function whiteall(){
    var list = document.querySelectorAll(".vote_btn");
    for(let i=0; i<list.length; i++){
        list[i].parentNode.parentNode.style.background="#fff";
    }
}
function count_me(cid){
    whiteall();
    document.getElementById("cid_number").value = cid;
    document.getElementById(cid).parentNode.parentNode.style.background="#0f0";
    verification_container.style.display = "block";
    playVideo();
}

document.querySelector("#snap").addEventListener("click", function(){   
    var canvas = document.getElementById("canvas");
    var ctx = canvas.getContext("2d");
    ctx.drawImage(VIDEO, 0, 38, 300, 225);
    document.getElementById("submit_vote").style.display = "inline-block";
});