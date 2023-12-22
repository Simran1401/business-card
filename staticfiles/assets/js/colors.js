// customclr.addEventListener("input", myFunction);
// function myFunction() {
//   console.log('color', customclr.value);
// }
let customclr = document.getElementById("myColor");
customclr.addEventListener("input", function () {
    let colorValue = customclr.value;
    const input = document.getElementById("my-input");
    var r = document.querySelector(':root');
    console.log('color', customclr.value);
    r.style.setProperty('--blue', colorValue);
    input.value = colorValue;
    console.log('--blue:', r.style.getPropertyValue('--blue'));
    console.log(input.value);
    localStorage.setItem('my-input-value', colorValue);

});

function selectFontColor() {
    var select = document.getElementById("form_select");
    var fontColor = select.value === "black" ? "black" : "white";
    var root = document.querySelector(":root");
    root.style.setProperty("--font_color", fontColor);
    console.log("--font_color:", root.style.getPropertyValue('--font_color'));

    localStorage.setItem('font-color', fontColor);
}

// function selectFontFamily1() {
//     var select = document.getElementById("form_select1");
//     var fontFamily = select.value === "Montserrat" ? "Montserrat" : "Jost";
//     var root = document.querySelector(":root");
//     root.style.setProperty("--font_family1", fontFamily);
//     console.log("--font_family1:", root.style.getPropertyValue('--font_family1'));
// }

function selectFontFamily1() {
    var select = document.getElementById("form_select1");
    var fontFamily;
    switch (select.value) {
        case "Montserrat":
            fontFamily = "Montserrat";
            break;
        case "Jost":
            fontFamily = "Jost";
            break;
        case "Open Sans":
            fontFamily = "Open Sans";
            break;
        case "Roboto":
            fontFamily = "Roboto";
            break;
        case "Lato":
            fontFamily = "Lato";
            break;
        case "Poppins":
            fontFamily = "Poppins";
            break;
        case "Ubuntu":
            fontFamily = "Ubuntu";
            break;
        case "Source Sans Pro":
            fontFamily = "Source Sans Pro";
            break;
        case "Nunito":
            fontFamily = "Nunito";
            break;
        case "Playfair Display":
            fontFamily = "Playfair Display";
            break;
        case "Oswald":
            fontFamily = "Oswald";
            break;
        case "Lora":
            fontFamily = "Lora";
            break;
        case "Merriweather":
            fontFamily = "Merriweather";
            break;
        default:
            fontFamily = "Jost";
            break;
    }
    var root = document.querySelector(":root");
    root.style.setProperty("--font_family1", fontFamily);
    localStorage.setItem('font-family1', fontFamily);
    console.log("--font_family1:", root.style.getPropertyValue('--font_family1'));
}

function selectFontFamily2() {
    var select = document.getElementById("form_select2");
    var fontFamily;
    switch (select.value) {
        case "Montserrat":
            fontFamily = "Montserrat";
            break;
        case "Jost":
            fontFamily = "Jost";
            break;
        case "Open Sans":
            fontFamily = "Open Sans";
            break;
        case "Roboto":
            fontFamily = "Roboto";
            break;
        case "Lato":
            fontFamily = "Lato";
            break;
        case "Poppins":
            fontFamily = "Poppins";
            break;
        case "Ubuntu":
            fontFamily = "Ubuntu";
            break;
        case "Source Sans Pro":
            fontFamily = "Source Sans Pro";
            break;
        case "Nunito":
            fontFamily = "Nunito";
            break;
        case "Playfair Display":
            fontFamily = "Playfair Display";
            break;
        case "Oswald":
            fontFamily = "Oswald";
            break;
        case "Lora":
            fontFamily = "Lora";
            break;
        case "Merriweather":
            fontFamily = "Merriweather";
            break;
        default:
            fontFamily = "Jost";
            break;
    }
    var root = document.querySelector(":root");
    root.style.setProperty("--font_family2", fontFamily);
    localStorage.setItem('font-family2', fontFamily);
    console.log("--font_family2:", root.style.getPropertyValue('--font_family2'));
}

let c_1 = document.getElementById("color_1");
let c_2 = document.getElementById("color_2");
let c_3 = document.getElementById("color_3");
let c_4 = document.getElementById("color_4");
let c_5 = document.getElementById("color_5");
let c_6 = document.getElementById("color_6");
let c_7 = document.getElementById("color_7");
let c_8 = document.getElementById("color_8");
let c_9 = document.getElementById("color_9");
let c_10 = document.getElementById("color_10");
let c_11 = document.getElementById("color_11");
let c_12 = document.getElementById("color_12");
let c_13 = document.getElementById("color_13");
let c_14 = document.getElementById("color_14");
let c_15 = document.getElementById("color_15");

