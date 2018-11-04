__DATA_FOR_DB_STATUS__;
__selected_year__;
// var __selected_year__ = null;


var chart_Detailofyearchart = function(){

    var __data = __DATA_FOR_DB_STATUS__["detail_of_year"][__selected_year__];
    __data.sort(function(a,b){
        return a.label > b.label;
    })

    var chart = new CanvasJS.Chart("DetailOfYearChart", {
        animationEnabled: true,
        theme: "dark1",
        title: {
            text: "年中各月份狀態"
        },
        axisY: {
            title: "文章數量",
            titleFontSize: 24
        },
        axisX:{
            title:"各月份",
            interval: 1,
        },
        data: [{
            type: "column",
            yValueFormatString: "#,### 篇文章",
            showInLegend: true, 
		    legendMarkerColor: "grey",
            dataPoints: __DATA_FOR_DB_STATUS__["detail_of_year"][__selected_year__]
        }]
    });

    // 繪圖
    chart.render();
}
