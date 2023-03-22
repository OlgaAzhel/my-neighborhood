let reportAddress = document.querySelector('#address')
let addresses = document.querySelector('#addresses')

let address = document.querySelector('#id_location')
let coordX = document.querySelector('#id_coordX')
let coordY = document.querySelector('#id_coordY')


function findAddresses() {
    console.log(reportAddress.value)
    let url = "https://nominatim.openstreetmap.org/search?format=json&limit=3&q=" + reportAddress.value
    console.log(url)
    fetch(url)
        .then(response => response.json())
        .then(data => addressArr = data)
        .then(showAddress => showAddresses())
        .catch(err => console.log(err))
}

function showAddresses() {
    addresses.innerHTML = ''
    if (addressArr.length > 0) {
        addressArr.forEach(address => {
            addresses.innerHTML = 'Please choose address:<br>'
            let addressName = address.display_name.replace("'", " ")
            addresses.innerHTML += "<a href='#' onclick='selectAddress(" +
                address.lat + "," + address.lon + "," + '"' + addressName + '"' + ")'>"
                + address.display_name
                // + "<br> Lat: " + element.lat
                // + " Lng: " + element.lon
                + "</a>"
        })
    }
    else {
        addresses.innerHTML = "<p style='color: red;'>Not found</p>"
    }
}

function selectAddress(x, y, adr) {
    address.value = adr
    coordX.value = x
    coordY.value = y
    mymap.flyTo([x, y], 16)
    marker.closePopup()
    marker.setLatLng([x, y])

}

function selectOnMap(latlng) {
    coordX.value = latlng.lat
    coordY.value = latlng.lng
    mymap.flyTo([latlng.lat, latlng.lng], 16)
    marker.closePopup()
    marker.setLatLng([latlng.lat, latlng.lng])
    fetch(`https://nominatim.openstreetmap.org/reverse?lat=${latlng.lat}&lon=${latlng.lng}&format=json`, {
        headers: {
            'User-Agent': 'ID of your APP/service/website/etc. v0.1'
        }
    }).then(res => res.json())
        .then(res => {
            console.log(res.display_name)
            address.value = res.display_name
        })
}




let mymap = L.map('mapid').setView([28.0683496, -80.5603303],14)

let marker = L.marker([28.0683496, -80.5603303]).addTo(mymap)

L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(mymap);

mymap.on('click', function (e) {
    selectOnMap(e.latlng)
});