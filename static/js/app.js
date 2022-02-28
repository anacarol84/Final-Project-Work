getData();

async function getData() {
    const response = await fetch('Climate_change_analysis.csv');
    const data = await response.text();
    console.log(data);
}   

const xlabels = [];
const ytemps = [];

chartIt();

async function chartIt() {
const data = await getData();
const ctx = document.getElementById('chart').getContext('2d');
const xlabels = [];
const myChart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: data.xs,
        datasets: [{
            label: 'Global Average Temperature',
            data: data.ys,
            fill: false,
            backgroundColor: 'rgba(75, 192, 192, 0.2)',
            borderColor: 'rgba(75, 192, 192, 1)',
            borderWidth: 1
        }]
    },
});
}

async function getData() {
  const xs = [];
  const ys = [];  

  const response = await fetch('Climate_change_analysis.csv');
  const data = await response.text();

  const table = data.split('\n').slice(1);
  table.forEach(row=> {
    const columns=row.split(',');
    const year = columns[0];
    xs.push(year);
    const temp = columns[1];
    ys.push(parseFloat(temp) + 14);
    console.log(year, temp);
  });
  return{xs, ys};
}

// d3.json("/api/data").then(data=>{
//     console.log(data);
// });

// d3.json("/api/temp/Australia").then(data=>{
//     console.log(data)