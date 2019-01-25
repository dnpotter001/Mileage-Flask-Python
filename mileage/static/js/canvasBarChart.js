//gets the canvas from html file
const chartArea = document.getElementById("chart");
const chartButton = document.getElementById("generateChart");

chartButton.addEventListener("click", () => {
  if(fileInput.value) {
    let chart = new BarChart(
      chartArea,
      workout,
      60, // grid scale
      25, //padding
      10, //bar gap
    );

    console.log(chart.maxValue);
    chart.DrawGridLine();
    chart.drawBars();

  } else {
    fileNameLabel.innerHTML = "Upload a CSV first";

  }
})


function setupCanvas(canvas) {
  let dpr = window.devicePixelRatio || 1;
  let ctx = canvas.getContext('2d');
  let rect = canvas.getBoundingClientRect();
  //new scaling to improve sharpness
  canvas.width = rect.width * (2);
  canvas.height = rect.height * (2);
  ctx.scale(1, 1);
  return ctx;
}


function getIntervalData(workout){
  let graphData = [];
  for(x in workout.intervals){
    let interval = workout.intervals[x]
    let timeArray = interval[1].split(':');
    let totalSecond = (timeArray[0] * 60) + ((timeArray[1]/100) * 60);
    graphData[x] = totalSecond;
  }
  console.log(graphData);
  return graphData;
}

function getBarLabels(workout){
  let barLabels = [];
  for(x in workout.intervals){
    let interval = workout.intervals[x]
    barLabels[x] = interval[1];
  }
  return barLabels;
}

function drawLine(ctx, startX, startY, endX, endY, colour){
  ctx.save();
  ctx.strokeStyle = colour;
  ctx.lineWidth = 4 ;
  ctx.beginPath();
  ctx.moveTo(startX,startY);
  ctx.lineTo(endX, endY);
  ctx.stroke();
  ctx.restore();
}

function drawBar(ctx, upperLX, upperLY, width, height, colour, label){
  ctx.save();
  ctx.fillStyle = colour;
  ctx.font = "bold 30px Arial";
  ctx.textAlign ="center";
  ctx.fillRect(upperLX, upperLY, width, height);
  ctx.fillText(label, upperLX+(width/2), upperLY-5);
  ctx.restore();
}


/*-------------------GENERATE A NEW GRAPH OBJECT -------------------*/
let BarChart = function(canvas, workout, gridScale, padding, barGap){
  //take parameters and sets up canvas and data
  this.canvas = canvas;
  this.ctx = setupCanvas(this.canvas);
  this.data = getIntervalData(workout);
  this.barLabels = getBarLabels(workout);
  console.log(this.barLabels);

  //sets the max value
  this.maxValue = 0;
  for(x in this.data){
    if(this.maxValue < this.data[x]){
      this.maxValue = this.data[x];
    }
  }

  let canvasW = this.canvas.width - padding;
  let canvasH = this.canvas.height - padding;

  //function for drawing grid lines
  this.DrawGridLine = function(){
    let gridValue = 0;
    while(gridValue <= this.maxValue){
      let yHeight = (canvasH) * (1 - gridValue/this.maxValue) + padding;
      drawLine(
        this.ctx,
        0 + padding,
        yHeight, //-padding,
        canvasW ,
        yHeight,// -padding,
        "#000000"
      );

      //adds labels to lines
      this.ctx.save();
      this.ctx.font = "bold 30px Arial";
      console.log(gridValue);
      this.ctx.fillText(gridValue/60, 0, yHeight);
      this.ctx.restore();

      gridValue = gridValue + gridScale;
    }
  }

  this.drawBars = function(){
    let barNo = 0;
    let barWidth = canvasW / this.data.length;
    let barIncrement = (canvasH / this.maxValue) ;

    for(x in this.data){
      drawBar(
        this.ctx,
        barNo * barWidth + padding,
        (this.maxValue - this.data[x])*barIncrement +padding ,
        barWidth - (barGap *2),
        this.data[x] *barIncrement,
        getRandomColor(),
        this.barLabels[x],
      );
      barNo++
    }
  }

  this.drawLabel = function(){
    this.ctx.save();
    this.ctx.textBaseLine = "bottom";
    this.ctx.textAlign = "center";
    this.fillStyle = "#000000";
    this.ctx.font= "bold 40px Arial";
    this.ctx.fillText("Super chart", canvasW / 2, canvasH);
  }
}

function getRandomColor() {
  let letters = '0123456789ABCDEF';
  let color = '#';
  for (let i = 0; i < 6; i++) {
    color += letters[Math.floor(Math.random() * 16)];
  }
  return color;
}
