import {getCsrfToken} from "./utils.js";
import {launch_success_toast} from "./utils.js";
import {launch_error_toast} from "./utils.js";
import {toBase64} from "./utils.js";

const apiURL = '/api/v1/';

export function postVehicle(
    name, licensePlate, radioCallName,
    state, vehicleTyp, vehicleTypeName, seats, file
) {
    let url = apiURL + 'vehicles/';

    if (file == undefined) file = null;

    let data = {
        "name": name,
        "license_plate": licensePlate,
        "radio_call_name": radioCallName,
        "status": state,
        "type": {
          "short": vehicleTyp,
          "name": vehicleTypeName
        },
        "seats": seats,
        "image": null
    };

    console.log(data);

    fetch(url, {
        method: 'POST',
        cache: 'no-cache',
        credentials: 'same-origin',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCsrfToken()
        },
        body: JSON.stringify(data)
    })
        .then(response => response.json())
        .then(data => {
            console.log(data)
            if (data.id != undefined)
                launch_success_toast("Fahrzeug erfolgreich erstellt!");

        })
        .catch(e => {
            console.error(e);
            launch_error_toast("Fahrzeug konnte nicht erstellt werden!");
        });
}