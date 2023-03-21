
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

let mymap = L.map('mapid').setView([28.0683496, -80.5603303], 14)
let marker

L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(mymap);

function showReports() {
    reports.forEach(report => {
        let pop = L.popup({
            closeOnClick: true
        }).setContent('<img src=' + report.photo_url + ' style="width: 100px">')
        let coords = [report.coordX, report.coordY]
        let marker = L.marker(coords).addTo(mymap).bindPopup(pop)

        tooltip = L.tooltip({
            permanent: true
        }).setContent('<p>' + report.title + '</p>')
        marker.bindTooltip(tooltip)
    })
}
let reports
let url = '/reportsApi'
fetch(url)
    .then(response => response.json())
    .then(data => reports = data)
    .then(showCat => showReports())
    .then(centerMap => center())

let list = document.querySelectorAll('.card')

function center() {
    reports.forEach((cat, idx) => {
        console.log("script is running")
        list[idx].addEventListener("mouseover", (event) => {
            mymap.flyTo([cat.coordX, cat.coordY], 14)
        })
    })
}