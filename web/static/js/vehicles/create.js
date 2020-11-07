import {validateNotEmptyInput} from "../modules/validators.js";
import {validateNotNegativeInput} from "../modules/validators.js";
import {makeValid} from "../modules/validators.js";
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

    makeValid(vehicleNameInput);
    makeValid(radioCallNameInput);
    makeValid(imageInput);

    let isValid = [];
    isValid.push(validateNotEmptyInput(licensePlateInput));
    isValid.push(validateNotEmptyInput(seatsInput));
    isValid.push(validateNotNegativeInput(seatsInput));
    isValid.push(validateNotEmptyInput(vehicleTypeInput));
    isValid.push(validateNotEmptyInput(stateInput));
    for (var valid of isValid)
        if (!valid)
            return;

    // TODO: add image
    let data = {
        "name": vehicleNameInput.value,
        "kennzeichen": licensePlateInput.value,
        "funkrufname": radioCallNameInput.value,
        "status": stateInput.value,
        "typ": vehicleTypeInput.value,
        "seats": seatsInput.value
    };

    let vehicleTypeName = vehicleTypeInput[vehicleTypeInput.selectedIndex].text;
    vehicleTypeName = vehicleTypeName.match(/.* \(/)[0].replace(" (", "");

    postVehicle(
        vehicleNameInput.value,
        licensePlateInput.value,
        radioCallNameInput.value,
        stateInput.value,
        vehicleTypeInput.value,
        vehicleTypeName,
        seatsInput.value,
        imageInput.files[0]
    );

}
