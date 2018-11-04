// Global Variables
var __DATA_FOR_DB_STATUS__ = null;
var __selected_year__ = null;


var barchart_dbst = function() {

    var xhttp;
    xhttp=new XMLHttpRequest();
    var url = "http://localhost:5000/api/dbstatus/";
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            text = xhttp.responseText;
            data = JSON.parse(text);
            __DATA_FOR_DB_STATUS__ = data; // Backup Data
            console.log(__DATA_FOR_DB_STATUS__);
            callback_barchart("barchartContainer", data["year_count"]);
        }
    };
    xhttp.open("GET", url, true);
    xhttp.send();



    
    }


function callback_barchart(divid, data){
    function onClick(e){
        __selected_year__ = e.dataPoint.label;
        // alert( 
        //     e.dataSeries.type + ", dataPoint { x:" + e.dataPoint.label + ", y: "+ e.dataPoint.y + " }" 
        // );
        chart_Detailofyearchart();
        piechartCountryDetail();
    }


    var chart = new CanvasJS.Chart(divid, {
        animationEnabled: true,
        theme:"dark2",
        title:{
            text: "年份狀況 Year Status",
            horizontalAlign: "center"
        },
        data: [{
            type: "doughnut",
            startAngle: 60,
            click: onClick,
            //innerRadius: 60,
            indexLabelFontSize: 17,
            indexLabel: "{label} - #percent%",
            toolTipContent: "<b>{label}:</b> {y} (#percent%)",
            dataPoints: data // 真正的api資料
            // 假資料
            // dataPoints: [
            //     { y: 67, label: "Inbox" },
            //     { y: 28, label: "Archives" },
            //     { y: 10, label: "Labels" },
            //     { y: 7, label: "Drafts"},
            //     { y: 15, label: "Trash"},
            //     { y: 6, label: "Spam"}
            // ]
        }]
    });

    chart.canvas.setAttribute("id", "barchartContainerCanvas");



    // onclick
    // var canvas = $("#barchartContainerCanvas").next("canvas")[0];
    // console.log(canvas)
    // var canvas = document.getElementById("barchartContainerCanvas");
    // var ctx = canvas.getContext("2d");
    // canvas.onclick = function(evt) {

    //     console.log(typeof(chart));
    //     console.log(chart);
    //     var activePoints = chart.getElementsAtEvent(evt);
    //     if (activePoints[0]) {
    //       var chartData = activePoints[0]['_chart'].config.data;
    //       var idx = activePoints[0]['_index'];
  
    //       var label = chartData.labels[idx];
    //       var value = chartData.datasets[0].data[idx];
  
          
    //       console.log("label= "+ label + "  value= " + value);
    //     //   alert("label= "+ label + "  value= " + value);
    //     }
    // };




    // 繪圖
    chart.render();
}
