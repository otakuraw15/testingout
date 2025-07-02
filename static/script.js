document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('data-form');
    const latitudeDisplay = document.getElementById('latitude');
    const longitudeDisplay = document.getElementById('longitude');
    const messageDisplay = document.getElementById('message');

    form.addEventListener('submit', async (event) => {
        event.preventDefault();
        messageDisplay.textContent = ''; // Clear previous messages

        // Get form data
        const field1 = document.getElementById('field1').value;
        const field2 = document.getElementById('field2').value;
        const field3 = document.getElementById('field3').value;

        if (!field1 || !field2 || !field3) {
            messageDisplay.textContent = 'Please fill in all three fields.';
            messageDisplay.style.color = 'red';
            return;
        }

        // Get geolocation
        if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(async (position) => {
                const latitude = position.coords.latitude;
                const longitude = position.coords.longitude;

                latitudeDisplay.textContent = latitude.toFixed(6);
                longitudeDisplay.textContent = longitude.toFixed(6);

                const data = {
                    latitude: latitude,
                    longitude: longitude,
                    field1: field1,
                    field2: field2,
                    field3: field3
                };

                // For now, we'll just log to console and display a success message.
                // Backend integration will be in a later step.
                console.log('Data to send:', data);
                messageDisplay.textContent = 'Data captured! Check console. Backend integration pending.';
                messageDisplay.style.color = 'green';

                // TODO: Send data to backend
                // try {
                //     const response = await fetch('/submit_data', {
                //         method: 'POST',
                //         headers: {
                //             'Content-Type': 'application/json',
                //         },
                //         body: JSON.stringify(data),
                //     });
                //     if (response.ok) {
                //         const result = await response.json();
                //         messageDisplay.textContent = `Data submitted successfully! Server response: ${result.message}`;
                //         messageDisplay.style.color = 'green';
                //         form.reset(); // Clear the form
                //     } else {
                //         messageDisplay.textContent = `Error: ${response.statusText}`;
                //         messageDisplay.style.color = 'red';
                //     }
                // } catch (error) {
                //     console.error('Error sending data:', error);
                //     messageDisplay.textContent = 'Error sending data. See console for details.';
                //     messageDisplay.style.color = 'red';
                // }

            }, (error) => {
                console.error("Error getting location:", error);
                latitudeDisplay.textContent = 'Error';
                longitudeDisplay.textContent = 'Error';
                messageDisplay.textContent = `Error getting location: ${error.message}. Please ensure location services are enabled and permission is granted.`;
                messageDisplay.style.color = 'red';
            });
        } else {
            messageDisplay.textContent = "Geolocation is not supported by this browser.";
            messageDisplay.style.color = 'red';
            latitudeDisplay.textContent = 'N/A';
            longitudeDisplay.textContent = 'N/A';
        }
    });
});
