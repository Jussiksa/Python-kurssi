'use strict';

const trigger = document.querySelector('#trigger');
const target = document.querySelector('#target');

const picA = 'https://picsum.photos/id/10/400/300';
const picB = 'https://picsum.photos/id/20/400/300';

trigger.addEventListener('mouseover', function () {
  target.src = picB;
});

trigger.addEventListener('mouseout', function () {
  target.src = picA;
});