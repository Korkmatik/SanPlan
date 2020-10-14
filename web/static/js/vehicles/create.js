import {validateNotEmptyInput} from "../modules/validators.js";
import {validateNotNegativeInput} from "../modules/validators.js";
import {postVehicle} from "../modules/api.js";

let submitBtn = document.querySelector("#submit");
let vehicleNameInput = document.querySelector("#vehicle-name");
let licensePlateInput = document.querySelector("#license-plate");
let radioCallNameInput = document.querySelector("#radio-call-name");
let seatsInput = document.querySelector("#seats");
let imageInput = document.querySelector("#image");
let vehicleTypeInput = document.querySelector("#vehicle-type");
let stateInput = document.querySelector("#state");

submitBtn.addEventListener("click", createVehicle);

function createVehicle(event) {
    event.preventDefault();
    console.log(event);

    let isValid = true;
    isValid = validateNotEmptyInput(licensePlateInput);
    isValid = validateNotEmptyInput(seatsInput);
    isValid = validateNotNegativeInput(seatsInput);
    isValid = validateNotEmptyInput(vehicleTypeInput);
    isValid = validateNotEmptyInput(stateInput);
    if (!isValid) return;

    // TODO: add image
    let data = {
        "name": vehicleNameInput.value,
        "kennzeichen": licensePlateInput.value,
        "funkrufname": radioCallNameInput.value,
        "status": stateInput.value,
        "typ": vehicleTypeInput.value,
        "seats": seatsInput.value
    };

    postVehicle(
        vehicleNameInput.value,
        licensePlateInput.value,
        radioCallNameInput.value,
        stateInput.value,
        vehicleTypeInput.value,
        vehicleTypeInput.innerText,
        seatsInput.value,
        imageInput.files[0]
    )

}