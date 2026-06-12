async function analyze() {

    const need = document.querySelector(".need").value;
    const url = document.querySelector(".urlinput").value;
    const preferenceIds = ["story", "difficulty", "action","strategy", "free","calm"];
    const labels = {
    "story":"스토리",
    "difficulty":"난이도",
    "action":"액션성",
    "strategy":"전략성",
    "free":"자유도",
    "calm":"힐링도"
    }

    const preferences = getValues(preferenceIds)

    const loading = document.querySelector(".loading-overlay");

    loading.classList.remove("hidden");

    const res = await fetch("https://strev.fastapicloud.dev/analyze", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            url: url,
            need: need,
            preferences: preferences

        })
    });

    const data = await res.json();
    const percentageScore = toPercent(data.score);

    const gameImage = document.querySelector(".game-image");
    const gameTitle = document.querySelector(".game-title");
    const gameScore = document.querySelector(".game-score");

    gameImage.src = data.imgurl;
    gameTitle.innerText = "게임명: "+data.title;

    const scoreSectionDiv = document.querySelector(".score-section")

    html = "";
    for(const id of preferenceIds){
        if (preferences[id] > 0) {
            const score = toPercent(data.pref[id]);
            const label = labels[id]

            html += `
            <div class="score_row">
            <span>${label}: ${score}%</span><br>
            </div>
        `;
        }
    }

    scoreSectionDiv.innerHTML = html

    if (!!need || need.length !== 0){
        gameScore.innerText = "적합도: "+ percentageScore + "%";
    }


    const gpt = await gptFront()

    const infoPara = document.querySelector(".info");
    infoPara.innerText = gpt.desc;

    loading.classList.add("hidden");
}

async function gptFront(){
    const url = document.querySelector(".urlinput").value;
    const preferences = getValues(["story", "difficulty", "action","strategy", "free","calm"])
    const need = document.querySelector(".need").value;

    const res = await fetch("https://strev.fastapicloud.dev/gpt", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            url: url,
            need: need,
            preferences: preferences
        })
    });
    const data = await res.json()

    return data
}

function toPercent(fl){
    return Math.round(10000 * fl) / 100
}

function getValues(preferenceIds){
    const preferences = {};

    for(const id of preferenceIds) {
        preferences[id] = Number(document.querySelector(`#${id}`).value);
    }

    return preferences
}