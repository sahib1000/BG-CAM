document.addEventListener("DOMContentLoaded", function () {
    const video = document.getElementById("camera");
    const captureBtn = document.getElementById("captureBtn");
    const loadingDiv = document.getElementById("loading");
    const outputImage = document.getElementById("outputImage");
    const downloadBtn = document.getElementById("downloadBtn");

    navigator.mediaDevices.getUserMedia({ video: true })
        .then(stream => {
            video.srcObject = stream;
        })
        .catch(err => {
            alert("Please allow camera access in browser settings.");
            console.error("Camera error:", err);
        });

    captureBtn.addEventListener("click", () => {
        const canvas = document.createElement("canvas");
        canvas.width = video.videoWidth;
        canvas.height = video.videoHeight;
        canvas.getContext("2d").drawImage(video, 0, 0);

        canvas.toBlob(blob => {
            const formData = new FormData();
            formData.append("image", blob, "photo.png");

            loadingDiv.classList.remove("hidden");

            fetch("/process", {
                method: "POST",
                body: formData
            })
            .then(res => res.blob())
            .then(blob => {
                loadingDiv.classList.add("hidden");
                const url = URL.createObjectURL(blob);
                outputImage.src = url;
                downloadBtn.href = url;
                downloadBtn.classList.remove("hidden");
            })
            .catch(err => console.error("Error:", err));
        }, "image/png");
    });
});
