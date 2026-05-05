async function analyze(){

    const need = document.getElementsByClassName("need")[0].value;
    const url = document.getElementsByClassName("urlinput")[0].value;

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

    const percentage_score = Math.round(10000*data.score)/100

    const resultEl =document.getElementsByClassName("result");

    resultEl.innerText = percentage_score+"%"
}