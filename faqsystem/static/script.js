function show(id) {
    entry = document.getElementById(id);
    answer = entry.getElementsByClassName("answer")[0];
    if (answer.style.display == 'block') {
        // answer.style.removeProperty('-webkit-line-clamp');
        answer.style.display = 'none';
    } else {
        // answer.style.webkitLineClamp = 'unset';
        answer.style.display = 'block';
    }
    for (element of entry.getElementsByClassName("ansimg")) {
        if (element.style.display) {
            element.style.removeProperty('display');
        } else {
            element.style.display = 'unset';
        }
    }
    for (element of entry.getElementsByClassName("ansfile")) {
        if (element.style.display) {
            element.style.removeProperty('display');
        } else {
            element.style.display = 'block';
        }
    }
}
