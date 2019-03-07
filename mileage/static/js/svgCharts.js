
let colours = []
let letters = '456789AB'

let chars = letters.split('')
chars.forEach(c => {
  colours.push(`#${c}${c}${c}${c}${c}${c}`)
})


let BarChart = function (area, intervals) {

  this.createSVG = function () {
    this.ns = 'http://www.w3.org/2000/svg'
    this.svg = document.createElementNS(this.ns, 'svg')
    this.svg.setAttributeNS(null, 'width', '100%')
    this.svg.setAttributeNS(null, 'height', '100%')
    area.appendChild(this.svg)
  }

  this.drawSeries = function () {
    let barCount = intervals.length
    let barHeight = 100 / barCount;
    let maxValue = 0;

    if (barCount == 1) {
      area.innerHTML = "More intervals needed for bar chart. "
      if (window.screen.width <= "800"){
        area.style.height = "20px"
      }
      return;
    }
    intervals.forEach(x => {
      let split = x[4].split(/./ && /:/)
      let totalTime = 0;
      if (split.length == 2) {
        totalTime = (split[0] * 60) + parseFloat(split[1]);
      } else {
        totalTime = (split[0] * 60 * 60) + (split[1] * 60) + parseFloat(split[2]);
      }
      if (totalTime > maxValue) {
        maxValue = totalTime
      }
      x.push(totalTime);
    })

    let barInc = 70 / maxValue

    intervals.forEach(x => {
      let totalTime = x.pop()

      let rect = document.createElementNS(this.ns, 'rect')
      rect.setAttributeNS(null, 'width', barInc * totalTime + "%")
      rect.setAttributeNS(null, 'height', barHeight - 2 + "%")
      rect.setAttributeNS(null, 'y', (x[0] - 1) * barHeight + 2 + "%")
      rect.setAttributeNS(null, 'fill', colours[x[0] % colours.length])

      let label = document.createElementNS(this.ns, 'text')
      label.setAttributeNS(null, 'y', (x[0] - 0.5) * barHeight + 2.75 + "%");
      label.setAttributeNS(null, 'x', (barInc * totalTime) + 1 + "%");
      label.innerHTML = x[3]

      let g = document.createElementNS(this.ns, 'g');
      g.appendChild(rect)
      g.appendChild(label)
      this.svg.appendChild(g)

    })
    area.appendChild(this.svg)
  }
}

let LineGraph = function (area, intervals) {
  this.seriesCount = 0

  this.createSVG = function () {
    this.ns = 'http://www.w3.org/2000/svg'
    this.svg = document.createElementNS(this.ns, 'svg')
    this.svg.setAttributeNS(null, 'width', '100%')
    this.svg.setAttributeNS(null, 'height', '100%')
    area.appendChild(this.svg)
  }

  this.drawSeries = function (series, colour, seriesName) {

    let dotCount = intervals.length
    let dotWidth = 75 / dotCount;
    let maxValue = 0;

    if (dotCount == 1) {
      area.innerHTML = "More intervals needed for a line graph. "
      area.style.height = "20px"
      return;
    }
    intervals.forEach(x => {
      //console.log(x[series])
      if (x[series] < 0){
        x[series] = x[series] * - 1
        //console.log(x[series])
      }
    })
    let minValue = intervals[0][series];


    intervals.forEach(x => {
      if (x[series] > maxValue) {
        maxValue = x[series]
      }
      if (x[series] < minValue) {
        minValue = x[series]
      }

    })
    console.log("max and min ", maxValue, minValue)

    let dotInc = -300 / maxValue
    console.log("dot inc and width", dotInc, dotWidth)

    intervals.forEach((interval) => {
      let dot = document.createElementNS(this.ns, 'circle');
      dot.setAttributeNS(null, 'r', 2)
      dot.setAttributeNS(null, 'cx', (interval[0] - 0.5) * dotWidth + "%")
      dot.setAttributeNS(null, 'cy', (interval[series]) * dotInc + 330 + "%")
      dot.setAttributeNS(null, 'fill', colour)
      this.svg.appendChild(dot)
    })

    let lineNo = 1
    let index = 0
    while (lineNo < dotCount) {
      let line = document.createElementNS(this.ns, 'line');
      line.setAttributeNS(null, 'x1', (intervals[index][0] - 0.5) * dotWidth + "%")
      line.setAttributeNS(null, 'y1', intervals[index][series] * dotInc + 330 + "%")
      line.setAttributeNS(null, 'x2', (intervals[index + 1][0] - 0.5) * dotWidth + "%")
      line.setAttributeNS(null, 'y2', intervals[index + 1][series] * dotInc + 330 + "%")
      line.setAttributeNS(null, 'style', `stroke:${colour};stroke-width:2`)
      this.svg.appendChild(line)
      lineNo = lineNo + 1
      index = index + 1
    }

    let key = document.createElementNS(this.ns, 'line');
    key.setAttributeNS(null, 'x1', 75 + "%")
    key.setAttributeNS(null, 'y1', 5 + (this.seriesCount * 15) + "%")
    key.setAttributeNS(null, 'x2', 80 + "%")
    key.setAttributeNS(null, 'y2', 5 + (this.seriesCount * 15) + "%")
    key.setAttributeNS(null, 'style', `stroke:${colour};stroke-width:2`)
    this.svg.appendChild(key)

    let keyText = document.createElementNS(this.ns, 'text');
    keyText.setAttributeNS(null, 'x', 81 + "%")
    keyText.setAttributeNS(null, 'y', 9 + (this.seriesCount * 15) + "%")
    keyText.innerHTML = seriesName;
    this.svg.appendChild(keyText)

    this.seriesCount = this.seriesCount + 1


    return;
  }
}

let AngleView = function (area) {

  this.createSVG = function () {
    this.ns = 'http://www.w3.org/2000/svg'
    this.svg = document.createElementNS(this.ns, 'svg')
    this.svg.setAttributeNS(null, 'width', '100%')
    this.svg.setAttributeNS(null, 'height', '100%')
    area.appendChild(this.svg)
  }

  this.drawAngles = function(cat, fin, slip, wash){

    //draw cross
    let verticleAxis = document.createElementNS(this.ns, 'line');
    verticleAxis.setAttributeNS(null, 'x1', 50 + "%")
    verticleAxis.setAttributeNS(null, 'y1', 0 + "%")
    verticleAxis.setAttributeNS(null, 'x2', 50 + "%")
    verticleAxis.setAttributeNS(null, 'y2', 100 + "%")
    verticleAxis.setAttributeNS(null, 'style', `stroke:black;stroke-width:2`)

    let horizontalAxis = document.createElementNS(this.ns, 'line');
    horizontalAxis.setAttributeNS(null, 'x1', 0 + "%")
    horizontalAxis.setAttributeNS(null, 'y1', 50 + "%")
    horizontalAxis.setAttributeNS(null, 'x2', 100 + "%")
    horizontalAxis.setAttributeNS(null, 'y2', 50 + "%")
    horizontalAxis.setAttributeNS(null, 'style', `stroke:black;stroke-width:2`)

    this.svg.appendChild(verticleAxis)
    this.svg.appendChild(horizontalAxis)

    //catch
    
  }
}

