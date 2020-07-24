function ajaxrequest(input_id,req_url,span_id)
{
    var cn = document.getElementById(input_id).value;
    var val = "cname="+cn;
    var request = new XMLHttpRequest();
    request.onreadystatechange = check;
    request.open("POST",req_url,true);
    request.setRequestHeader('Content-Type','application/x-www-form-urlencoded');
    request.send(val);
    function check()
    {
    if (request.readyState == 4)
    {
        var val = request.responseText;
        var json_data = JSON.parse(val);
        var sp = document.getElementById(span_id);
        if(json_data.error != undefined)
        {
            sp.innerText = json_data.error;
            document.getElementById("b1").disabled = true;
        }
        else
        {
            sp.innerText = json_data.mess;
            document.getElementById("b1").disabled = false
        }
    }
    }

}