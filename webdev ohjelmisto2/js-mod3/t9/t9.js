'use strict';

const calcInput = document.querySelector('#calculation');
const startBtn = document.querySelector('#start');
const resultP = document.querySelector('#result');

startBtn.addEventListener('click', function () {
  const input = calcInput.value.trim();
  let answer;

  if (input.includes('+')) {
    const parts = input.split('+');
    answer = Number(parts[0]) + Number(parts[1]);
  } else if (input.includes('-')) {
    const parts = input.split('-');
    answer = Number(parts[0]) - Number(parts[1]);
  } else if (input.includes('*')) {
    const parts = input.split('*');
    answer = Number(parts[0]) * Number(parts[1]);
  } else if (input.includes('/')) {
    const parts = input.split('/');
    const num1 = Number(parts[0]);
    const num2 = Number(parts[1]);
    answer = num2 !== 0 ? num1 / num2 : 'Cannot divide by zero';
  } else {
    answer = 'Invalid calculation';
  }

  resultP.textContent = answer;
});