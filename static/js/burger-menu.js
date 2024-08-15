const burgerMenu = document.querySelector('.burger-menu')
const navigation = document.querySelector('.navigation')
let isMainMenuActive = false

burgerMenu.addEventListener('click', function () {
    if (!isMainMenuActive) {
        navigation.classList.add('active');
        burgerMenu.classList.add('active');
    } else {
        navigation.classList.remove('active');
        burgerMenu.classList.remove('active');
    }
    isMainMenuActive = !isMainMenuActive
});

document.addEventListener('DOMContentLoaded', function () {
    document.addEventListener('click', function (event) {
        if (isMainMenuActive) {
            let isClickInsideMenu = navigation.contains(event.target);
            if (!isClickInsideMenu && event.target !== document.querySelector('.burger-menu')) {
                navigation.classList.remove('active');
                burgerMenu.classList.toggle('active');
                isMainMenuActive = false;
            }
        }
    });
});