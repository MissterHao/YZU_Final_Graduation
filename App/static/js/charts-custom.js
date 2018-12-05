var ActivateWord = [];  // 預設資料
var TRENDS_DATA = JSON.parse(TRENDS_DATA);
var colors = [
    "75,192,192",
    "234,122,8",
    "114,129,244",
    "64,158,161",
    "141,123,137",

    
    "118,197,204",
    "21,79,8",
    "206,116,238",
    "242,232,8",
    "225,134,134",
];

function getTrendDataConfig(key, index){

    var colorIndex = index;

    return {
            label: key,
            backgroundColor: "rgba(" + colors[colorIndex] + ",0.4)",
            borderColor: "rgba(" + colors[colorIndex] + ",1)",
            data: TRENDS_DATA[key],
            pointBorderColor: "rgba(" + colors[colorIndex] + ",1)",
            pointHoverBackgroundColor: "rgba(" + colors[colorIndex] + ",1)",
        
        
            fill: true,
            lineTension: 0.3,
            borderCapStyle: 'butt',
            borderDash: [],
            borderDashOffset: 0.0,
            borderJoinStyle: 'miter',
            borderWidth: 1,
            pointBackgroundColor: "#fff",
            pointBorderWidth: 1,
            pointHoverRadius: 5,
            pointHoverBorderColor: "rgba(220,220,220,1)",
            pointHoverBorderWidth: 2,
            pointRadius: 1,
            pointHitRadius: 10,
            spanGaps: false
        }
}


function redraw(){
    var LINECHARTEXMPLE   = $('#lineChartExample');

    var drawdataset=[]
    for(i in ActivateWord){
        drawdataset.push( getTrendDataConfig(ActivateWord[i], i) );
    }

    var lineChartExample = new Chart(LINECHARTEXMPLE, {
        type: 'line',
        data: {
            labels: [ "2017-3", "2017-4", "2017-5", "2017-6", "2017-7", "2017-8", "2017-9", "2017-10", "2017-11", "2017-12", "2018-1", "2018-2"],
            datasets: drawdataset
        }
    });

}

/*global $, document, LINECHARTEXMPLE*/
$(document).ready(function () {
    'use strict';




    var brandPrimary = 'rgba(51, 179, 90, 1)';

    var LINECHARTEXMPLE   = $('#lineChartExample');

    // ActivateWord.push("ethanol");
    // ActivateWord.push("hydro");
    var lineChartExample = new Chart(LINECHARTEXMPLE, {
        type: 'line',
        data: {
            labels: [ "2017-3", "2017-4", "2017-5", "2017-6", "2017-7", "2017-8", "2017-9", "2017-10", "2017-11", "2017-12", "2018-1", "2018-2"],
            datasets: [
                // getTrendDataConfig("ethanol"),
                // getTrendDataConfig("hydro")
            ]
        }
    });

    $(".add").click(function(){

        console.log("Before:  " + ActivateWord.join(", "))
        if( $( "#"+this.id ).hasClass( "activate" )){
            $("#"+this.id).removeClass("activate");
            $("#"+this.id).addClass("deactivate");
            
            $("#"+this.id+"Outer").removeClass("activate");
            $("#"+this.id+"Outer").addClass("deactivate");


            var index = ActivateWord.indexOf(this.id);
            console.log("index:"+index);
            if (index !== -1) ActivateWord.splice(index, 1);      
            
            
        }else if( $( "#"+this.id ).hasClass( "deactivate" )){
            $("#"+this.id).removeClass("deactivate");
            $("#"+this.id).addClass("activate");
            $("#"+this.id+"Outer").removeClass("deactivate");
            $("#"+this.id+"Outer").addClass("activate");

            ActivateWord.push(this.id);

        }

        console.log("After:  " + ActivateWord.join(", "))
        redraw();
    });
});



// function addData(chart, label, data) {
//     chart.data.labels.push(label);
//     chart.data.datasets.forEach((dataset) => {
//         dataset.data.push(data);
//     });
//     chart.update();
// }

// function addData(chart, label, data) {
//     chart.data.labels.push(label);
//     chart.data.datasets.forEach((dataset) => {
//         dataset.data.push(data);
//     });
//     chart.update();
// }




// {
//     label: ActivateWord[0],
//     fill: true,
//     lineTension: 0.3,
//     backgroundColor: "rgba(51, 179, 90, 0.38)",
//     borderColor: brandPrimary,
//     borderCapStyle: 'butt',
//     borderDash: [],
//     borderDashOffset: 0.0,
//     borderJoinStyle: 'miter',
//     borderWidth: 1,
//     pointBorderColor: brandPrimary,
//     pointBackgroundColor: "#fff",
//     pointBorderWidth: 1,
//     pointHoverRadius: 5,
//     pointHoverBackgroundColor: brandPrimary,
//     pointHoverBorderColor: "rgba(220,220,220,1)",
//     pointHoverBorderWidth: 2,
//     pointRadius: 1,
//     pointHitRadius: 10,
//     data: [50, 20, 40, 31, 32, 22, 10],
//     spanGaps: false
// },
// {
//     label: ActivateWord[1],
//     backgroundColor: "rgba(75,192,192,0.4)",
//     borderColor: "rgba(75,192,192,1)",
//     data: TRENDS_DATA[ActivateWord[1]],
//     pointBorderColor: "rgba(75,192,192,1)",
//     pointHoverBackgroundColor: "rgba(75,192,192,1)",


//     fill: true,
//     lineTension: 0.3,
//     borderCapStyle: 'butt',
//     borderDash: [],
//     borderDashOffset: 0.0,
//     borderJoinStyle: 'miter',
//     borderWidth: 1,
//     pointBackgroundColor: "#fff",
//     pointBorderWidth: 1,
//     pointHoverRadius: 5,
//     pointHoverBorderColor: "rgba(220,220,220,1)",
//     pointHoverBorderWidth: 2,
//     pointRadius: 1,
//     pointHitRadius: 10,
//     spanGaps: false
// }