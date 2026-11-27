'use strict';

const form = document.querySelector('#joke-form');
const queryInput = document.querySelector('#query');
const resultsSection = document.querySelector('#results');

form.addEventListener('submit', async function (event) {
  event.preventDefault();
  const searchTerm = queryInput.value.trim();
  if (!searchTerm) return;

  resultsSection.innerHTML = '';

  try {
    const response = await fetch(
      `https://api.chucknorris.io/jokes/search?query=${encodeURIComponent(searchTerm)}`
    );
    const data = await response.json();

    for (const joke of data.result) {
      const article = document.createElement('article');
      const p = document.createElement('p');
      p.textContent = joke.value;
      article.appendChild(p);
      resultsSection.appendChild(article);
    }
  } catch (error) {
    console.error('Error searching jokes:', error);
  }
});
