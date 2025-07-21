//select id=red_header
const red_class = document.querySelector('#red_header');
//select header
const header = document.querySelector('header');
red_class.addEventListener('click', function() {
    header.classList.add('red');
})