function changeToColor1() {
    const colorValue = 'dodgerblue';
    const color1 = document.querySelector(':root');
    const input = document.getElementById("my-input");
    color1.style.setProperty('--blue', colorValue);
    input.value = colorValue;
    console.log(input.value);
    localStorage.setItem('my-input-value', colorValue);
    color1.style.setProperty('--blue', colorValue);
    c_1.classList.add('active');
    c_2.classList.remove('active');
    c_3.classList.remove('active');
    c_4.classList.remove('active');
    c_5.classList.remove('active');
    c_6.classList.remove('active');
    c_7.classList.remove('active');
    c_8.classList.remove('active');
    c_9.classList.remove('active');
    c_10.classList.remove('active');
    c_11.classList.remove('active');
    c_12.classList.remove('active');
    c_13.classList.remove('active');
    c_14.classList.remove('active');
    c_15.classList.remove('active');
}

function changeToColor2() {
    const colorValue = 'tomato';
    const color2 = document.querySelector(':root');
    const input = document.getElementById("my-input");
    color2.style.setProperty('--blue', colorValue);
    input.value = colorValue;
    console.log(input.value);
    localStorage.setItem('my-input-value', colorValue);
    c_2.classList.add('active');
    c_1.classList.remove('active');
    c_3.classList.remove('active');
    c_4.classList.remove('active');
    c_5.classList.remove('active');
    c_6.classList.remove('active');
    c_7.classList.remove('active');
    c_8.classList.remove('active');
    c_9.classList.remove('active');
    c_10.classList.remove('active');
    c_11.classList.remove('active');
    c_12.classList.remove('active');
    c_13.classList.remove('active');
    c_14.classList.remove('active');
    c_15.classList.remove('active');
}

function changeToColor3() {
    const colorValue = 'orange';
    const color3 = document.querySelector(':root');
    const input = document.getElementById("my-input");
    color3.style.setProperty('--blue', colorValue);
    input.value = colorValue;
    console.log(input.value);
    localStorage.setItem('my-input-value', colorValue);
    c_3.classList.add('active');
    c_2.classList.remove('active');
    c_1.classList.remove('active');
    c_4.classList.remove('active');
    c_5.classList.remove('active');
    c_6.classList.remove('active');
    c_7.classList.remove('active');
    c_8.classList.remove('active');
    c_9.classList.remove('active');
    c_10.classList.remove('active');
    c_11.classList.remove('active');
    c_12.classList.remove('active');
    c_13.classList.remove('active');
    c_14.classList.remove('active');
    c_15.classList.remove('active');
}

function changeToColor4() {
    const colorValue = 'mediumseagreen';
    const color4 = document.querySelector(':root');
    const input = document.getElementById("my-input");
    color4.style.setProperty('--blue', colorValue);
    input.value = colorValue;
    console.log(input.value);
    localStorage.setItem('my-input-value', colorValue);
    c_4.classList.add('active');
    c_2.classList.remove('active');
    c_3.classList.remove('active');
    c_1.classList.remove('active');
    c_5.classList.remove('active');
    c_6.classList.remove('active');
    c_7.classList.remove('active');
    c_8.classList.remove('active');
    c_9.classList.remove('active');
    c_10.classList.remove('active');
    c_11.classList.remove('active');
    c_12.classList.remove('active');
    c_13.classList.remove('active');
    c_14.classList.remove('active');
    c_15.classList.remove('active');
}

function changeToColor5() {
    const colorValue = 'violet';
    const color5 = document.querySelector(':root');
    const input = document.getElementById("my-input");
    color5.style.setProperty('--blue', colorValue);
    input.value = colorValue;
    console.log(input.value);
    localStorage.setItem('my-input-value', colorValue);
    c_5.classList.add('active');
    c_2.classList.remove('active');
    c_3.classList.remove('active');
    c_4.classList.remove('active');
    c_1.classList.remove('active');
    c_6.classList.remove('active');
    c_7.classList.remove('active');
    c_8.classList.remove('active');
    c_9.classList.remove('active');
    c_10.classList.remove('active');
    c_11.classList.remove('active');
    c_12.classList.remove('active');
    c_13.classList.remove('active');
    c_14.classList.remove('active');
    c_15.classList.remove('active');
}

