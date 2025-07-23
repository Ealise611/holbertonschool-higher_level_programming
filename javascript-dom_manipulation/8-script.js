fetch('https://hellosalut.stefanbohacek.com/?lang=fr')
.then(response => response.json())
.then(data => {
    console.log("完整資料:", data); 
    //result from fetch
    const hello_results = data.hello;
    //select id = hello
    const id_hello = document.getElementById('hello');
    id_hello.textContent = hello_results;
})