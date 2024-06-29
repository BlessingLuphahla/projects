function display(val) {
    document.getElementById('result').value += val;
    
}

function solve() {

    var result = document.getElementById('result').value;
    result = eval(result);
    document.getElementById('result').value = result;
}