'use strict';

const names = ['John', 'Paul', 'Jones'];
const target = document.querySelector('#target');

let html = '';
for (const name of names) {
  html += '<li>' + name + '</li>';
}

target.innerHTML = html; 