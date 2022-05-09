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
// document.querySelector("#snap").addEventListener("click", function(){   
//     var ctx = canvas.getContext("2d");
//     ctx.drawImage(video, 0, 38, 300, 225);
//     console.log(video.srcObject);
//     document.getElementById("submit_vote").style.display = "inline-block";
// });
// Created to capture the image from camera

function loadModels(){
    Promise.all([
        faceapi.nets.tinyFaceDetector.loadFromUri('/models'),
        faceapi.nets.faceRecognitionNet.loadFromUri("/models"),
        faceapi.nets.faceLandmark68Net.loadFromUri("/models"),
        faceapi.nets.ssdMobilenetv1.loadFromUri("/models")
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
    // console.log(labeledDescriptors)
    const faceMatcher = new faceapi.FaceMatcher(labeledDescriptors, 0.7)


    video.addEventListener('play', async () => {
        console.log('Playing')
        // const canvas = faceapi.createCanvasFromMedia(video)
        // document.body.append(canvas)

        // const displaySize = { width: video.width, height: video.height }
        // faceapi.matchDimensions(canvas, displaySize)
        var timer = setInterval(async () => {
            const detections = await faceapi.detectAllFaces(video).withFaceLandmarks().withFaceDescriptors()

            // const resizedDetections = faceapi.resizeResults(detections, displaySize)

            // canvas.getContext('2d').clearRect(0, 0, canvas.width, canvas.height)

            // Here it was resizedDetections.map ans so on...
            const results = detections.map((d) => {
                return faceMatcher.findBestMatch(d.descriptor)
            });

            if(results.length > 0){ // if math is greater than 60% then it will recognize.
                if(results[0]["_distance"] >= 0.6){ // Only required these to recognize the face.
                    console.log(results[0]["_distance"]);
                    console.log("Matched");
                    document.getElementById("submit_vote").style.display = "block";
                    clearInterval(timer);
                }
            }
            // results.forEach( (result, i) => {
            //     const box = resizedDetections[i].detection.box
            //     const drawBox = new faceapi.draw.DrawBox(box, { label: result.toString() })
            //     drawBox.draw(canvas)
            // })
        }, 100);

        // work after matched is done.
    })

}
function loadLabeledImages() {
    //const labels = ['Black Widow', 'Captain America', 'Hawkeye' , 'Jim Rhodes', 'Tony Stark', 'Thor', 'Captain Marvel']
    const labels = [''] // for WebCam
    return Promise.all(
        labels.map(async (label)=>{
            const descriptions = []
            // for(let i=1; i<=2; i++) {
                const img = await faceapi.fetchImage('voter.png');
                const detections = await faceapi.detectSingleFace(img).withFaceLandmarks().withFaceDescriptor()
                // console.log(label + i + JSON.stringify(detections))
                descriptions.push(detections.descriptor)
            // }
            // document.body.append(label+' Faces Loaded | ')
            return new faceapi.LabeledFaceDescriptors(label, descriptions)
        })
    )
}