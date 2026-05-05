async function analyze(){

    const need = document.getElementsByClassName(".need").value
    const url = document.getElementsByClassName(".urlinput").value

    const res = await fetch("http://localhost:8000/analyze",{
        method:"POST",
        headers:{
            "Content-Type":"application/json"
        },
        body:JSON.stringify({
            url:url,
            need:need
        })
    })

    const data = await res.json()

    const percentage_score = round(10000*data.score)/100

    document.getElementById("result").innerText =
        "니즈 부합도: " + percentage_score + "%"
}