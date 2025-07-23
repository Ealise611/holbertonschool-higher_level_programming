//select id=add_item
const add_item = document.querySelector('#add_item');
//select class = my_list
const my_list = document.querySelector('.my_list');

add_item.addEventListener('click', function() {
    const new_item = document.createElement('li');
    new_item.textContent = 'Item';
    my_list.appendChild(new_item);
});
