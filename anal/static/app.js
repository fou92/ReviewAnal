async function analyze(){

    const need = document.querySelector(".need").value;
    const url = document.querySelector(".urlinput").value;

    const res = await fetch("https://strev.fastapicloud.dev/analyze",{
        method:"POST",
        headers:{
            "Content-Type":"application/json"
        },
        body:JSON.stringify({
            url:url,
            need:need
        })
    });

    const data = await res.json();
    const percentage_score = Math.round(10000*data.score)/100;
    const resultEl =document.querySelector(".result");

    resultEl.innerText = percentage_score+"%"
}