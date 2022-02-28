d3.json("/api/Country").then(data=>{
  var dd = d3.select("#countrySelector")
  console.log(data.names)
  data.names.forEach(n=>{
      dd.append("option").text(n).property("value", n)
  }) 
  
  console.log(data)
})

d3.select("#countrySelector").on("change",()=>{
  country = d3.select("#countrySelector").node().value
  d3.json(`/predict/temp/${country}`).then(data=>{
    console.log(data)
    d3.select("#temp_dump").html(data.prediction.map(row => `<li>${row}</li>`))
  })

})