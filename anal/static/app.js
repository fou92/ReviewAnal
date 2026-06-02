async function analyze() {

    const need = document.querySelector(".need").value;
    const url = document.querySelector(".urlinput").value;

    const res = await fetch("https://strev.fastapicloud.dev/analyze", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            url: url,
            need: need
        })
    });

    const data = await res.json();
    const percentageScore = Math.round(10000 * data.score) / 100;

    const gameImage = document.querySelector(".game-image");
    const gameTitle = document.querySelector(".game-title");
    const gameScore = document.querySelector(".game-score");

    gameImage.src = data.imgurl;
    gameTitle.innerText = "게임명: "+data.title;
    gameScore.innerText = "적합도: "+ percentageScore + "%";

    const gpt = await gpt_front()

    const infoPara = document.querySelector(".info");
    infoPara.innerText = gpt.desc;
}

async function gpt_front(){
    const need = document.querySelector(".need").value;
    const url = document.querySelector(".urlinput").value;

    const res = await fetch("https://strev.fastapicloud.dev/gpt", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            url: url,
            need: need
        })
    });
    const data = await res.json()

    return data
}

// 23:34