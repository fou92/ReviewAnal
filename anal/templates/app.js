async function analyze(){

    const need = document.getElementById("need").value

    const res = await fetch("http://localhost:8000/analyze",{
        method:"POST",
        headers:{
            "Content-Type":"application/json"
        },
        body:JSON.stringify({
            need:need,
            game_id:578080
        })
    })

    const data = await res.json()

    document.getElementById("result").innerText =
        "니즈 부합도: " + data.need_match_score
}