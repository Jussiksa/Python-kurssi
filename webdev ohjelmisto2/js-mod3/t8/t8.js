'use strict';

const num1Input = document.querySelector('#num1');
const num2Input = document.querySelector('#num2');
const operationSelect = document.querySelector('#operation');
const startBtn = document.querySelector('#start');
const resultP = document.querySelector('#result');

startBtn.addEventListener('click', function () {
  const num1 = Number(num1Input.value);
  const num2 = Number(num2Input.value);
  const operation = operationSelect.value;
  let answer;

  if (operation === 'add') {
    answer = num1 + num2;
  } else if (operation === 'sub') {
    answer = num1 - num2;
  } else if (operation === 'multi') {
    answer = num1 * num2;
  } else if (operation === 'div') {
    answer = num2 !== 0 ? num1 / num2 : 'Cannot divide by zero';
  }

  resultP.textContent = answer;
});
