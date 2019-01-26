

function BarChart(intervals) {
  const chartArea = document.getElementById("graph");
  console.log(intervals)

  let ns = 'http://www.w3.org/2000/svg'
  let svg = document.createElementNS(ns, 'svg')
  svg.setAttributeNS(null, 'width', '100%')
  svg.setAttributeNS(null, 'height', '100%')
  chartArea.appendChild(svg)

  let barCount = intervals.length
  let barHeight = 100/barCount;
  let maxValue= 0;
  //calc times and max value
  intervals.forEach(x => {
    let split = x[1].split(/./ && /:/)
    let totalTime = (split[0] * 60) + parseFloat(split[1]);
    if (totalTime > maxValue){
      maxValue = totalTime
    }
    x.push(totalTime);
  })

  let barInc = 100 / maxValue
  console.log(barCount, barHeight, maxValue, barInc)

  intervals.forEach(x => {
    let totalTime = x.pop()
    let rect = document.createElementNS(ns, 'rect')
    rect.setAttributeNS(null, 'width', barInc * totalTime + "%")
    rect.setAttributeNS(null, 'height', barHeight -2 + "%")
    rect.setAttributeNS(null, 'y', (x[0] -1) * barHeight +2+ "%")
    rect.setAttributeNS(null, 'fill', '#f06')
    svg.appendChild(rect) 
  })
  chartArea.appendChild(svg)
}

