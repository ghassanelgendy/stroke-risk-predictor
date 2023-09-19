document
	.getElementById("prediction-form")
	.addEventListener("submit", function (event) {
		event.preventDefault(); // Prevent form submission

		// Collect user input data from form
		var formData = new FormData(event.target);

		// Send a POST request to the server (Flask) for prediction
		fetch("/predict", {
			// Updated fetch URL
			method: "POST",
			body: formData,
		})
			.then((response) => response.json())
			.then((data) => {
				// Display the prediction result on the page
				document.getElementById("result-text").textContent = data.result;
				document.getElementById("prediction-result").style.display = "block";

				// Reset the form to clear previous input
				document.getElementById("prediction-form").reset();
			})
			.catch((error) => console.error("Error:", error));
	});
