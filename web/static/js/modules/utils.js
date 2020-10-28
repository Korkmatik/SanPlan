
export function getCsrfToken() {
    let csrfMetaTag = document.querySelector("meta[name=csrf-token]")
    return csrfMetaTag.content;
}

// Credits goes to Pierre Smith: https://codepen.io/kipp0/pen/pPNrrj
export function launch_success_toast(message) {
    var x = document.getElementById("success-toast");
    var toastMessage = document.querySelector("div#success-desc");
    toastMessage.innerHTML = message;
    x.className = "show";
    setTimeout(function(){ x.className = x.className.replace("show", ""); }, 5000);
}

export function launch_error_toast(message) {
    var x = document.getElementById("error-toast");
    var toastMessage = document.querySelector("div#error-desc");
    toastMessage.innerHTML = message;
    x.className = "show";
    setTimeout(function(){ x.className = x.className.replace("show", ""); }, 5000);
}

export function toBase64(file) {
    return new Promise((resolve, reject) => {
        const reader = new FileReader();
        reader.readAsDataURL(file);
        reader.onload = () => resolve(reader.result);
        reader.onerror = error => reject(error);
    });
}
