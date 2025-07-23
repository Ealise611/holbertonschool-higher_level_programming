//select id = update_header
const update_header = document.querySelector('#update_header');
//select header
const header = document.querySelector('header');

update_header.addEventListener('click', function() {
    header.textContent = 'New Header!!!'
});
