//select id=toggle_header
const toggle_class = document.querySelector('#toggle_header');
//select header
const header = document.querySelector('header');
toggle_class.addEventListener('click', function() {
    if (header.classList.contains('green')) {
        header.classList.remove('green');
        header.classList.add('red')
    } else {
        header.classList.remove('red');
        header.classList.add('green');
    }
});
