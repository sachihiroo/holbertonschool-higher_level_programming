document.addEventListener('DOMContentLoaded', () => {
	fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
	 .then(res => res.json())
	 .then(({ name }) => document.getElementById('character').innerText = name)
	 .catch(err => console.error('Error fetching character:', err));
  });
  