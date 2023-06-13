// Grab data
let apiCod = "/api/v1.0/codsYears";

function init() {
  d3.json(apiCod).then(function(data) {
    let filter = "alzheimers";
    let dataPlot = getDataPlot(data, filter);
    Plotly.newPlot("plot", dataPlot);
  });
}

// Function to generate data plot for a given filter
function getDataPlot(data, filter) {
  console.log(data); // Check the data object
  console.log(filter); // Check the filter value

  let filteredData = data["2022"][filter];
  console.log(filteredData); // Check the filtered data

  if (filteredData) {
    let xValues = Object.keys(filteredData);
    let yValues = Object.values(filteredData);

    let trace = {
      x: xValues,
      y: yValues,
      type: 'bar'
    };

    let layout = {
      title: `Data Plot for ${filter} (2022)`,
      xaxis: {
        title: 'States'
      },
      yaxis: {
        title: 'Number of Cases'
      }
    };

    let plotData = [trace];

    return plotData;
  } else {
    // Handle the case when filteredData is undefined
    console.log(`No data available for filter: ${filter}`);
    return null;
  }
}


// Function called by DOM changes
function refreshPlot() {
  let dropdownMenu = d3.select("#selDataset");
  let filter = dropdownMenu.property("value");
  d3.json(apiCod).then(function(data) {
    let dataPlot = getDataPlot(data, filter);
    Plotly.newPlot("plot", dataPlot);
  });
}

// On change to the DOM, call refreshPlot()
d3.select("#selDataset").on("change", refreshPlot);

init();
