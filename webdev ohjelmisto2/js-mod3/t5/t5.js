'use strict';

const picArray = [
  {
    title: 'Title 1',
    caption: 'Caption 1',
    description: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.',
    image: {
      large: 'https://picsum.photos/id/10/800/600',
      medium: 'https://picsum.photos/id/10/400/300',
    },
  },
  {
    title: 'Title 2',
    caption: 'Caption 2',
    description: 'Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.',
    image: {
      large: 'https://picsum.photos/id/20/800/600',
      medium: 'https://picsum.photos/id/20/400/300',
    },
  },
  {
    title: 'Title 3',
    caption: 'Caption 3',
    description: 'Ut enim ad minim veniam, quis nostrud exercitation ullamco.',
    image: {
      large: 'https://picsum.photos/id/30/800/600',
      medium: 'https://picsum.photos/id/30/400/300',
    },
  },
];

const section = document.querySelector('#pictures');

for (const pic of picArray) {
  const article = document.createElement('article');
  article.classList.add('card');

  const h2 = document.createElement('h2');
  h2.textContent = pic.title;

  const figure = document.createElement('figure');

  const img = document.createElement('img');
  img.src = pic.image.medium;
  img.alt = pic.title;

  const figcaption = document.createElement('figcaption');
  figcaption.textContent = pic.caption;

  figure.appendChild(img);
  figure.appendChild(figcaption);

  const p = document.createElement('p');
  p.textContent = pic.description;

  article.appendChild(h2);
  article.appendChild(figure);
  article.appendChild(p);

  section.appendChild(article);
}
