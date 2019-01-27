function getRandomColor() {
  let letters = '0123456789ABCDEF';
  let color = '#';
  for (let i = 0; i < 6; i++) {
    color += letters[Math.floor(Math.random() * 16)];
  }
  return color;
}

function BarChart(intervals) {
  const chartArea = document.getElementById("barChart");
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
    let totalTime = 0;
    console.log(split)
    if (split.length == 2){
      totalTime = (split[0] * 60) + parseFloat(split[1]);
    } else {
      totalTime = (split[0]* 60 * 60) + (split[1] * 60) + parseFloat(split[2]);
    }
    if (totalTime > maxValue){
      maxValue = totalTime
    }
    console.log(totalTime)
    x.push(totalTime);
  })

  let barInc = 80 / maxValue
  console.log(barCount, barHeight, maxValue, barInc)

  intervals.forEach(x => {
    let totalTime = x.pop()
    let rect = document.createElementNS(ns, 'rect')
    rect.setAttributeNS(null, 'width', barInc * totalTime + "%")
    rect.setAttributeNS(null, 'height', barHeight -2 + "%")
    rect.setAttributeNS(null, 'y', (x[0] -1) * barHeight +2+ "%")
    rect.setAttributeNS(null, 'fill', getRandomColor())

    let label = document.createElementNS(ns, 'text')
    label.setAttributeNS(null, 'y', (x[0]-0.5) * barHeight + 2 +  "%");
    label.setAttributeNS(null, 'x', (barInc * totalTime)+ 1 + "%");
    label.innerHTML = x[1]
    
    svg.appendChild(label) 
    svg.appendChild(rect) 
   
  })
  chartArea.appendChild(svg)
}

