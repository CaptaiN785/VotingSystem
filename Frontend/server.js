var video = document.getElementById("video");
var verification_container = document.getElementById("verification_container");

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
    loadModels();
}

function loadModels(){
    Promise.all([
        faceapi.nets.tinyFaceDetector.loadFromUri("models"),
        faceapi.nets.faceRecognitionNet.loadFromUri("models"),
        faceapi.nets.faceLandmark68Net.loadFromUri("models"),
        faceapi.nets.ssdMobilenetv1.loadFromUri("models")
    ]).then(start);
}

function start(){
    playvideo();
}
function playvideo(){
    navigator.getUserMedia({video:{}}, (stream)=>{
        video.srcObject = stream;
    }, (err)=>{
        console.log(err);
    });
    recognizeFaces();
}
async function recognizeFaces() {

    const labeledDescriptors = await loadLabeledImages()
    const faceMatcher = new faceapi.FaceMatcher(labeledDescriptors, 0.7)


    document.getElementById("confirm_label").style.display = "block";
    video.addEventListener('play', async () => {
        var timer = setInterval(async () => {
            const detections = await faceapi.detectAllFaces(video).withFaceLandmarks().withFaceDescriptors()

            const results = detections.map((d) => {
                return faceMatcher.findBestMatch(d.descriptor)
            });

            if(results.length > 0){ // if match is greater than 60% then it will recognize.
                if(results[0]["_distance"] >= 0.6){
                    console.log(results[0]["_distance"]);
                    console.log("Matched");
                    document.getElementById("submit_vote").style.display = "block";
                    clearInterval(timer);
                }
            }
        }, 100);
    })

}
function loadLabeledImages() {
    const labels = ['']
    return Promise.all(
        labels.map(async (label)=>{
            const descriptions = []
                const img = await faceapi.fetchImage('voter.png');
                const detections = await faceapi.detectSingleFace(img).withFaceLandmarks().withFaceDescriptor()
                descriptions.push(detections.descriptor)
            return new faceapi.LabeledFaceDescriptors(label, descriptions)
        })
    )
}