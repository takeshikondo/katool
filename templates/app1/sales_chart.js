//x = ['8月1日', '8月2日', '8月3日', '8月4日', '8月5日', '8月6日', '8月7日']
x = [1, 2, 3, 4, 5, 6, 7, 8]
y1 = [35, 34, 37, 35, 34, 35, 34, 25]
y2 = [25, 27, 27, 25, 26, 27, 25, 21]
y_max = 40
y_min = 0
stepSize = 10

var ctx = document.getElementById("myChart");
var myChart = new Chart(ctx, {
    type: 'line',
    data: {        
        labels: x,        
        datasets: [
            {
                label: '最高気温(度）',
                data: y1,
                borderColor: "rgba(255,0,0,1)",
                backgroundColor: "rgba(255,0,0,0.1)"
            },            
            {
                label: '最低気温(度）',
                data: y2,
                borderColor: "rgba(0,0,255,1)",
                backgroundColor: "rgba(0,0,255,0.1)"
            }            
        ],
    },
    options: {
        title: {
            display: false,
            text: '気温（8月1日~8月7日）'
        },
        scales: {
            yAxes: [{
                ticks: {
                    suggestedMax: y_max,
                    suggestedMin: y_min,
                    stepSize: stepSize,
                    /*
                    callback: function(value, index, values){
                                return  value +  '度'
                    }
                    */   
                  }
              }]
        },
    }
});
