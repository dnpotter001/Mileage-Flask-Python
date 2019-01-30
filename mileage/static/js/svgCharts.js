
let colours = []
let letters = '456789AB'

let chars = letters.split('')
chars.forEach(c => {
  colours.push(`#${c}${c}${c}${c}${c}${c}`)
})

console.log(colours)

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
      chartArea.innerHTML = "More intervals needed for bar chart. "
      return;
    }
    intervals.forEach(x => {
      let split = x[1].split(/./ && /:/)
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

    let barInc = 80 / maxValue

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
      label.innerHTML = x[1]

      let g = document.createElementNS(this.ns, 'g');
      g.appendChild(rect)
      g.appendChild(label)
      this.svg.appendChild(g)

    })
    area.appendChild(this.svg)
  }
}

let LineGraph = function (area) {

  this.createSVG = function () {
    this.ns = 'http://www.w3.org/2000/svg'
    this.svg = document.createElementNS(this.ns, 'svg')
    this.svg.setAttributeNS(null, 'width', '100%')
    this.svg.setAttributeNS(null, 'height', '100%')
    area.appendChild(this.svg)
  }

  this.drawSeries = function(intervals, series) {
    return;
  }
}
