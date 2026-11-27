'use strict';

const form = document.querySelector('#source');
const firstNameInput = document.querySelector('input[name="fName"]');
const lastNameInput = document.querySelector('input[name="lName"]');
const target = document.querySelector('#target');

form.addEventListener('submit', function (event) {
  event.preventDefault();
  target.textContent = `Your name is ${firstNameInput.value} ${lastNameInput.value}`;
});