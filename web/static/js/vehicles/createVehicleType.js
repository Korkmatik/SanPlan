import {validateNotEmptyInput} from "../modules/validators.js";
import {postVehicleType} from "../modules/api.js";

const shortInput = document.querySelector("#short");
const nameInput = document.querySelector("#name");

const submitBtn = document.querySelector("#submit_btn");
submitBtn.addEventListener("click", createVehicleType);

function createVehicleType(event) {
    event.preventDefault();

    let isValid = [];
    isValid.push(validateNotEmptyInput(shortInput));
    isValid.push(validateNotEmptyInput(nameInput));

    for (var valid of isValid)
        if (!valid)
            return;

    let data = {
        "short": shortInput.value,
        "name": nameInput.value
    };

    postVehicleType(data, () => {
        shortInput.value = "";
        shortInput.classList.remove("is-valid");
        nameInput.value = "";
        nameInput.classList.remove("is-valid");
    });
}