function changeToColor6() {
    const colorValue = 'brown';
    const color6 = document.querySelector(':root');
    const input = document.getElementById("my-input");
    color6.style.setProperty('--blue', colorValue);
    input.value = colorValue;
    console.log(input.value);
    localStorage.setItem('my-input-value', colorValue);
    c_6.classList.add('active');
    c_2.classList.remove('active');
    c_3.classList.remove('active');
    c_4.classList.remove('active');
    c_5.classList.remove('active');
    c_1.classList.remove('active');
    c_7.classList.remove('active');
    c_8.classList.remove('active');
    c_9.classList.remove('active');
    c_10.classList.remove('active');
    c_11.classList.remove('active');
    c_12.classList.remove('active');
    c_13.classList.remove('active');
    c_14.classList.remove('active');
    c_15.classList.remove('active');
}

function changeToColor7() {
    const colorValue = 'blueviolet';
    const color7 = document.querySelector(':root');
    const input = document.getElementById("my-input");
    color7.style.setProperty('--blue', colorValue);
    input.value = colorValue;
    console.log(input.value);
    localStorage.setItem('my-input-value', colorValue);
    c_7.classList.add('active');
    c_2.classList.remove('active');
    c_3.classList.remove('active');
    c_4.classList.remove('active');
    c_5.classList.remove('active');
    c_6.classList.remove('active');
    c_1.classList.remove('active');
    c_8.classList.remove('active');
    c_9.classList.remove('active');
    c_10.classList.remove('active');
    c_11.classList.remove('active');
    c_12.classList.remove('active');
    c_13.classList.remove('active');
    c_14.classList.remove('active');
    c_15.classList.remove('active');
}

function changeToColor8() {
    const colorValue = 'chocolate';
    const color8 = document.querySelector(':root');
    const input = document.getElementById("my-input");
    color8.style.setProperty('--blue', colorValue);
    input.value = colorValue;
    console.log(input.value);
    localStorage.setItem('my-input-value', colorValue);
    c_8.classList.add('active');
    c_2.classList.remove('active');
    c_3.classList.remove('active');
    c_4.classList.remove('active');
    c_5.classList.remove('active');
    c_6.classList.remove('active');
    c_7.classList.remove('active');
    c_1.classList.remove('active');
    c_9.classList.remove('active');
    c_10.classList.remove('active');
    c_11.classList.remove('active');
    c_12.classList.remove('active');
    c_13.classList.remove('active');
    c_14.classList.remove('active');
    c_15.classList.remove('active');
}

function changeToColor9() {
    const colorValue = 'crimson';
    const color9 = document.querySelector(':root');
    const input = document.getElementById("my-input");
    color9.style.setProperty('--blue', colorValue);
    input.value = colorValue;
    console.log(input.value);
    localStorage.setItem('my-input-value', colorValue);
    c_9.classList.add('active');
    c_2.classList.remove('active');
    c_3.classList.remove('active');
    c_4.classList.remove('active');
    c_5.classList.remove('active');
    c_6.classList.remove('active');
    c_7.classList.remove('active');
    c_8.classList.remove('active');
    c_1.classList.remove('active');
    c_10.classList.remove('active');
    c_11.classList.remove('active');
    c_12.classList.remove('active');
    c_13.classList.remove('active');
    c_14.classList.remove('active');
    c_15.classList.remove('active');
}

function changeToColor10() {
    const colorValue = 'darkgreen';
    const color10 = document.querySelector(':root');
    const input = document.getElementById("my-input");
    color10.style.setProperty('--blue', colorValue);
    input.value = colorValue;
    console.log(input.value);
    localStorage.setItem('my-input-value', colorValue);
    c_10.classList.add('active');
    c_2.classList.remove('active');
    c_3.classList.remove('active');
    c_4.classList.remove('active');
    c_5.classList.remove('active');
    c_6.classList.remove('active');
    c_7.classList.remove('active');
    c_8.classList.remove('active');
    c_9.classList.remove('active');
    c_1.classList.remove('active');
    c_11.classList.remove('active');
    c_12.classList.remove('active');
    c_13.classList.remove('active');
    c_14.classList.remove('active');
    c_15.classList.remove('active');
}

function changeToColor11() {
    const colorValue = 'darkmagenta';
    const color11 = document.querySelector(':root');
    const input = document.getElementById("my-input");
    color11.style.setProperty('--blue', colorValue);
    input.value = colorValue;
    console.log(input.value);
    localStorage.setItem('my-input-value', colorValue);
    c_11.classList.add('active');
    c_2.classList.remove('active');
    c_3.classList.remove('active');
    c_4.classList.remove('active');
    c_5.classList.remove('active');
    c_6.classList.remove('active');
    c_7.classList.remove('active');
    c_8.classList.remove('active');
    c_9.classList.remove('active');
    c_10.classList.remove('active');
    c_1.classList.remove('active');
    c_12.classList.remove('active');
    c_13.classList.remove('active');
    c_14.classList.remove('active');
    c_15.classList.remove('active');
}

