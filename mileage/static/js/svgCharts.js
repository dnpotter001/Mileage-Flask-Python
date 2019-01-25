

function BarChart(intervals) {
  const chartArea = document.getElementById("graph");
  console.log(intervals)

  let ns = 'http://www.w3.org/2000/svg'
  let svg = document.createElementNS(ns, 'svg')
  svg.setAttributeNS(null, 'width', '100%')
  svg.setAttributeNS(null, 'height', '100%')
  chartArea.appendChild(svg)

  let barCount = intervals.length
  console.log(chartArea.getBoundingClientRect())
  let barInc = 90 / barCount
  let barHeight = 90 / barCount;

  intervals.forEach(x => {
    let barNumber = 0;
    let rect = document.createElementNS(ns, 'rect')
    rect.setAttributeNS(null, 'width', barInc * x[0] + "%")
    rect.setAttributeNS(null, 'height', barHeight + "%")
    rect.setAttributeNS(null, 'y', (barHeight * x[0]) -2 + "%")

    rect.setAttributeNS(null, 'fill', '#f06')
    svg.appendChild(rect) 
  })
  chartArea.appendChild(svg)





}

function TableFull(inervals) { }
