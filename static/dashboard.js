window.onload = function () {
    // Create the notification dynamically
    const notification = document.createElement('div');
    notification.className = 'notification';
    notification.textContent = 'Login Successful!';

    // Append it to the body
    document.body.appendChild(notification);

    // Show the notification
    notification.style.display = 'block';

    // Remove the notification after 5 seconds
    setTimeout(() => {
        notification.style.display = 'none'; // Hide it
        document.body.removeChild(notification); // Remove from DOM
    }, 5000);
};
