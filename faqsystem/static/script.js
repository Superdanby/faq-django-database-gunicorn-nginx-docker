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

function update(id)
{
    if (!array[id])
    {
        array[id] = true;

        var formData = new FormData();
        for(element of document.getElementById("clicks-form-" + id))
        {
            formData.append(element.name, element.value);
        }
        var xmlHttp = new XMLHttpRequest();
        xmlHttp.onreadystatechange = function()
        {
            if(xmlHttp.readyState == 4 && xmlHttp.status == 200)
            {
                document.getElementById("clicks-" + id).innerHTML = xmlHttp.responseText + "<i class=\"material-icons md-14\">search</i>";
            }
        }
        xmlHttp.open("post", window.location.href);
        xmlHttp.send(formData);
    }
}

var array = [];
