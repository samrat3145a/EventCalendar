function myFunction() {

    function1();
    checkEvent();

}

function funSubmit() {
    document.getElementById("form").submit();
}
function getDate(x) {
    var b = 1;
    var z = get_Date();
    z = z + "$";
    var l = 0, i = 0;
    for (l = 0; l < z.length; l++) {
        if (z[l] == "$") {
            var t = z.substr(l - i + 1, i - 1);
            if (b == x)
                return t;
            b++;
            i = 0;
        }
        i++;
    }

}
function function2() {
    var list1 = document.getElementsByClassName("current-day-events-list")[0];
    document.getElementById("all_event").style.visibility = "hidden";
    list1.innerHTML = " ";
    var l, count = 0;
    var n = get_count();
    for (l = 1; l <= n; l++) {
        var m = function1();
        var t = getDate(l + 1);
        // console.log(t+" "+m);
        //window.alert(dom2);
        if (m == t && count < 5) {
            count++;
        }
    }
    return count;
}

function function1() {
    var list1 = document.getElementsByClassName("calendar-left-side-day")[0];
    var g = list1.innerHTML;
    if (parseInt(list1.innerHTML) >= 1 && parseInt(list1.innerHTML) <= 9 && g.length < 2) {
        list1.innerHTML = '0' + list1.innerHTML;
    }
    var list3 = document.getElementsByClassName("calendar-current-year")[0];
    var list2 = document.getElementsByClassName("active")[0];
    var temp = list2.innerHTML;
    if (temp == 'Jan') temp = '01'; if (temp == 'Feb') temp = '02';
    if (temp == 'Mar') temp = '03'; if (temp == 'Apr') temp = '04';
    if (temp == 'May') temp = '05'; if (temp == 'Jun') temp = '06';
    if (temp == 'Jul') temp = '07'; if (temp == 'Aug') temp = '08';
    if (temp == 'Sep') temp = '09'; if (temp == 'Oct') temp = '10';
    if (temp == 'Nov') temp = '11'; if (temp == 'Dec') temp = '12';
    document.getElementById('test').value = list3.innerHTML + "-" + temp + "-" + list1.innerHTML;
    return (list3.innerHTML + "-" + temp + "-" + list1.innerHTML);

}

function checkEvent()
{
    var count=function2();
    // console.log(count);
    if(count > 0)
    {
        document.getElementById("btn_event").style.background='#007bff';
        document.getElementById("btn_event").innerText='Show todays Event';
    }

    else
    {
        document.getElementById("btn_event").innerText='No Event';
    }

}
