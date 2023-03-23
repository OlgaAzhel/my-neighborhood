

let reports
let url = '/reportsApi'
let photos
let photosurl = '/photosApi'


fetch(photosurl)
    .then(response => response.json())
    .then(data => photos = [...data])


fetch(url)
    .then(response => response.json())
    .then(data => reports = data)
    .then(showCat => showReports())
    .then(centerMap => center())


let mymap = L.map('mapid').setView([28.0683496, -80.5603303], 14)
let marker


L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(mymap);

function showReports() {
    reports.forEach(report => {
        let pictureArr = []
        if (photos) {
            pictureArr = photos.filter(picObj => {
                return picObj.report === report.id
            })
        }
        let imgUrl = ""
        let content
        if (pictureArr.length > 0) {
            imgUrl = pictureArr[0].url
            content = '<a href =/reports/' + report.id + '><img src=' + imgUrl + ' style="width: 100px"></a>'
        } else {
            content = '<a href=/reports/' + report.id + '>DETAILS HERE--></a>'
        }

        let pop = L.popup({
            closeOnClick: true
        }).setContent(content)
        let coords = [report.coordX, report.coordY]
        let marker = L.marker(coords).addTo(mymap).bindPopup(pop)

        tooltip = L.tooltip({
            permanent: true
        }).setContent(report.title)
        marker.bindTooltip(tooltip)
    })
}





let list = document.querySelectorAll('.card')

function center() {
    reports.forEach((cat, idx) => {
        console.log("script is running")
        list[idx].addEventListener("mouseover", (event) => {
            mymap.flyTo([cat.coordX, cat.coordY], 14)
        })
    })
}