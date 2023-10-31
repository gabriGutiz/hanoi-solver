
var menu = document.getElementById('menu');
var start = document.getElementById('start');
var tryAgain = document.getElementById('tryAgain');
var tick = new Audio('assets/audio/tick.mp3');
start.addEventListener('submit', init);

var pegsState = {
  pegs: [
    {id: 0, name: 'Inicio', disks: [], level: 20, coord: {x: 100, y: 400, w: 200, h: 200}},
    {id: 2, name: 'Fim', disks: [], level: 20, coord: {x: 500, y: 400, w: 200, h: 200}},
    {id: 1, name: 'Auxiliar', disks: [], level: 20, coord: {x: 300, y: 400, w: 200, h: 200}},
  ]
}
var move = 0;

function drawPegs() {
  ctx.fillStyle = '#d1e0ff';
  ctx.fillRect(0, 0, canvas.width, canvas.height);

  ctx.lineWidth = 8
  pegsState.pegs.forEach(peg => {
    ctx.moveTo(peg.coord.x, peg.coord.y);
    ctx.lineTo(peg.coord.x + peg.coord.w, peg.coord.y);
    ctx.moveTo(peg.coord.x + 100, peg.coord.y);
    ctx.lineTo(peg.coord.x + 100, peg.coord.y - peg.coord.h);

    ctx.fillStyle = 'black';
    ctx.font = '20px Helvetica, Arial, sans-serif';
    ctx.textAlign = 'center';
    ctx.fillText(peg.name, peg.coord.x + 100, peg.coord.y + 40);
  });
  ctx.stroke();
}

function Disk(x, y, width, height, color) {
  this.x = x;
  this.y = y;
  this.width = width;
  this.height = height;
  this.color = color;
}

Disk.prototype.draw = function() {
  ctx.fillStyle = this.color;
  ctx.lineWidth = 1;
  ctx.fillRect(this.x, this.y, this.width, this.height);
  ctx.strokeRect(this.x, this.y, this.width, this.height);
};

function initDisks(n) {
  var peg = pegsState.pegs[0].coord;
  var colors = ['#aa1414', '#ce1414', '#f74545', '#f7a145', '#c5e56b', '#5bff0a', '#28ede9', '#84c5ff', '#2295f9', '#5f22f9'];
  var width = 20 * n;
  for(var i = n; i > 0; i--) {
    let disk = new Disk((peg.w/2 + (peg.w - width)/2), peg.y - pegsState.pegs[0].level, width, peg.h/10, '#ffc2cd');
    pegsState.pegs[0].disks.push(disk);
    pegsState.pegs[0].level += peg.h / 10;
    width -= 20;
  }
}


function drawDisks(state) {
  state.pegs.forEach(function(peg) {
    peg.disks.forEach(function(disk) {
        disk.draw();
    });
  })
}

var delay = 1;
function moveDisk(from, to) {
    setTimeout(function() {
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      var movingDisk = from.disks.pop();
      movingDisk.x += (to.id - from.id) * 200;
      movingDisk.y = 400 - to.level;
      tick.play();
      to.disks.push(movingDisk);
      from.level -= 20;
      to.level += 20;
      drawPegs();
      drawDisks(pegsState);
      move++;
    }, 1000 * delay)
    delay++;
}

function hanoi(n, moves, from, to, aux) {
  if(n >= 1) {
    moves = hanoi(n-1, moves, from, aux, to);
    moveDisk(from, to);
    moves++;
    console.log("DE: " + from.name + " PARA: " + to.name);
    moves = hanoi(n-1, moves, aux, to, from);
  }
  return moves;
}

function init(e) {
  e.preventDefault();
  var num = Number(document.getElementById('disks').value);
  menu.style.display = 'none';
  canvas.style.display = 'block';
  canvas = document.getElementById('canvas');
  canvas.width = canvas.scrollWidth;
  canvas.height = canvas.scrollHeight;
  ctx = canvas.getContext('2d');
  initDisks(num);
  var moves = hanoi(num, 0, ...pegsState.pegs);
  console.log('MOVES: ' + moves);
  tryAgain.style.display = 'block';
}
