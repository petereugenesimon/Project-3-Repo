let apiCOD = "/api/v1.0/codsYears";

function init() {
    d3.json(apiCOD).then(function(data) {
        let filter = "2020"
        data = data['2020']
        let dataPlot = [{
            x: Object.keys(data),
            y: Object.values(data),
            type: 'bar'
        }]
        Plotly.newPlot("plot", dataPlot);
    });
}

function refreshPlot() {
    let dropdownMenu = d3.select("#selDataset");
    let filter = dropdownMenu.property("value");
    d3.json(apiCOD).then(function(data) {
        data = data[filter]
        let dataPlot = [{
            x: Object.keys(data),
            y: Object.values(data),
            type: 'bar'
        }]
        Plotly.newPlot("plot", dataPlot);
    });
}

d3.selectAll("#selDataset").on("change", refreshPlot);

init();

