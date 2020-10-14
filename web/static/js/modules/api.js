import {getCsrfToken} from "./utils.js";
import {launch_success_toast} from "./utils.js";
import {launch_error_toast} from "./utils.js";

const apiURL = '/api/v1/';

export function postVehicle(
    name, licensePlate, radioCallName,
    state, vehicleTyp, vehicleTypeName, seats, file
) {
    let url = apiURL + 'vehicles/';

    if (file == undefined) file = null;

    let data = {
        "name": name,
        "kennzeichen": licensePlate,
        "funkrufname": radioCallName,
        "status": state,
        "vehicle_type_short": vehicleTyp,
        "vehicle_type_name": vehicleTypeName,
        "seats": seats,
        "image": file
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
            if (data.id != undefined)
                launch_success_toast("Fahrzeug erfolgreich erstellt!");
        })
        .catch(e => {
            console.error(e);
            launch_error_toast("Fahrzeug konnte nicht erstellt werden!");
        });
}