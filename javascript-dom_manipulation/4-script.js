document.addEventListener('DOMContentLoaded', function() {
	const addItemButton = document.getElementById('add_item');
	const myList = document.querySelector('.my_list');
  
	addItemButton.addEventListener('click', function() {
	  // Create a new <li> element
	  const newItem = document.createElement('li');
	  newItem.textContent = 'Item'; // Set the text content of the new <li>
  
	  // Append the new <li> element to the <ul>
	  myList.appendChild(newItem);
	});
  });
  