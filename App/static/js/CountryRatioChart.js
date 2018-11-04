__DATA_FOR_DB_STATUS__;
__selected_year__;


function piechartCountryDetail(){
    var chart = new CanvasJS.Chart("CountryRatioChart", {
        exportEnabled: true,
        animationEnabled: true,
        theme:"dark2",
        title:{
            text: "文章來源比"
        },
        legend:{
            cursor: "pointer",
            itemclick: explodePie
        },
        data: [{
            type: "pie",
            showInLegend: true,
            toolTipContent: "{name}: <strong>{y}篇文章</strong>",
            indexLabel: "{name} - {y}篇文章",
            dataPoints: __DATA_FOR_DB_STATUS__["role_of_year"][__selected_year__]
        }]
    });
    chart.render();
}




function explodePie (e) {
	if(typeof (e.dataSeries.dataPoints[e.dataPointIndex].exploded) === "undefined" || !e.dataSeries.dataPoints[e.dataPointIndex].exploded) {
		e.dataSeries.dataPoints[e.dataPointIndex].exploded = true;
	} else {
		e.dataSeries.dataPoints[e.dataPointIndex].exploded = false;
	}
	e.chart.render();

}