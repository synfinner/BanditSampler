# BanditSampler

This script attempts to fetch all of the compiled Bandit Stealer binaries stored on a discovered Bandit Stealer panel. 

Huge shout out to [@TLP_R3D](https://twitter.com/@TLP_R3D) and [@josh_penny](https://twitter.com/josh_penny)!

## Setup 

`pip3 install -r requirements.txt`

## How

From several of the Bandit Stealer panels I came across, I noted two methods on how the panels allow admins to download their compiled binaries via a list that is populated from a requst to /builds. Naturally, we can just script that same process 😉. 

Method 1 relies on a POST request containing the file name, whereas Method 2 uses a GET request to /downloads. I'm sure there are more.

### Method 1

```
fetch('http://localhost:8080/builds')
	.then(response => response.json())
	.then(data => {
		data.forEach(file => {
			const row = document.createElement('tr');

			const fileNameCell = document.createElement('td');
			fileNameCell.textContent = file.name;
			row.appendChild(fileNameCell);

			const fileDateCell = document.createElement('td');
			fileDateCell.textContent = file.date;
			row.appendChild(fileDateCell);

			const fileSizeCell = document.createElement('td');
			fileSizeCell.textContent = file.size;
			row.appendChild(fileSizeCell);

			const downloadCell = document.createElement('td');
			const downloadLink = document.createElement('button');
			downloadLink.textContent = 'Download';
			downloadLink.className = 'btn btn-outline-theme btn-sm';
			downloadLink.addEventListener('click', function() {
				fetch(`http://localhost:8080/builds/download?fileName=${encodeURIComponent(file.name)}`, {
						method: 'POST',
					})
					.then(response => response.blob())
					.then(blob => {
						var url = window.URL.createObjectURL(blob);
						var a = document.createElement('a');
						a.href = url;
						a.download = file.name;
						document.body.appendChild(a);
						a.click();
						a.remove();
					});
			});

			downloadCell.appendChild(downloadLink);
			row.appendChild(downloadCell);

			// Append the row to the table body
			buildsTableBody.appendChild(row);
		});
	})
	.catch(error => {
		console.error('Error:', error);
	});
```

### Method 2

```
fetch('http://localhost:8080/builds')
	.then(response => response.json())
	.then(data => {
		data.forEach(file => {
			const row = document.createElement('tr');

			const fileNameCell = document.createElement('td');
			fileNameCell.textContent = file.name;
			row.appendChild(fileNameCell);

			const fileDateCell = document.createElement('td');
			fileDateCell.textContent = file.date;
			row.appendChild(fileDateCell);

			const fileSizeCell = document.createElement('td');
			fileSizeCell.textContent = file.size;
			row.appendChild(fileSizeCell);

			const downloadCell = document.createElement('td');
			const downloadLink = document.createElement('button');
			downloadLink.textContent = 'Download';
			downloadLink.className = 'btn btn-outline-theme btn-sm';
			downloadLink.addEventListener('click', function() {
				fetch(`http://localhost:8080/downloads?fileName=${encodeURIComponent(file.name)}`, {
						method: 'GET',
					})
					.then(response => response.blob())
					.then(blob => {
						var url = window.URL.createObjectURL(blob);
						var a = document.createElement('a');
						a.href = url;
						a.download = file.name;
						document.body.appendChild(a);
						a.click();
						a.remove();
					});
			});

			downloadCell.appendChild(downloadLink);
			row.appendChild(downloadCell);

			// Append the row to the table body
			buildsTableBody.appendChild(row);
		});
	})
	.catch(error => {
		console.error('Error:', error);
	});
```