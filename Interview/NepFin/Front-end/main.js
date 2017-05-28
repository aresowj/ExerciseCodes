var allFilled = false;
var clickedDivs = [];

function init() {
    var boxes = document.getElementsByClassName("box");

    for (var i=0; i<boxes.length; i++) {
        boxes[i].addEventListener("click", function () {
            boxOnClick(boxes[i]);
        });
    }
}

function boxOnClick(div) {
    if (div.style.backgroundColor == "" || div.style.backgroundColor == "white") {
        div.style.backgroundColor = "#33C6E4";
    } else {
        div.style.backgroundColor = "white";
    }
}

init();