function changeToColor12() {
    const colorValue = 'deeppink';
    const color12 = document.querySelector(':root');
    const input = document.getElementById("my-input");
    color12.style.setProperty('--blue', colorValue);
    input.value = colorValue;
    console.log(input.value);
    localStorage.setItem('my-input-value', colorValue);
    c_12.classList.add('active');
    c_2.classList.remove('active');
    c_3.classList.remove('active');
    c_4.classList.remove('active');
    c_5.classList.remove('active');
    c_6.classList.remove('active');
    c_7.classList.remove('active');
    c_8.classList.remove('active');
    c_9.classList.remove('active');
    c_10.classList.remove('active');
    c_11.classList.remove('active');
    c_1.classList.remove('active');
    c_13.classList.remove('active');
    c_14.classList.remove('active');
    c_15.classList.remove('active');
}

function changeToColor13() {
    const colorValue = 'gold';
    const color13 = document.querySelector(':root');
    const input = document.getElementById("my-input");
    color13.style.setProperty('--blue', colorValue);
    input.value = colorValue;
    console.log(input.value);
    localStorage.setItem('my-input-value', colorValue);
    c_13.classList.add('active');
    c_2.classList.remove('active');
    c_3.classList.remove('active');
    c_4.classList.remove('active');
    c_5.classList.remove('active');
    c_6.classList.remove('active');
    c_7.classList.remove('active');
    c_8.classList.remove('active');
    c_9.classList.remove('active');
    c_10.classList.remove('active');
    c_11.classList.remove('active');
    c_12.classList.remove('active');
    c_1.classList.remove('active');
    c_14.classList.remove('active');
    c_15.classList.remove('active');
}

function changeToColor14() {
    const colorValue = 'green';
    const color14 = document.querySelector(':root');
    const input = document.getElementById("my-input");
    color14.style.setProperty('--blue', colorValue);
    input.value = colorValue;
    console.log(input.value);
    localStorage.setItem('my-input-value', colorValue);
    c_14.classList.add('active');
    c_2.classList.remove('active');
    c_3.classList.remove('active');
    c_4.classList.remove('active');
    c_5.classList.remove('active');
    c_6.classList.remove('active');
    c_7.classList.remove('active');
    c_8.classList.remove('active');
    c_9.classList.remove('active');
    c_10.classList.remove('active');
    c_11.classList.remove('active');
    c_12.classList.remove('active');
    c_13.classList.remove('active');
    c_1.classList.remove('active');
    c_15.classList.remove('active');
}

function changeToColor15() {
    const colorValue = 'black';
    const color15 = document.querySelector(':root');
    const input = document.getElementById("my-input");
    color15.style.setProperty('--blue', colorValue);
    input.value = colorValue;
    console.log(input.value);
    localStorage.setItem('my-input-value', colorValue);
    c_15.classList.add('active');
    c_2.classList.remove('active');
    c_3.classList.remove('active');
    c_4.classList.remove('active');
    c_5.classList.remove('active');
    c_6.classList.remove('active');
    c_7.classList.remove('active');
    c_8.classList.remove('active');
    c_9.classList.remove('active');
    c_10.classList.remove('active');
    c_11.classList.remove('active');
    c_12.classList.remove('active');
    c_13.classList.remove('active');
    c_14.classList.remove('active');
    c_1.classList.remove('active');
}

function selectImage(image) {
    // Remove active class from previously selected image, if any
    var activeImage = document.querySelector('.col-sm-4 .active');
    if (activeImage) {
        activeImage.classList.remove('active');
    }

    // Add active class to the clicked image
    image.classList.add('active');

    // Get the image value (x.id) and update the separate input tag
    var imageValue = image.previousElementSibling.value;
    document.getElementById('selected-image').value = imageValue;

    // Save the image value in localStorage
    localStorage.setItem('selectedImage', imageValue);

    // Log the selected image value to the console
    console.log('Selected Image ID:', imageValue);
}


// Check if a selected image is stored in localStorage
var storedImage = localStorage.getItem('selectedImage');
if (storedImage) {
    // Add active class to the corresponding image
    var imageElements = document.querySelectorAll('.col-sm-4 img');
    for (var i = 0; i < imageElements.length; i++) {
        if (imageElements[i].src === storedImage) {
            imageElements[i].classList.add('active');
        } else {
            imageElements[i].classList.remove('active');
        }
    }

    // Update the separate input tag with the stored image value
    document.getElementById('selected-image').value = storedImage;

    // Log the selected image value to the console
    console.log('Selected Image:', storedImage);
}

