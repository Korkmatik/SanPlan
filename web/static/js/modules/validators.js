
export function validateNotEmptyInput(inputBox) {
    return checkValue(inputBox, val => val == "");
}

export function validateNotNegativeInput(inputBox) {
    return checkValue(inputBox, val => parseInt(val) <= 0);
}

function checkValue(inputBox, comparison) {
    clearClasses(inputBox);

    if (comparison(inputBox.value))
        return invalid(inputBox);

    return makeValid(inputBox);
}

export function makeValid(inputBox) {
    addValidClass(inputBox);
    return true;
}

export function invalid(inputBox) {
    addInvalidClass(inputBox);
    return false;
}

function clearClasses(inputBox) {
    inputBox.classList.remove("is-valid");
    inputBox.classList.remove("is-invalid");
}

function addValidClass(inputBox) {
    inputBox.classList.add("is-valid");
}

function addInvalidClass(inputBox) {
    inputBox.classList.add("is-invalid");
}