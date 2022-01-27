var input = document.getElementById("inputText");
var btn = document.getElementById("button");
var ul = document.getElementById("list");



function addToDo() {
    var li = document.createElement('li');
    li.classList.add('listItem');
    if(input.value.length > 0){ 
        inputText = document.createTextNode(input.value);
        li.appendChild(inputText);
        ul.appendChild(li);
        input.value = "";
    }
    
    li.addEventListener("click", toggleDone);

    function toggleDone() {
        li.classList.toggle('done');
    }
}

btn.addEventListener("click", addToDo);
