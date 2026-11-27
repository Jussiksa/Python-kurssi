'use strict';

const form = document.querySelector('#search-form');
const queryInput = document.querySelector('#query');

form.addEventListener('submit', async function (event) {
  event.preventDefault();
  const valueFromInput = queryInput.value.trim();
  if (!valueFromInput) return;

  try {
    const response = await fetch(
      `https://api.tvmaze.com/search/shows?q=${encodeURIComponent(valueFromInput)}`
    );
    const data = await response.json();
    console.log(data);
  } catch (error) {
    console.error('Error fetching data:', error);
  }
});
