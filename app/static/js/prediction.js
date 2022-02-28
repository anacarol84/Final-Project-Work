$("#prediction").click(() =>{
    var year = $("#year").val();
    var state = $("#state").val();
    console.log(year)
    console.log(state)
    $.getJSON(`/api/predict/${year}/${state}`, (predicted) => { 
        var temp = Math.floor(predicted.prediction)

        // //need to return global temperature prediction and Co2 when you select Year and Country
        // console.log(prediction)
        // var img_src = ""
        // var temp_text = ""
        // if(temp > 30){
        //     img_src = "static/img/hot.png"
        //     temp_text = `It is a hot sunny day. The temperature is expected to be ${temp}.`
        // } else if (temp > 15){
        //     img_src = "static/img/perfect.png"
        //     temp_text = `It is a perfect day to be out. The temperature is expected to be ${temp}.`
        // } else { 
        //     img_src = "static/img/cold.png"
        //     temp_text = `It is a shivering cold day. The temperature is expected to be ${temp}.`
        // }

        $("#forecasted-temp").html(`
        <div class="card" style="width: 18rem;">
            <img src="${img_src}" class="card-img-top">
            <div class="card-body">
            <p class="card-text">${temp_text}</p>
            </div>
        </div>
        `)
    });
});
d3.json("/api/Country").then(data=>{
    var dd = d3.select("#countrySelector")
    console.log(data.names)
    data.names.forEach(n=>{
        dd.append("option").text(n).property("value", n)
    }) 
    showInfo(data.names[0])
    console.log(data)
})

// d3.json("/api/temp/Australia").then(data=>{
//     console.log(data)
// })

async function showInfo(userInput) {
    d3.json(`/api/temp/${userInput}`).then(data=>{
        d3.select("#curr_country").html(userInput)
        d3.select("#temp_here").html(data.temperature)
        d3.select("#co_here").html(data.C02)
        console.log(data)
    })
}


