function getInputValues() {
    // Retrieve values from input fields
    const age = document.getElementById('age').value;
    const hyper_tension = document.getElementById('hypertension').value;
    const heart_disease = document.getElementById('heart').value;
    const work_type = document.getElementById('work').value;
    const marry = document.getElementById('marry').value;
    const smoking = document.getElementById('smoking').value;
    const bmi = document.getElementById('bmi').value;
    const glucose = document.getElementById('glucose').value;


    for (const i of work_type) {
        if (i.checked) {
        work_type_value = i.value;
        break; 
        }
    }



    // Create a JavaScript object to hold the values
    const data = {
        age: age,
        hyper_tension: hyper_tension,
        heart_disease: heart_disease,
        work_type_value: work_type,
        marry: marry,
        smoking: smoking,
        bmi: bmi,
    fglucose: glucose,
    };

    // Send the data as JSON to the Flask backend
    fetch('/predict', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
    },
    body: JSON.stringify(data),
    })
    .then(response => response.json())
    .then(responseData => {
        const prediction = responseData.prediction;

      // Display the prediction result to the user
    const resultElement = document.getElementById('result');
    
      // Set the text based on the prediction
    if (prediction === 1) {
        document.getElementById("result").innerText="he is really dead";
    } else {
        document.getElementById("result").innerText="luckily he survived";
    }
    })
    .catch(error => {
        console.error('Error:', error);
    });
}












