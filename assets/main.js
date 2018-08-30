this.onload = function (e) {

}

function printText(text) {
    fetch('./webprint/print', {
        method: 'POST',
        body: text
    }).then(response => {
        console.log(response.status)
        if (response.status === 200) {
            alert('Job accepted')
        }
        //console.log(response.json())
    })
}


function printFile() {
    fetch('./webprint/print', {
        method: 'POST',
        body: document.getElementById('fileinput').files[0]
    }).then(response => {
        console.log(response.status)
        if (response.status === 200) {
            alert('Job accepted')
        }
    })
}