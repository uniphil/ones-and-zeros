var lede; if (lede = document.getElementsByClassName('lede')[0]) {
  var current = 1;
  var TOTAL = 16;

  function name(n) {
    var s = ('0' + n).slice(-2);  // zero-pad
    return 'url("static/media/carousel/' + s + '.JPG")';
  }

  var bg = document.createElement('div');
  var next = document.createElement('div');
  bg.setAttribute('class', 'bg');
  next.setAttribute('class', 'bg next');
  next.style.backgroundImage = name(++current);
  lede.appendChild(bg);
  lede.appendChild(next);

  function advance() {
    if (++current > TOTAL) current = 1;
    next.setAttribute('class', 'bg next fade-in');
    setTimeout(function() {
      bg.style.backgroundImage = next.style.backgroundImage;
      next.setAttribute('class', 'bg next');
      next.style.backgroundImage = name(current);
    }, 2000);
  }

  lede.style.background = 'transparent';

  setInterval(advance, 6000);
}
